import Button from "./UI/Button";

export default function Chatbot({messages, onSend, isLoading, headline, description, setHeadline,setDescription, onCategorize,onSummarize}) {
  return (
    <div className="card">
      <h2>News-bot</h2>

      <div className="chat-window">
        {/* ToDo: render real messages here */}
        <div className="chat-message bot">
          Bot: Ask me anything about this article.
        </div>
      </div>

 {/* categorization and summarization buttons */}
      <div className="button-row">
              <Button onClick={onCategorize}> Categorization </Button>
      
              {/* ToDo; button for summary */}
              <Button>  Summarization </Button> 
            </div>



      <div className="chat-input-row">
        <input
          className="textbox"
          placeholder="Type your question..."
        />
        <Button>Send</Button>
      </div>
    </div>
  );
}