import { createContext } from "react";

export type JwtPayload = { exp: number; [key: string]: unknown };

export interface AuthContextType {
  user: JwtPayload | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
}

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

