# Hi 👋, I'm Ashwin

<p align="left">
  <img src="https://raw.githubusercontent.com/brnhaze/Portfolio/main/portfolio_image.jpg" alt="Ashwin Profile Picture" width="120" style="border-radius: 10px; margin-right: 20px;" align="left">
</p>

<h3>Ashwin</h3>
<p><strong>Data Science | Machine Learning | Analytics | Engineering</strong></p>
<p>🇨🇦 Canada &nbsp; | &nbsp; 💼 Open to Work</p>
<p>
  <a href="mailto:ashwinpraneelpal@hotmail.com">✉️ Email</a> |
  <a href="https://www.linkedin.com/in/ashwinpal17/">🔗 LinkedIn</a> |
  <a href="https://github.com/brnhaze/Portfolio/blob/main/README.md">💻 GitHub</a> |
  <a href="https://www.mygreatlearning.com/eportfolio/ashwin-pal" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MIT_logo.svg/2560px-MIT_logo.svg.png"
       alt="MIT"
       height="16"
       style="vertical-align: text-bottom;">
  MIT Portfolio
</a>
</p>
<br clear="left"/>

**Passionate about Data Engineering, Science, Analytics, & Machine Learning; building scalable data solutions.**

Welcome to my GitHub Portfolio—a collection of end-to-end data science and engineering projects, each showcasing my skills in data wrangling, ETL pipelines, big data processing, machine learning, deep learning, and real-time data streaming. I apply tools such as Python, SQL, Spark, Airflow, Docker, and Kafka, along with visualization platforms like Power BI, Tableau, and D3.js, to analyze and present insights through interactive dashboards. My work also includes API-driven applications, CI/CD implementations, and hands-on projects published here to demonstrate practical, production-ready solutions.

---

## 📚 Table of Contents

