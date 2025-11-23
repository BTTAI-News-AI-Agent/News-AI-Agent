import InputPanel from "../components/InputPanel";
import OutputPanel from "../components/OutputPanel";
import Chatbot from "../components/Chatbot";

function Home() {
  return (
    <div className="page">
      <header className="header">
        <h1>AI Agent for News</h1>
        <p>Enter a news headline and description, then explore with the agent.</p>
      </header>

      <main className="main-grid">
        <section>
          <InputPanel />
        </section>

        <section>
          <OutputPanel />
        </section>
      </main>

      <section>
        <Chatbot />
      </section>
    </div>
  );
}

export default Home;
