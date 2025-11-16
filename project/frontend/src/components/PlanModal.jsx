
import React from "react";
import ModalShell from "./ModalShell";
import { useUIStore } from "../state/useUIStore";

export default function PlanModal() {
  const modal = useUIStore((s) => s.modal);
  const close = useUIStore((s) => s.closeModal);

  if (!modal?.plan) return null;
  const { plan } = modal;

  return (
    <ModalShell>
      <h2 className="text-2xl font-bold mb-3">{plan.title}</h2>
      <p className="text-gray-700 mb-4">{plan.summary}</p>

      <div className="space-y-1 text-gray-600 text-sm mb-6">
        <p><strong>Capital:</strong> {plan.capital}</p>
        <p><strong>Time to Income:</strong> {plan.timeframe}</p>
        <p><strong>Risk:</strong> {plan.risk}</p>
      </div>

      {plan.details && <p className="text-gray-700 mb-6">{plan.details}</p>}

      <button
        onClick={close}
        className="w-full bg-gray-800 text-white py-2 rounded-lg"
      >
        Close
      </button>
    </ModalShell>
  );
}
