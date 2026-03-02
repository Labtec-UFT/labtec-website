import axios from "axios";
import { ACCESS_TOKEN } from "../../constants/constants";

const client_api = axios.create({
  baseURL: "http://localhost:8000",
});

client_api.interceptors.request.use(async (config) => {
  const token = localStorage.getItem(ACCESS_TOKEN);
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default client_api;