export async function sendChat(headline, description, question) {
  const res = await fetch("http://localhost:5001/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ headline, description, question }),
  });

  if (!res.ok) {
    throw new Error("Chat API error");
  }

  const data = await res.json();

  if (data.error) {
    throw new Error(data.error);
  }

  // Backend returns answer
  return data.answer;
}
