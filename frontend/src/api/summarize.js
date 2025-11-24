export async function summarizeNews(headline, description) {
  const res = await fetch("http://localhost:5000/api/summarize", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ headline, description }),
  });

  if (!res.ok) {
    throw new Error("Summarization API error");
  }

  return res.json(); 
}
