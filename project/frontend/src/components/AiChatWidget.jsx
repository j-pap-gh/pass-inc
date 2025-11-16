
import React, { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import api from "../api/apiClient";

export default function AiChatWidget() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [open, setOpen] = useState(false);

  const chatMutation = useMutation({
    mutationFn: async (payload) => {
      const res = await api.post("/ai/chat", payload);
      return res.data;
    },
    onSuccess: (res) => {
      setMessages((prev) => [...prev, { role: "assistant", text: res.reply }]);
    }
  });

  const sendMsg = () => {
    if (!input.trim()) return;
    const msg = { role: "user", text: input.trim() };
    setMessages((prev) => [...prev, msg]);
    chatMutation.mutate({ message: input.trim() });
    setInput("");
  };

  return (
    <>
      <button
        onClick={() => setOpen(!open)}
        className="fixed bottom-6 right-6 bg-brand text-white p-4 rounded-full shadow-lg"
      >
        💬
      </button>

      {open && (
        <div className="fixed bottom-20 right-6 w-80 bg-white rounded-xl shadow-xl border p-4 max-h-[450px] flex flex-col">
          <div className="flex-1 overflow-y-auto space-y-3 mb-3 pr-1">
            {messages.map((m, i) => (
              <div
                key={i}
                className={`p-2 rounded-lg text-sm ${
                  m.role === "user"
                    ? "bg-brand text-white self-end"
                    : "bg-gray-100"
                }`}
              >
                {m.text}
              </div>
            ))}
          </div>

          <div className="flex gap-2">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMsg()}
              className="flex-1 border px-3 py-2 rounded-lg"
              placeholder="Ask something…"
            />
            <button
              onClick={sendMsg}
              className="bg-brand text-white px-3 py-2 rounded-lg"
            >
              Send
            </button>
          </div>
        </div>
      )}
    </>
  );
}
