import { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";

import Input from "@components/commons/Input";
import Button from "@components/commons/Button";
import logo from "@assets/labtec_black.png";

import { AuthContext } from "../../../context/AuthContext";
import { HOME_ROUTE } from "../../../constants/constants";

export default function Login() {
  const auth = useContext(AuthContext);
  if (!auth) throw new Error("AuthContext não encontrado");

  const { login } = auth;
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      await login(email, password);
      navigate(HOME_ROUTE, { replace: true });
    } catch (err: unknown) {
      if (
        typeof err === "object" &&
        err !== null &&
        "response" in err
      ) {
        const axiosErr = err as { response?: { data?: { detail?: string } } };
        setError(axiosErr.response?.data?.detail ?? "Credenciais inválidas.");
      } else {
        setError("Erro ao conectar com o servidor.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center gap-6 w-full h-screen overflow-hidden">

      <div className="flex flex-col items-center gap-2">
        <img src={logo} alt="Logo Labtec" className="w-20" />
        <p className="text-xl font-bold tracking-wide">Entre na sua Conta</p>
        <p className="text-sm text-gray-500 tracking-wide">Dashboard</p>
      </div>

      <form onSubmit={handleSubmit} className="flex flex-col items-center gap-6">
        <Input
          label="Endereço de Email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          autoComplete="email"
        />

        <Input
          label="Senha"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          autoComplete="current-password"
        />

        {error && (
          <p className="text-sm text-red-500 text-center w-85">{error}</p>
        )}

        <Button text={loading ? "Entrando..." : "ENTRAR"} />
      </form>
    </div>
  );
}