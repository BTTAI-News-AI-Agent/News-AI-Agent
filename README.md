# News-AI-Agent



### 👥 **Team Members**

| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Ashriya Tuladhar   | @t-ashriya | **Data Exploration & Preprocessing:** Conducted detailed dataset analysis, including class balance assessment and visualizations to identify data distribution issues. Built text preprocessing pipelines with tokenization, lemmatization, and cleaning to improve data quality for modeling.<br><br>**Feature Engineering:** Developed semantic text features using Word2Vec embeddings to capture contextual relationships between words to improve classification performance.<br><br> **Model Development and Evaluation:** Implemented and evaluated Naive Bayes models for news categorization. Researched and integrated T5-based transformer models for abstractive text summarization, and evaluated the performance for both models.<br><br>**System Architecture & Full-Stack Development:** Designed and implemented the overall React–Flask application structure, including backend API routes and frontend component layout. Created the project’s initial codebase and skeleton structure to support modular development across core features.<br><br>**Agentic System & User Interface Design:** Defined the core user-facing features - categorization, summarization, and chatbot, and distributed feature ownership across the team. Owned and implemented the news categorization pipeline, including the best categorization model pickling, and integration with the Flask backend and React frontend. Designed the agent logic to route user requests to the appropriate component (e.g. categorization or summarization models, or the chatbot for general queries). Assisted with integrating the chatbot into the backend agent system and ensured smooth communication between frontend, backend, and machine learning models for user access.<br><br>**Project Coordination & Leadership:** Coordinated the overall project by leading the meetings, brainstorming and assigning tasks, aligning interfaces, and ensuring smooth integration. Led overall project organization and technical direction to support effective team collaboration for the success of the project. |
|  Anya Liu  |  @anya-liu004   |  |
| Sophie Lin  |    @sophieelin |  **Feature Engineering:** Implemented TF-IDF for text feature extraction for text feature extraction, architected the integration of TF-IDF with Word2Vec for improved model effectiveness.<br><br>**Model Development and Evaluation:** Developed a Random Forest model for text classification, including hyperparameter tuning to optimize accuracy and generalization across different article inputs.<br><br>**LLM Integration (Chatbot):** Utilized large language models (GPT-4) to build a chatbot for answering questions and generating summaries for article inputs.<br><br>**AI Agent Development:** Designed and implemented the AI agent to integrate our classification and LLM components into a unified system. Developed agent logic for task routing, context management, and model coordination to produce coherent, accurate, and contextually grounded responses.<br><br>**Full-Stack Development:** Built backend API routes using Flask to support AI agent and chatbot interactions, and connected these to the frontend messaging interface for seamless user experience. |
| Sonia Broni  |   @bronisonia  | Data Exploration/Wrangling: tokenization, stop-word removal, lemmatization, established code for the data processing, and visualization ; Feature engineering: Word2Vec & TF-IDF ; Model development and evaluation: Random Forest for categorization and evaluation (hyper-parameter tuning with GridSearch), T5 research for summarization; Chatbot: golden questions set; Final Presentation: development, organization and slide deck coordination ; Team Strategies: Cross-check collaboration & assistance in delegation|
| Erwin Coq   |   @SAMGETUB   |  |
| Jerry Liu  |   @Jerry13975  |  |

---

## 🎯 **Project Highlights**

**Example:**

- Developed a machine learning model using `[model type/technique]` to address `[challenge project task]`.
- Achieved `[key metric or result]`, demonstrating `[value or impact]` for `[host company]`.
- Generated actionable insights to inform business decisions at `[host company or stakeholders]`.
- Implemented `[specific methodology]` to address industry constraints or expectations.

---

## 👩🏽‍💻 **Setup and Installation**


### 1) Clone the repository
```bash
git clone https://github.com/BTTAI-News-AI-Agent/News-AI-Agent.git
cd News-AI-Agent
```
### 2) Backend setup (Flask)
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3) Set environment variables (for GPT model features)
If you are using GPT for summarization or the chatbot, set your OpenAI API key:

**Mac/Linux**
```bash
export OPENAI_API_KEY="YOUR_KEY_HERE"
```
**Windows (PowerShell)**
```bash
setx OPENAI_API_KEY "YOUR_KEY_HERE"
```
Restart your terminal after running setx.

### 4) Run the backend server
```bash
python app.py
```
Backend runs at:
```bash
 http://localhost:5001
```

### 5) Frontend setup (React)
Open a new terminal:
```bash
cd frontend
npm install
npm start
```
Frontend runs at:
```bash
 http://localhost:3000
```

### 6) Accessing the dataset (for training / notebooks)
```bash
The BBC News dataset used in this project is publicly available on Kaggle:
https://www.kaggle.com/c/learn-ai-bbc/overview
```

