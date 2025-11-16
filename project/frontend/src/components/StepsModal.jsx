
import React from "react";
import ModalShell from "./ModalShell";
import { useUIStore } from "../state/useUIStore";

export default function StepsModal() {
  const modal = useUIStore((s) => s.modal);
  const close = useUIStore((s) => s.closeModal);

  if (!modal?.plan) return null;
  const { plan } = modal;

  return (
    <ModalShell>
      <h2 className="text-2xl font-bold mb-4">Steps for {plan.title}</h2>

      <div className="space-y-3 mb-6">
        {plan.steps?.map((step, i) => (
          <div key={i} className="p-3 border rounded-lg bg-gray-50">
            {step}
          </div>
        ))}
      </div>

      <button
        onClick={close}
        className="w-full bg-gray-800 text-white py-2 rounded-lg"
      >
        Close
      </button>
    </ModalShell>
  );
}
