
import React from "react";
import { useQuery } from "@tanstack/react-query";
import api from "../api/apiClient";
import { useUIStore } from "../state/useUIStore";
import PlanModal from "../components/PlanModal";
import StepsModal from "../components/StepsModal";

export default function ActionPlans() {
  const openModal = useUIStore((s) => s.openModal);
  const modal = useUIStore((s) => s.modal);

  const { data, isLoading, error } = useQuery({
    queryKey: ["plans"],
    queryFn: async () => {
      const res = await api.get("/plans");
      return res.data;
    }
  });

  if (isLoading) return <p className="text-center py-20">Loading plans…</p>;
  if (error) return <p className="text-center text-red-600 py-20">{error.message}</p>;

  return (
    <div className="max-w-3xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold mb-6">Action Plans</h1>

      <div className="grid gap-6">
        {data.map((plan) => (
          <div
            key={plan.id}
            className="p-6 bg-white rounded-xl shadow-sm border hover:shadow-md"
          >
            <h2 className="text-xl font-semibold mb-2">{plan.title}</h2>
            <p className="text-gray-700 mb-4">{plan.summary}</p>

            <div className="flex gap-3">
              <button
                onClick={() => openModal({ type: "plan", plan })}
                className="bg-brand text-white px-4 py-2 rounded-lg"
              >
                View Details
              </button>

              <button
                onClick={() => openModal({ type: "steps", plan })}
                className="border border-brand text-brand px-4 py-2 rounded-lg"
              >
                View Steps
              </button>
            </div>
          </div>
        ))}
      </div>

      {modal?.type === "plan" && <PlanModal />}
      {modal?.type === "steps" && <StepsModal />}
    </div>
  );
}
