# News-AI-Agent



### 👥 **Team Members**

| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Ashriya Tuladhar   | @t-ashriya | Data exploration: class balance analysis and visualization, text normalization and lemmatization;Feature engineering: word embedding features (Word2Vec); Model development and evaluation: Naive Bayes for categorization, T5-based summarization; System architecture & development: designed and implemented the complete React–Flask application framework, created backend API routes and frontend component structure; established skeleton code and distributed development tasks across three core features - categorization, summarization, and chatbot; overall project coordination |
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

**Provide step-by-step instructions so someone else can run your code and reproduce your results. Depending on your setup, include:**

* How to clone the repository
* How to install dependencies
* How to set up the environment
* How to access the dataset(s)
* How to run the notebook or scripts

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
