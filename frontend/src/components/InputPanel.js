import Button from "./UI/Button";
import TextBox from "./UI/TextBox";

export default function InputPanel() {
  return (
    <div className="card">
      <h2>Input</h2>

      <label>News headline</label>
      <input className="textbox" placeholder="Type headline here" />

      <label>Short description</label>
      <TextBox rows={4} placeholder="Paste short article text here" />

      <div className="button-row">
        <Button> Categorization </Button>
        <Button> Summarization </Button>
      </div>

      {/* ToDo: add handlers state + */}
    </div>
  );
}
