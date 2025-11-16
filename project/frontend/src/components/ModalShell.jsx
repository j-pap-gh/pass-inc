
import React from "react";
import { useUIStore } from "../state/useUIStore";

export default function ModalShell({ children }) {
  const close = useUIStore((s) => s.closeModal);

  return (
    <div
      className="fixed inset-0 bg-black/40 backdrop-blur-sm flex items-center justify-center z-50"
      onClick={close}
    >
      <div
        className="bg-white w-full max-w-lg rounded-xl p-6 shadow-xl"
        onClick={(e) => e.stopPropagation()}
      >
        {children}
      </div>
    </div>
  );
}
