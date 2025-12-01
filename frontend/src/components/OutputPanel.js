import Button from "./UI/Button";

export default function OutputPanel({category, summary, isLoadingCategory, isLoadingSummary, onCLearOutput, error}) {
  return (
    <div className="card">
      

      {error && <p style={{ color: "red" }}>{error}</p>}

      <h3>Predicted Category</h3>
      <div className="output-box">
        {isLoadingCategory ? "Running model..." : category}
      </div>

{/* ToDo: summary output */}
      <h3>Summary</h3>
      <div className="output-box">
        {isLoadingSummary ? "Running model..." : summary}
      </div>

      <div className="button-row">
        <Button onClick={onCLearOutput}>Clear</Button>
      </div>
     
    </div>
  );
}
