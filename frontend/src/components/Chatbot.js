import Button from "./UI/Button";

export default function Chatbot() {
  return (
    <div className="card">
      <h2>Chatbot</h2>

      <div className="chat-window">
        {/* ToDo: render real messages here */}
        <div className="chat-message bot">
          Bot: Ask me anything about this article.
        </div>
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