
import React from "react";
import { Link } from "react-router-dom";

export default function PremiumSuccess() {
  return (
    <div className="max-w-xl mx-auto py-20 px-4 text-center">
      <h1 className="text-3xl font-bold mb-4">🎉 You're Premium!</h1>

      <p className="text-gray-700 mb-8">
        Your subscription is active. Enjoy full access to the platform!
      </p>

      <Link
        to="/"
        className="inline-block bg-brand text-white px-6 py-3 rounded-lg"
      >
        Start exploring
      </Link>
    </div>
  );
}
