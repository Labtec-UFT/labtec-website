import { useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../../context/AuthContext";
import { LOGIN_ROUTE } from "../../../constants/constants";

export default function Logout() {
  const auth = useContext(AuthContext);
  if (!auth) throw new Error("AuthContext não encontrado");

  const { logout } = auth;
  const navigate = useNavigate();

  useEffect(() => {
    logout().finally(() => {
      navigate(LOGIN_ROUTE, { replace: true });
    });
  }, []);

  return (
    <div className="flex items-center justify-center w-full h-screen">
      <p className="text-gray-500 text-sm">Saindo...</p>
    </div>
  );
}
