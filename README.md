# News-AI-Agent



### 👥 **Team Members**

| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Ashriya Tuladhar   | @t-ashriya | **Data Exploration & Preprocessing:** Conducted detailed dataset analysis, including class balance assessment and visualizations to identify data distribution issues. Built text preprocessing pipelines with tokenization, lemmatization, and cleaning to improve data quality for modeling.<br><br>**Feature Engineering:** Developed semantic text features using Word2Vec embeddings to capture contextual relationships between words to improve classification performance.<br><br> **News Categorization Model Development & Evaluation:** Implemented and evaluated Naive Bayes models for multi-class news categorization across multiple feature representations, including Bag-of-Words, TF-IDF, and Word2Vec-based embeddings. Assessed model performance using accuracy, precision, recall, F1-score, confusion matrices, and compared results to identify the most effective modeling approach.<br><br>**Text Summarization Model Development & Evaluation** Implemented an abstractive summarization pipeline using the google/flan-t5-small transformer model. Evaluated model performance through qualitative analysis and using SacreBLEU for inspection of generated summaries.<br><br>**System Architecture, AI Agent Logic & User-Interface:** Designed and implemented the overall React–Flask application architecture, including backend API routes, frontend component structure, and a modular codebase to support scalable feature development. Owned and implemented the news categorization pipeline, including the best categorization model pickling, and integration with the Flask backend and React frontend. Designed the agent logic to route user requests to the appropriate component (e.g. categorization or summarization models, or the chatbot for general queries). Assisted with integrating the chatbot user interface into the backend agent system and ensured smooth communication between frontend, backend, and machine learning models for user access.<br><br>**Project Coordination & Leadership:** Coordinated the overall project by leading the meetings, brainstorming and assigning tasks, aligning interfaces, and ensuring smooth integration. Led overall project organization and technical direction to support effective team collaboration for the success of the project. |
|  Anya Liu  |  @anya-liu004   |  **Data Exploration & Visualization**: Conducted in-depth exploratory data analysis on the BBC News dataset, creating visualizations to examine class balance, article length distributions, and text characteristics to inform preprocessing and modeling decisions.<br><br>**Feature Engineering & Representation Learning**: Implemented and evaluated multiple text feature representations, including TF-IDF, Word2Vec, Google News pre-trained Word2Vec, and hybrid approaches combining TF-IDF with Google Word2Vec embeddings. Systematically compared feature types to identify the most effective representation for downstream classification tasks.<br><br>**Model Evaluation & Comparison**: Trained a Logistic Regression model and evaluated multiple machine learning models using different feature configurations, comparing performance across accuracy and F1 metrics to select the best-performing feature–model combinations for news categorization.<br><br>**Summarization Model Research & Integration**: Researched and evaluated multiple abstractive summarization models, including OpenLLaMA, BART, and T5. Conducted comparative analysis of summary quality and performance tradeoffs, ultimately selecting a T5-based model for integration into the final AI agent summarization pipeline.<br><br>**Evaluation Framework & Golden Dataset**: Designed and curated a golden evaluation dataset for summarization, enabling structured comparison between model-generated summaries and human-authored reference summaries to support both qualitative review and metric-based evaluation. |
| Sophie Lin  |    @sophieelin |  **Feature Engineering:** Implemented TF-IDF for text feature extraction for text feature extraction, architected the integration of TF-IDF with Word2Vec for improved model effectiveness.<br><br>**Model Development and Evaluation:** Developed a Random Forest model for text classification, including hyperparameter tuning to optimize accuracy and generalization across different article inputs. Evaluated the model using accuracy, precision, recall, and F1-score to assess overall performance and classification reliability. <br><br>**LLM Integration (Chatbot):** Utilized large language models (GPT-4) to build a chatbot for answering questions and generating summaries for article inputs.<br><br>**AI Agent Development:** Designed and implemented the AI agent to integrate our classification and LLM components into a unified system. Developed agent logic for task routing, context management, and model coordination to produce coherent, accurate, and contextually grounded responses. Implemented fallback strategies to handle ambiguous inputs and model failures, ensuring reliable system behavior. Integrated logging and evaluation mechanisms to monitor agent decisions and response quality. <br><br>**Full-Stack Development:** Built backend API routes using Flask to support AI agent and chatbot interactions, and connected these to the frontend messaging interface for seamless user experience. |
| Sonia Broni  |   @bronisonia  | **Data Exploration/Wrangling:** tokenization, stop-word removal, lemmatization, established code for the data processing, and visualization  <br><br>**Feature engineering:** Word2Vec & TF-IDF <br><br>**Model development and evaluation:** Random Forest for categorization and evaluation (hyper-parameter tuning with GridSearch), T5 research for summarization<br><br>**Chatbot:** golden questions set; Final Presentation: development, organization and slide deck coordination <br><br>**Team Strategies:** Cross-check collaboration & assistance in delegation|
| Erwin Coq   |   @SAMGETUB   | **Data Exploration & Preprocessing:** Explored the BBC News dataset to assess structure, quality, and completeness. Verified the absence of missing values to ensure the data was ready for modeling.<br><br>**Feature Engineering & Representation:** Implemented Google News pre-trained Word2Vec (base) embeddings to represent news articles. Built and evaluated a hybrid representation combining Google Word2Vec embeddings with TF-IDF weighting to capture both semantic context and term importance.<br><br>**Model Development & Training:** Contributed to training and evaluating a Logistic Regression model for news categorization. Assisted in analyzing model performance to support feature and model selection.<br><br>**Summarization Model Research & Evaluation:** Researched and evaluated ChatGPT-based abstractive summarization for news articles using the golden dataset. Finalized the golden dataset and performed human evaluation by comparing ChatGPT-generated summaries against reference answers.