After downloading, place the data files in a local data/ directory before running the notebooks located in the notebooks/ folder.





---

## 🏗️ **Project Overview**

**Describe:**

This project is connected to the Break Through Tech AI Program because during our Machine Learning Foundations training, we learned and worked through the entire CRISP-DM framework with mini assignments and projects. With this foundation, we brought the real-world framework to life with our News AI Agent project. We persevered from solidfying business understanding as a team, to grappling with the process of deployment that demanded new skills and efficient time management, skills that we also matured in during our ML Foundations course, and our AI Studio professional development course. We truly captured a glimpse of what it is like to be immersed in the world of data scienced/ML, developing a product for every-day users admist the overlooked challenges of deep research, team coordination, and effectual, detailed, documentation.

Our host company was Microsoft. The project objective and scope was to build machine learning models in order to categorize news content. Following, we evaluated different LLMs in order to identify the most effective models for news categorization and summarization tasks. We also used prompt engineering to optimize model responses and improve classification accuracy. Using a public dataset from BBC with 2225 articles, we aimed to build a system that could accurately classify previously unseen news articles into their right categories. Categories included business, entertainment, politics, sport, or technology. 

The real-world significance of the problem and the potential impact of your work is that in today’s world of information, we are bombarded with hundreds of news stories, yet still don’t have a complete picture of what’s really going on. This News AI Agent aims to solve exactly that. It categorizes news articles by topic, summarizes them, and even answers users’ questions through an intelligent chatbot. The business impact includes: 
-   Automated news recommendation to personalize the news according to user’s interests.
-   Identify topics of untracked news which helps clients save time and reduce unwanted information.
-   Increase user engagement through AI summaries and interactive Q&A.
-   Enable scalable news delivery - classification and summarization reduce manual effort for content management.

## 📊 **Data Exploration**

* Dataset overview: Used the BBC News dataset (Kaggle) containing 2,225 labeled news articles across five categories (business, entertainment, politics, sport, tech), split into 1,490 training and 735 testing samples.

<p align="center">
  <img src="imgs/check_balance.png" width="600">
</p>


* Exploratory analysis: Examined class distribution, article length, and word frequency patterns; categories were relatively balanced, and article lengths followed a right-skewed distribution.

* Data cleaning: Applied text normalization, including lowercasing, tokenization, stop-word removal, punctuation handling, and lemmatization; removed duplicates and extreme length outliers to improve data quality.
<p align="center">
  <img src="imgs/remove_outliers.png" width="500">
</p>


* Feature engineering: Transformed text using individual and ensembling of Bag-of-Words, TF-IDF, and Word2Vec embeddings to generate multiple numerical representations for downstream modeling.





---

## 🧠 **Model Development**

**You might consider describing the following (as applicable):**

* Model(s) used (e.g., CNN with transfer learning, regression models)
* Feature selection and Hyperparameter tuning strategies
* Training setup (e.g., % of data for training/validation, evaluation metric, baseline performance)


---

## 📈 **Results & Key Findings**

**You might consider describing the following (as applicable):**

* Performance metrics (e.g., Accuracy, F1 score, RMSE)
* How your model performed

  


**Potential visualizations to include:**

* Confusion matrix, precision-recall curve, feature importance plot, prediction distribution, outputs from fairness or explainability tools

---

## 🚀 **Next Steps**

* AI Agent Guard Rails

Improve the AI agent by adding stronger guard rails and safety checks to ensure more reliable, controlled, and trustworthy outputs.

* Performance Optimization
  
Optimize system performance to achieve lower latency, improving responsiveness and overall user experience.

* Model Deployment

Deploy the classification model behind a clean, production-ready API endpoint that supports scalability, versioning, and future enhancements.

* Retrieval-Augmented Generation (RAG)

Introduce RAG to reduce hallucinations and improve response accuracy by grounding LLM outputs in the source article. This approach may impact response speed due to chunking and retrieval, so performance optimizations should be explored.

* User Interface

Improve the user interface to be more intuitive, easier to use, and visually appealing. Enable users to interact directly with an online model without needing to copy and paste articles manually.

* Containerization

Containerize the application using Docker to ensure consistency across development, testing, and production environments, simplifying deployment and maintenance.

---

## 📝 **License**

This project is licensed under the MIT License.


## 🙏 **Acknowledgements** (Optional but encouraged)

Thank your Challenge Advisor - Dr. Francesca Lazzeri, TA - Andrii Zahorodnii, Breakthrough Tech AI mentors - Chu Huang & Maxime Nguyen, the Microsoft and MIT representatives and others who supported your project.
