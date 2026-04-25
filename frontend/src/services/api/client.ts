import axios from "axios";
import { ACCESS_TOKEN } from "../../constants/constants";

export type ApiErrorPayload = {
  code: string;
  message: string;
  fields: Record<string, unknown>;
  trace_id?: string;
};


const client_api = axios.create({
  baseURL: window.location.origin,
  withCredentials: true,
});

client_api.interceptors.request.use(async (config) => {
  const token = localStorage.getItem(ACCESS_TOKEN);
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

client_api.interceptors.response.use(
  (response) => response,
  (error) => {

    return Promise.reject(error);
  },
);

export default client_api;