| Jerry Liu  | @Jerry13975 | **Feature Engineering:** Implemented Bag of Words (BoW) for text feature extraction to represent news articles for classification. Added visualizations to show word frequency distributions and class-specific patterns to help the team understand the dataset and identify important features.<br><br>**Model Development and Evaluation:** Built and evaluated a Naive Bayes model for news categorization. Adjusted model parameters to optimize performance and created visualizations such as heatmaps to analyze model predictions and overall performance. These analyses helped inform decisions on preprocessing and model selection.<br><br>**Summarization Model Research and Integration:** Contributed a curated set of question and answer samples to enhance the evaluation of the T5 summarization pipeline. These samples allowed structured testing of model outputs and ensured the summarization component produced accurate and user-relevant summaries.|



---

## 🎯 **Project Highlights**
- Built an end-to-end News AI Agent capable of categorizing, summarizing, and answering questions about news articles using a combination of classical ML and large language models.
- Developed and evaluated multiple text representation strategies (TF-IDF, Word2Vec, Google News Word2Vec, and hybrid feature ensembles) to identify the most effective features for news classification.
- Trained and compared several machine learning classifiers (Naive Bayes, Random Forest) and selected best-performing feature–model combinations based on accuracy and F1-score.
- Researched, evaluated, and integrated abstractive summarization models (OpenLLaMA, BART, and T5), ultimately deploying a T5-based summarizer for the final AI agent.
- Designed a golden evaluation dataset for summarization to enable structured qualitative comparison and metric-based evaluation of model outputs.
- Implemented an agentic routing system to intelligently direct user requests to the appropriate pipeline (classification, summarization, or chatbot).
- Delivered a full-stack React + Flask application, enabling real-time interaction with machine learning models through a user-friendly interface.

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

For each of the six feature types, we split the labeled training dataset into training and test sets using an 80-20 stratification to ensure balanced representation across classes.

### Feature Types
- TF-IDF
- Bag-of-Words
- Word2Vec
- TF-IDF + Word2Vec
- Google Word2Vec (pretrained)
- TF-IDF + Google Word2Vec

### Models Used

**Logistic Regression**  
- Features: All six types  
- Hyperparameters: C = 0.1  
- Preprocessing: StandardScaler applied  
- Notes: Regularized model suitable for all feature types  

**Naive Bayes**  
- Features: Bag-of-Words, TF-IDF  
- Hyperparameters: alpha = 0.1, fit_prior = True  
- Notes: Works best with discrete count features rather than embeddings  

**Random Forest**  
- Features: All six types  
- Hyperparameters: n_estimators = 200, max_features = 'sqrt', min_samples_leaf = 3, min_samples_split = 10  
- Notes: Ensemble of trees, handles high-dimensional features effectively  

### Training Setup
- Dataset split: 80% train, 20% test (stratified)  
- Evaluation metrics: Accuracy and F1-score  
- Baseline: Performance of each model compared across all feature types to select the best-performing combinations


---

## 📈 **Results & Key Findings**

**You might consider describing the following (as applicable):**

* Performance metrics (e.g., Accuracy, F1 score, RMSE)
* How your model performed

  


**Potential visualizations to include:**

* Confusion matrix, precision-recall curve, feature importance plot, prediction distribution, outputs from fairness or explainability tools

Agent Workflow

<img width="774" height="399" alt="Screenshot 2025-12-14 at 4 05 27 PM" src="https://github.com/user-attachments/assets/26283fb8-65b3-4b18-b88c-5c9bfab77fc3" />


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


## 🙏 **Acknowledgements** 

Thank your Challenge Advisor - Dr. Francesca Lazzeri, TA - Andrii Zahorodnii, Breakthrough Tech AI mentors - Chu Huang & Maxime Nguyen, the Microsoft and MIT representatives and others who supported your project.
