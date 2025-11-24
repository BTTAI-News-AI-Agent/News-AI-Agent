export default function OutputPanel({category, summary, isLoadingCategory, isLoadingSummary, error}) {
  return (
    <div className="card">
      <h2>Output</h2>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <h3>Predicted Category</h3>
      <div className="output-box">
        {isLoadingCategory ? "Running model..." : category}
      </div>

{/* ToDo: summary output */}
      <h3>Summary</h3>
     
    </div>
  );
}
