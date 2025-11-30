import Button from "./UI/Button";
import TextBox from "./UI/TextBox";

export default function InputPanel({headline, description, setHeadline,setDescription,onCategorize,onSummarize}) {
  return (
    <div className="card">
      

      <label>News headline</label>
      <input 
        className="textbox" 
        placeholder="Type headline here" 
        value={headline}
        onChange={(e) => setHeadline(e.target.value)}/>

      <label>Short description</label>
      <TextBox 
        rows={4} 
        placeholder="Paste short article text here" 
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        style={{ minHeight: "150px" }}/>

      <div className="button-row">
        {/* <Button onClick={onCategorize}> Categorization </Button> */}

        {/* ToDo; button for summary */}
        {/* <Button>  Summarization </Button>  */}
      </div>

    </div>
  );
}
