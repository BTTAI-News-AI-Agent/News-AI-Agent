import React, { useState, useRef, useEffect } from "react";
import Button from "./UI/Button";
import TextBox from "./UI/TextBox";

export default function Chatbot({
  messages,
  onSend,
  isLoading,
  headline,
  description,
  setHeadline,
  setDescription,
  onCategorize,
  onSummarize,
}) {
  const [question, setQuestion] = useState("");
  const messagesEndRef = useRef(null);

  // SAFETY CHECK - Debug what we're receiving
  console.log("=== CHATBOT DEBUG ===");
  console.log("messages received:", messages);
  console.log("type:", typeof messages);
  console.log("isArray:", Array.isArray(messages));
  console.log("====================");

  // Auto-scroll to bottom when new messages arrive
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = () => {
    if (!question.trim() || isLoading) return;
    onSend(question);
    setQuestion("");
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  // Safety: ensure messages is always an array
  const safeMessages = Array.isArray(messages) ? messages : [];

  return (
    <div className="card">
      <h2 style={{ textAlign: "center" }}>News-bot •ᴗ•</h2>

      {/* Article context */}
      {(headline || description) && (
        <div className="article-context">
          {headline && (
            <p>
              <strong>Headline:</strong> {headline}
            </p>
          )}
          {description && (
            <p>
              <strong>Description:</strong> {description}
            </p>
          )}
        </div>
      )}

      {/* Chat window with scrollable messages */}
      <div className="chat-window">
        {safeMessages.length > 0 ? (
          safeMessages.map((msg, idx) => (
            <div
              key={idx}
              className={`message ${
                msg.sender === "user" ? "user-message" : "bot-message"
              }`}
            >
              <div className="message-bubble">
                <div className="message-label">
                  {msg.sender === "user" ? "You" : "Bot"}
                </div>
                <div className="message-text">{msg.text}</div>
              </div>
            </div>
          ))
        ) : (
          <div className="message bot-message">
            <div className="message-bubble">
              <div className="message-label">Bot</div>
              <div className="message-text">
                Ask me anything about this article.
              </div>
            </div>
          </div>
        )}

        {/* Loading indicator */}
        {isLoading && (
          <div className="message bot-message">
            <div className="message-bubble">
              <div className="message-label">Bot</div>
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* User question input */}
      <label>Your Question</label>
      <TextBox
        rows={2}
        placeholder="Type your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyPress={handleKeyPress}
        disabled={isLoading}
      />

      {/* Button row */}
      <div className="button-row">
        <Button onClick={handleSend} disabled={isLoading || !question.trim()}>
          {isLoading ? "Sending..." : "Send"}
        </Button>
      </div>
    </div>
  );
}