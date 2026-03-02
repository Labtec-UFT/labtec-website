// src/routes/ProtectedRoute.tsx
import { useContext, type JSX } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext.tsx";
import { LOGIN_ROUTE } from "../../constants/constants.ts";

interface ProtectedRouteProps {
  children: JSX.Element;
}

export default function ProtectedRoute({ children }: ProtectedRouteProps) {
  const auth = useContext(AuthContext);

  if (!auth) throw new Error("AuthContext não encontrado");

  const { user, loading } = auth;

  if (loading) return <div>Carregando!</div>;

  return user ? children : <Navigate to={LOGIN_ROUTE} replace />;
}