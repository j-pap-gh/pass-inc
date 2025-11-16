
import React from "react";
import { useMutation } from "@tanstack/react-query";
import api from "../api/apiClient";

export default function Upgrade() {
  const { mutate, isPending, error } = useMutation({
    mutationFn: () => api.post("/subscribe/start-checkout"),
    onSuccess: (res) => {
      window.location.href = res.data.checkout_url;
    }
  });

  return (
    <div className="max-w-xl mx-auto py-20 px-4">
      <h1 className="text-3xl font-bold mb-4 text-center">Upgrade to Premium</h1>

      <p className="text-center text-gray-600 mb-10">
        Unlock all passive income plans, AI guidance, and premium resources.
      </p>

      {error && (
        <p className="text-red-600 text-center mb-4">{error.message}</p>
      )}

      <button
        disabled={isPending}
        onClick={() => mutate()}
        className="w-full bg-brand text-white py-4 rounded-lg text-lg font-medium hover:bg-brand-dark disabled:opacity-50"
      >
        {isPending ? "Redirecting…" : "Upgrade for €9.99 / month"}
      </button>
    </div>
  );
}