• [Projects](#-featured-projects)   • [Skills & Tools](#-skills--tools)   • [Work Experience](#-work-experience)   • [Education](#-education)   • [Contact](#-lets-connect)

---

## 🚀 Featured Projects

### [🚍 Building a Real-Time Transit Data Pipeline (MBTA Route 1)](https://github.com/ashwinpal17/Portfolio/tree/main/Project-16.1-MBTA)
This project implements a production-style **data engineering pipeline** that ingests live bus data from the MBTA Route 1 API and moves it through a multi-container architecture using Docker, MySQL, Debezium CDC, MongoDB, Flask, and Jupyter Notebook.

- Ingest  
  - Calls the official MBTA V3 API every 10 seconds to pull live vehicle data for Route 1.  
  - Parses nested JSON to extract vehicle ID, latitude/longitude, speed, direction, occupancy, trip ID, and current stop sequence.  
  - Handles missing fields and API variability to keep the pipeline robust.

- Store & Model  
  - Stores raw and enriched records in a **MySQL** database running inside a Docker container.  
  - Designed and implemented a relational schema (`mbta_buses` table) to support historical analysis by trip, route, and time.  
  - Ensured proper indexing on time and trip fields to support downstream queries.

- Change Data Capture (CDC)  
  - Configured **Debezium** (Java + Maven + Spring Boot) to read MySQL binlogs and capture row-level changes in real time.  
  - Streamed change events into **MongoDB** as documents, creating an append-only event store for downstream consumers.  
  - Implemented a custom listener to transform Debezium events and write them into a dedicated CDC collection.

- Analyze & Visualize  
  - Built a **Flask** web server to display near real-time bus locations on a Mapbox/OpenStreetMap view.  
  - Used a **Jupyter Notebook** to compute:  
    - Average time for a bus to complete Route 1.  
    - Estimated speed from first to last stop using the Haversine formula.  
    - Visualizations of stop sequence progression and route coverage over time.  

Outcome:  
  - This project showcases a full **end-to-end data pipeline**—from live API ingestion to CDC and analytics—demonstrating skills in containerized data engineering, streaming architectures, and geospatial analysis using real-world transit data.

### [📊 Building an ETL Pipeline for Canadian Retail Sales (MRTS)](https://github.com/brnhaze/Portfolio/blob/main/ETL_MRTS/Module%208_Final_Project_Template.html)
This project develops a full **ETL pipeline** using the *Monthly Retail Trade Survey (MRTS)* dataset from Statistics Canada to study long-term consumer spending patterns.  

- Extract 
  - Pulled raw data from multi-year Excel worksheets (1992–2021).  
  - Parsed NAICS codes, business categories, and monthly sales values.  
  - Generated both adjusted and non-adjusted versions to preserve seasonal insights.  

- Transform
  - Standardized dates into `YYYY-MM` format.  
  - Cleaned and harmonized “Kind of Business” entries.  
  - Removed nulls, duplicates, and aggregated overlapping rows.  
  - Reshaped into a long-format table (`Kind of Business`, `YYYY_MM`, `Total_Sales`).  
  - Added derived metrics like month-over-month and year-over-year changes.  

- Load  
  - Exported the transformed dataset (~23,000+ records across 68 business categories) to CSV.  
  - Built Python installation scripts (`install_mrts_mysql.py`, `install_mrts_simple.py`) to create a MySQL database, define schema, and bulk-insert rows.  
  - Validated row counts and distinct categories in **MySQL Workbench**.  

  Outcome: 
  The ETL pipeline successfully converted raw survey data into a structured, queryable format. This enabled trend analysis, seasonal exploration, and forecasting of Canadian retail sales. Key insights include steady long-run growth, seasonal peaks during holidays, and sharp declines during economic shocks (2008, 2020).  

### [📊 IBM HR Attrition Prediction](https://github.com/brnhaze/Portfolio/blob/main/Employee%20Attrition/Employee%20Attrition%20Prediction.html)
This project explores employee attrition using the IBM HR dataset, with the goal of predicting which employees are most likely to leave. The analysis begins with a comprehensive exploratory data analysis (EDA) to understand key patterns related to job roles, compensation, work-life balance, and overtime. These insights helped shape the modeling strategies and feature engineering decisions.

Multiple classification models were developed, including Logistic Regression, Linear Discriminant Analysis (LDA), K-Nearest Neighbors (KNN), Quadratic Discriminant Analysis (QDA), Random Forest (with class weighting and hyperparameter tuning), and boosting algorithms such as AdaBoost, Gradient Boosting, and XGBoost. Each model was evaluated using accuracy, precision, recall, and F1-score, with a particular focus on recall for the attrition class (label = 1), since it is more critical to identify at-risk employees.

Threshold tuning was applied to Logistic Regression and LDA models to improve sensitivity, and GridSearchCV was used to optimize decision tree and random forest hyperparameters. Feature importance was evaluated using SHAP values, with key predictors identified as OverTime, MonthlyIncome, JobRole, and WorkLifeBalance. These findings align with HR business intuition and can inform strategic retention programs.

The project was built using Python in Jupyter Notebook, and leverages libraries such as scikit-learn, pandas, numpy, matplotlib, seaborn, and SHAP. All results are summarized in a business-facing report available below.
- [Report (pdf)](https://github.com/brnhaze/Portfolio/blob/main/Employee%20Attrition/Report%20pdf.pdf)
- [Report(docx)](https://github.com/brnhaze/Portfolio/blob/main/Employee%20Attrition/Report%20docx.pdf)

### [📊 IBM HR Attrition Prediction](https://github.com/brnhaze/Portfolio/blob/main/Employee%20Attrition/IBM%20HR%20Employee%20Attrition.html)
This project analyzes employee attrition using the IBM HR dataset and implements a range of classification models to predict which employees are most likely to leave the company. The analysis begins with thorough exploratory data analysis (EDA) to uncover key trends and relationships between features and attrition outcomes. Models such as Logistic Regression, Linear Discriminant Analysis (LDA), K-Nearest Neighbors (KNN), and Quadratic Discriminant Analysis (QDA) were trained and evaluated.

Feature importance was explored using SHAP to gain model-agnostic interpretability and explainability. Special focus was given to threshold optimization techniques to improve recall for the minority class (employees who left), which is critical for actionable HR interventions. Logistic Regression with a tuned threshold of 0.35 emerged as the most balanced and production-ready model, while LDA showed comparable performance after threshold adjustment. KNN and QDA were found to overfit to the minority class without class-balancing methods.

This project was developed using Python in a Jupyter Notebook environment. It leverages pandas, numpy, matplotlib, and seaborn for data analysis and visualization. scikit-learn was used extensively for modeling, evaluation metrics, and hyperparameter tuning through GridSearchCV. SHAP was applied for detailed model interpretation, particularly to visualize how features like OverTime, JobRole, and MaritalStatus impact attrition risk. The final notebook provides a clear, business-friendly summary with actionable insights and model recommendations.
- [Report](https://github.com/brnhaze/Portfolio/blob/main/Employee%20Attrition/IBM_HR_Attrition_Report.docx)


### [📈 Network Stock Portfolio Optimization](https://github.com/brnhaze/Portfolio/blob/main/Stocks/Network_Stock_Portfolio_Optimization_2.html)
This project simulates and compares investment strategies using S&P 500 stock data and network-based clustering. It involves downloading historical price data with the `yfinance` API, isolating 'Close' prices from multi-index DataFrames, and cleaning the dataset for analysis. The simulation evaluates portfolio growth for different initial investments and compares the performance of central and peripheral portfolios against the S&P 500 benchmark, with results visualized using matplotlib.
- [Network Portfolio Optimization Report](https://github.com/brnhaze/Portfolio/blob/main/Stocks/Network_Portfolio_Optimization_Report.pdf)

### [📚 Deep Learning Text Classification with Transformers](https://github.com/brnhaze/Portfolio/blob/main/Text%20Classification/Deep%20Learning%20Text%20Classification%20with%20Transformers%204.html)
Applies Transformer-based models (like BERT) to classify text data into multiple categories. Preprocesses text, encodes labels, and handles class imbalance. Uses TensorFlow/Keras and Hugging Face Transformers to fine-tune pre-trained models. Evaluates model performance using training, validation, and test metrics with confusion matrices and classification reports.

### [🩺 Diabetes Prediction (Deep Learning)](https://github.com/brnhaze/Portfolio/blob/main/Diabetes/Predicting%20Chance%20of%20Diabetes%20Deep%20Learning%20Regression.html)
Builds multiple deep learning models to classify diabetes risk using clinical data. Compares model architectures and evaluates performance using training/validation/test metrics. Applies TensorFlow and Keras with preprocessing and EDA done using Pandas, NumPy, and Seaborn.

### 🩺 Liver Disease Image Classification (Deep Learning)
Built two progressive deep learning pipelines to classify liver disease tissue images using histopathology data.
- [**Notebook 1:**](https://github.com/brnhaze/Portfolio/blob/main/Liver%20Disease/Liver%20Disease%20Deep%20learning%20image%20Classification%201.html) Developed a custom CNN model trained on 128×128 resized liver images. Served as a baseline using fundamental convolutional layers for binary classification. Focused on building a functional pipeline from scratch using raw image data. Implemented using TensorFlow, Keras, and Matplotlib for training, visualization, and evaluation.
- [**Notebook 2:**](https://github.com/brnhaze/Portfolio/blob/main/Liver%20Disease/Liver%20Disease%20Deep%20learning%20image%20Classification%202.html) Rebuilt and improved the project using transfer learning (VGG16), upgraded input size (224×224), and added multiple deep learning models. This version addressed memory issues from the first notebook, added better evaluation with confusion matrices and accuracy/loss comparisons, and delivered stronger performance. Utilized TensorFlow, Keras, Scikit-learn, and VGG16 from `keras.applications` for enhanced modeling and analysis.

### [🩺 Liver Disease Prediction (Deep Learning)](https://github.com/brnhaze/Portfolio/blob/main/Liver%20Disease/Predicting_Liver_Disease_Using_Machine_Learning_A_Data_Driven_Approach_in_Binary_Classification.html)
Uses neural networks and ensemble models to predict liver disease. Applied TensorFlow, Keras, XGBoost, and LightGBM, with preprocessing and EDA done using Pandas, NumPy, and Seaborn.

### 🐉 Dragon Ball Z: Data Science Saga⚡
Explore the universe of Dragon Ball Z through the lens of data analytics and machine learning. This series of notebooks walks through the full data science pipeline—starting with EDA and moving through clustering, regression, classification, and model evaluation—all themed with your favorite DBZ characters and features.
- [**Notebook 1 Exploratory Data Analysis (EDA):**](https://github.com/brnhaze/Portfolio/blob/main/DragonBall/1%20EDA.html) In this notebook, we explore the raw Dragon Ball Z dataset, clean missing values, visualize relationships between characters and their attributes, and discover patterns in power levels, transformations, and classes. It sets the stage for future modeling work.
- [**Notebook 2: Unsupervised Learning:**](https://github.com/brnhaze/Portfolio/blob/main/DragonBall/2%20Unsupervised%20Learning.html) We use K-Means clustering and PCA to uncover natural groupings among DBZ characters without using predefined labels. This allows us to see which fighters cluster together based on their stats—Saiyans vs villains, elite warriors vs newcomers.
- [**Notebook 3: Supervised Learning – Linear Regression:**](https://github.com/brnhaze/Portfolio/blob/main/DragonBall/3%20Supervised%20Learning%20Regression.html) This notebook trains linear regression models to predict power levels based on other character attributes like attack, defense, and energy. We evaluate model fit, visualize predictions, and assess residuals for improvements.
- [**Notebook 4: Regularized Regression – Lasso & Ridge:**](https://github.com/brnhaze/Portfolio/blob/main/DragonBall/4%20Supervised%20Learning%20Regression%20Lasso_Ridge.html) We apply Lasso and Ridge regression to the same predictive task from Notebook 3, now incorporating regularization to reduce overfitting and improve generalization. Hyperparameter tuning is included to optimize performance.
- [**Notebook 5: Supervised Learning – Classification:**](https://github.com/brnhaze/Portfolio/blob/main/DragonBall/5%20Supervised%20Learning%20Classification.html) This project tackles classification of characters into different fighter categories using models like logistic regression and K-Nearest Neighbors (KNN). Evaluation includes confusion matrices and accuracy scores to find the top performers.
- [**Notebook 6: Advanced Regression – Continuous Targets:**](https://github.com/brnhaze/Portfolio/blob/main/DragonBall/6%20Supervised%20Learning%20Regression%20Continuous.html) We dive deeper into regression tasks involving continuous variables beyond just power level—possibly attack range, speed score, or fusion strength. Multiple regression techniques are compared for best results.
- [**Notebook 7: Classification with Decision Trees & Ensemble Methods:**](https://github.com/brnhaze/Portfolio/blob/main/DragonBall/7%20Supervised%20Learning%20Classification%20with%20Decision%20Trees%20etc.html) We implement decision trees, random forests, and gradient boosting to classify characters based on their DBZ profile. Feature importance helps us understand which traits make a Z-Fighter legendary.
  
### [🎵 Music Genre Classification](https://github.com/brnhaze/Portfolio/blob/main/Music%20Genre/Music%20Genre%20Classification%20using%20Deep%20Learning.html)
Compares ANN and CNN models using MFCC audio features to classify music genres.

### [🎧 Music Recommendation System](https://github.com/brnhaze/Portfolio/blob/main/Recommended%20Systems/Music/Music_Recommendation_System.html)
Collaborative + content-based hybrid recommender system to suggest personalized songs.

### [🛍️ Amazon Product Recommendation System](https://github.com/brnhaze/Portfolio/blob/main/Recommended%20Systems/Amazon%20Products/Amazon%20Products%20RecommendationSystem.html)
Builds an intelligent system that mimics Amazon’s recommendation logic.

### [🌍 Country Cost of Living & Ranking Prediction](https://github.com/brnhaze/Portfolio/blob/main/Cost%20of%20Living/DS_SupervisedLearning_Regression_Decision_etc_Cost_of_Living_Comparison.html)
XGBoost regression project predicting global rankings based on economic factors.

### [🚗 Car Price Prediction](https://github.com/brnhaze/Portfolio/blob/main/Car%20Price%20Prediction/1%20Project%20Plan.ipynb)
Predicts MSRP using regression and feature engineering on automotive datasets.

### [📰 News API + NLP](https://github.com/brnhaze/Portfolio/tree/main/News%20API)
Real-time data scraping and sentiment analysis using News API and NLP.

### [🎮 IGN Video Game Ratings](https://public.tableau.com/app/profile/ashwin.pal3698/viz/IGNVideoGameRatings/Dashboard1)
Data cleaning, SQL, and interactive [Tableau](https://public.tableau.com/views/IGNVideoGameRatings/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) / [Power BI](https://github.com/brnhaze/Portfolio/blob/main/IGN%20VIdeo%20Game%20Rarings/powerBI/file.pdf) dashboards for game reviews.

### [📺 Disney Movies QA](https://github.com/brnhaze/Portfolio/tree/main/Disney_Movies/Cleaned)
Focus on QA processes using Python, Excel, and SQL for profiling and cleaning.

### [🏈 NFL Penalty Capstone](https://public.tableau.com/app/profile/ashwin.pal3698/viz/NFLPenaltyAnalysis/Story)
Analyzes NFL penalties by player position using PostgreSQL and [Tableau](https://public.tableau.com/views/NFLPenaltyAnalysis/Story?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

### [📊 Excel Dashboard & Analytics](https://github.com/brnhaze/Portfolio/blob/main/Excel/walkthrough.md)
Built a dynamic Excel dashboard to track and visualize performance metrics using real-time formulas, conditional formatting, and interactive charts.
- Features include data validation, automated calculations, drop-downs, and multi-sheet integration for insightful reporting.
- Applied advanced Excel functions like INDEX, MATCH, VLOOKUP, and pivot tables for analytical depth.
- Project is designed for business reporting, data entry tracking, and weekly performance monitoring.
- Tools Used: Excel, Formulas, Pivot Tables, Charts, Conditional Formatting

---

## 🧠 Skills & Tools

- **Languages & Libraries**: Python, SQL, Pandas, NumPy, Scikit-learn, TensorFlow, Keras
- **Visualization**: Tableau, Power BI, Matplotlib, Seaborn
- **Cloud & Big Data**: AWS, Azure, PySpark, Apache Spark
- **ETL & Monitoring**: Azure Pipelines, Control-M, Splunk, ServiceNow
- **Machine Learning**: Classification, Regression, Clustering, Neural Networks, Recommender Systems

---

## 💼 Work Experience

### **Command Centre Engineer (Systems Specialist/Analyst)**  
**VanCity Savings Credit Union** | *May 2022 – Present*  
- Monitor, support, and maintain IT systems, ensuring uptime and operational continuity.
- Utilize tools like Splunk, ServiceNow, PagerDuty, and Azure Pipelines for incident response and performance monitoring.
- Automate ETL processes and optimize system performance through proactive troubleshooting.
- Collaborate cross-functionally to resolve issues, enhance workflows, and improve data reporting pipelines.
- Contribute to process documentation and knowledge sharing to maintain high operational standards.

---

## 🎓 Education

- [MIT – Applied Data Science Program (ADSP)](https://credentials.professional.mit.edu/fd3fe8ad-efa7-4853-bc0c-94b274529b48#acc.hcaXUitS)
- [Lighthouse Labs – Data Analytics Diploma  ](https://drive.google.com/file/d/1ZOCayHv5jsZlgkzW6tGexeAJ85jwSjIy/view?usp=drive_link)
- [BCIT – Computer Information Systems Administration Diploma](https://drive.google.com/file/d/1nBbuoL2uJSxZW7VFi127-Ve5jHlG9nW1/view?usp=drive_link)
- [Google Cybersecurity Certificate – Coursera](https://drive.google.com/file/d/1dar56FoOZOFtfPi_y1QSuXc1eKBmj_zp/view?usp=drive_link)
- [Microsoft Certified Data Analyst Associate – Power BI](https://drive.google.com/file/d/1FxhwwFys8ZnkvQa6axn2sKgh-kJa_uD1/view?usp=drive_link)
- [JIBC – Law Enforcement Studies Diploma](https://drive.google.com/file/d/1_-KxEw3X4hKcqmvhLuSRbENABqgnv3M4/view?usp=drive_link)

---

## 📫 Let's Connect!

- [📧 Email](mailto:ashwinpraneelpal@hotmail.com)
- [🔗 LinkedIn](https://www.linkedin.com/in/ashwinpal17/)
- [📄 Resume + Cover Letter](https://www.linkedin.com/in/ashwinpal17/)

> *"Bringing machine learning to life through practical projects, visualization, and impactful insights."*

---

Thank you for visiting my GitHub Portfolio! 🙏
