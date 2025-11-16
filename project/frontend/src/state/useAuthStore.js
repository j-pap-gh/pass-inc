
import { create } from "zustand";
import api from "../api/apiClient";

export const useAuthStore = create((set) => ({
  user: null,
  token: null,
  loading: false,

  setUser: (user) => set({ user }),
  setToken: (token) => set({ token }),

  login: async (email, password) => {
    set({ loading: true });
    try {
      const res = await api.post("/auth/login", { email, password });
      set({ token: res.data.token, user: res.data.user });
    } finally {
      set({ loading: false });
    }
  },

  logout: () => {
    set({ token: null, user: null });
  },

  refreshUser: async () => {
    try {
      const res = await api.get("/auth/me");
      set({ user: res.data });
    } catch {
      set({ user: null });
    }
  }
}));
