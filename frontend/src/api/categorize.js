export async function categorizeNews(headline, description) {
  const res = await fetch("http://localhost:5001/api/categorize", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ headline, description }),
  });

  if (!res.ok) {
    throw new Error("Categorization API error");
  }

  return res.json(); 
}
