import React, { useState } from "react";

import InputPanel from "../components/InputPanel";
import OutputPanel from "../components/OutputPanel";
import Chatbot from "../components/Chatbot";

import { categorizeNews } from "../api/categorize";
import { summarizeNews } from "../api/summarize";

export default function Home() {
  // article text
  const [headline, setHeadline] = useState("");
  const [description, setDescription] = useState("");

  // model outputs
  const [category, setCategory] = useState("");
  const [summary, setSummary] = useState("");

  // chatbot prompt text
  const [chatmessages, setChatMessages] = useState("");

  // loading and error
  const [isLoadingCategory, setIsLoadingCategory] = useState(false);
  const [isLoadingSummary, setIsLoadingSummary] = useState(false);
  const [isChatLoading, setIsChatLoading] = useState(false);
  const [error, setError] = useState(null);

  // handler for Categorization button
  async function handleCategorize() {
    try {
      setIsLoadingCategory(true);
      setError(null);
      const result = await categorizeNews(headline, description);
      setCategory(result.category);
    } catch (e) {
      console.error(e);
      setError("Failed to categorize article.");
    } finally {
      setIsLoadingCategory(false);
    }
  }

  // handler for Summarization button
  async function handleSummarize() {
    
  }

  // handler for Chatbot 
  async function handleSendChat(){

  }

  return (
    <div className="page">
      <header className="header">
        <h1>AI Agent for News</h1>
        <p>Enter a news headline and description, then explore with the agent.</p>
      </header>

      <main className="main-grid">
        <section className = "input-card">
          <InputPanel 
            headline={headline}
            description={description}
            setHeadline={setHeadline}
            setDescription={setDescription}
          />
        </section>

        <section>
          <OutputPanel 
            category={category}
            summary={summary}
            isLoadingCategory={isLoadingCategory}
            isLoadingSummary={isLoadingSummary}
            error={error}/>
        </section>
      </main>

      <section>
        <Chatbot 
          messages={chatmessages}
          onSend={handleSendChat}
          isLoading={isChatLoading}
          headline={headline}
          description={description}
          onCategorize={handleCategorize}
          onSummarize={handleSummarize}/>
      </section>
    </div>
  );
}


