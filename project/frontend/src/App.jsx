
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useAuthStore } from "./state/useAuthStore";

import Upgrade from "./pages/Upgrade";
import PremiumSuccess from "./pages/PremiumSuccess";
import ActionPlans from "./pages/ActionPlans";
import AdminDashboard from "./pages/AdminDashboard";

export default function App() {
  const { refreshUser } = useAuthStore();

  React.useEffect(() => {
    refreshUser();
  }, [refreshUser]);

  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-100">
        <Routes>
          <Route path="/" element={<ActionPlans />} />
          <Route path="/upgrade" element={<Upgrade />} />
          <Route path="/premium-success" element={<PremiumSuccess />} />
          <Route path="/admin" element={<AdminDashboard />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
