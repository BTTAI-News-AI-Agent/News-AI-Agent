export async function sendChat(messages) {
  const res = await fetch("http://localhost:5001/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ messages }),
  });

  if (!res.ok) {
    throw new Error("Chat API error");
  }

  return res.json(); 
}
