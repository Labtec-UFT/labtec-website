// src/context/AuthContext.tsx
import { createContext, useState, useEffect, useCallback } from "react";
import type { ReactNode } from "react";
import { jwtDecode } from "jwt-decode";
import api from "../services/api/client";
import { ACCESS_TOKEN } from "../constants/constants";


type JwtPayload = { exp: number; [key: string]: unknown };

interface AuthContextType {
  user: JwtPayload | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
}

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<JwtPayload | null>(null);
  const [loading, setLoading] = useState(true);

  // Tenta renovar o access token usando o refresh token (cookie httpOnly)
  const refreshAccessToken = useCallback(async (): Promise<string | null> => {
    try {
      const res = await api.post("/api/v1/token/refresh/");
      const access: string = res.data.access;
      localStorage.setItem(ACCESS_TOKEN, access);
      return access;
    } catch {
      localStorage.removeItem(ACCESS_TOKEN);
      return null;
    }
  }, []);

  // Verifica se o token atual é válido; se expirado, tenta renovar
  const checkAuth = useCallback(async () => {
    let token = localStorage.getItem(ACCESS_TOKEN);

    if (token) {
      const decoded = jwtDecode<JwtPayload>(token);
      const now = Date.now() / 1000;

      if (decoded.exp < now) {
        token = await refreshAccessToken();
      }
    } else {
      token = await refreshAccessToken();
    }

    if (token) {
      setUser(jwtDecode<JwtPayload>(token));
    } else {
      setUser(null);
    }
  }, [refreshAccessToken]);

  useEffect(() => {
    checkAuth().finally(() => setLoading(false));
  }, [checkAuth]);

  const login = async (email: string, password: string) => {
    const res = await api.post("/api/v1/login/", { email, password });
    const access: string = res.data.access;
    localStorage.setItem(ACCESS_TOKEN, access);
    setUser(jwtDecode<JwtPayload>(access));
  };

  const logout = async () => {
    try {
      await api.post("/api/v1/logout/");
    } finally {
      localStorage.removeItem(ACCESS_TOKEN);
      setUser(null);
    }
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}