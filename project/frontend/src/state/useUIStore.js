
import { create } from "zustand";

export const useUIStore = create((set) => ({
  modal: null,

  openModal: (value) => set({ modal: value }),
  closeModal: () => set({ modal: null })
}));
