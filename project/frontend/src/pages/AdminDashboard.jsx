
import React from "react";
import { useQuery, useMutation } from "@tanstack/react-query";
import api from "../api/apiClient";

export default function AdminDashboard() {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ["admin", "ideas"],
    queryFn: async () => {
      const res = await api.get("/admin/ideas");
      return res.data;
    }
  });

  const addIdea = useMutation({
    mutationFn: (payload) => api.post("/admin/ideas", payload),
    onSuccess: () => refetch()
  });

  if (isLoading) return <p className="py-20 text-center">Loading…</p>;
  if (error) return <p className="text-red-600 text-center py-20">{error.message}</p>;

  return (
    <div className="max-w-4xl mx-auto py-12 px-4">
      <h1 className="text-3xl font-bold mb-10">Admin Dashboard</h1>

      <IdeaForm onSubmit={(payload) => addIdea.mutate(payload)} />

      <h2 className="text-xl font-semibold mt-12 mb-4">Existing Ideas</h2>

      <div className="grid gap-4">
        {data.map((idea) => (
          <div key={idea.id} className="p-4 bg-white rounded-lg border shadow-sm">
            <h3 className="font-semibold">{idea.title}</h3>
            <p className="text-gray-700 text-sm">{idea.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function IdeaForm({ onSubmit }) {
  const [title, setTitle] = React.useState("");
  const [description, setDescription] = React.useState("");

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit({ title, description });
        setTitle("");
        setDescription("");
      }}
      className="bg-white p-6 rounded-xl shadow-sm border"
    >
      <h2 className="text-xl font-semibold mb-4">Add New Idea</h2>

      <div className="mb-4">
        <label className="block mb-1 font-medium">Title</label>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full border px-3 py-2 rounded-lg"
        />
      </div>

      <div className="mb-4">
        <label className="block mb-1 font-medium">Description</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full border px-3 py-2 rounded-lg"
        />
      </div>

      <button type="submit" className="bg-brand text-white px-5 py-2 rounded-lg">
        Add
      </button>
    </form>
  );
}
