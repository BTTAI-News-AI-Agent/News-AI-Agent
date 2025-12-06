import React, { useState } from "react";
import Button from "./UI/Button";
import TextBox from "./UI/TextBox";

export default function Chatbot({headline, description, messages, onSend, isLoading,}) {
  
  const [question, setQuestion] = useState("");

  const BotMessage =
    Array.isArray(messages) && messages.length > 0
      ? messages[messages.length - 1].text
      : "Ask me anything about this article.";

  function handleSend() {
    if (!question.trim() || isLoading) return;
    onSend(question);
    setQuestion(""); // clear user input
  }

  return (
    <div className="card">
      <h2>News-bot</h2>

      {/* Bot reply */}
      <div className="chat-window">
        <div className="message bot-message">
          <strong>Bot:</strong> {BotMessage}
        </div>

        {isLoading && (
          <div className="message bot-message">
            <strong>Bot:</strong> Thinking...
          </div>
        )}
      </div>

      {/* User question */}
      <label>Your Question</label>
      <TextBox
        rows={2}
        placeholder="Type your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        disabled={isLoading}
      />

      <div className="button-row">
        <Button onClick={handleSend} disabled={isLoading || !question.trim()}>
          {isLoading ? "Sending..." : "Send"}
        </Button>
      </div>
    </div>
  );
}
