\# 📊 Customer Churn Prediction Project



This project predicts customer churn using a Machine Learning pipeline built with \*\*Random Forest\*\*.  

It includes:



\- Data preprocessing  

\- Model training  

\- Model evaluation  

\- SHAP explainability (global + local)  

\- Business insights \& retention strategies  

\- Final notebook for complete reproducibility  



---



\## 📁 Project Structure



customer-churn-project/

│

│ README.md

│ requirements.txt

│ Customer\_Churn\_Report\_FINAL.pdf

│

├── data/

│ project\_customer\_churn\_dataset.csv

│ X\_train.csv

│ X\_test.csv

│ y\_train.csv

│ y\_test.csv

│ churn\_model.pkl

│ shap\_summary.png

│ waterfall\_plot.png

│

├── notebooks/

│ churn\_analysis.ipynb

│

└── src/

preprocess.py

train\_model.py

explain\_model.py





---



\## 🚀 How to Run



\### 1️⃣ Install dependencies





pip install -r requirements.txt





\### 2️⃣ Preprocess the dataset





python src/preprocess.py





\### 3️⃣ Train the model





python src/train\_model.py





\### 4️⃣ Generate SHAP explainability plots

python src/explain\_model.py







---



\## 📊 SHAP Explainability



\### 🔹 Global SHAP Summary Plot  

Shows most influential features affecting churn.



!\[SHAP Summary](data/shap\_summary.png)



\*\*File Path:\*\* `data/shap\_summary.png`



---



\### 🔹 Local SHAP Waterfall Plot  

Explains \*why\* one specific customer churned or not.



!\[Waterfall Plot](data/waterfall\_plot.png)



\*\*File Path:\*\* `data/waterfall\_plot.png`



---



\## 🧠 Key SHAP Insights



\### Top 5 features influencing churn:

1\. \*\*Monthly Charges\*\* – Higher billing increases churn probability.  

2\. \*\*Tenure Months\*\* – New customers have significantly higher churn risk.  

3\. \*\*Service Usage (GB)\*\* – Low usage strongly indicates disengagement.  

4\. \*\*Service Outages\*\* – Poor reliability is a major churn factor.  

5\. \*\*Support Calls (last 3 months)\*\* – Frequent complaints indicate dissatisfaction.



---



\## 💡 Business Recommendations



\### 📍 1. High-Billing Customers

\- Offer personalized discounts  

\- Introduce flexible payment options  

\- Provide loyalty benefits  



\### 📍 2. New, Short-Tenure Customers

\- Improve early onboarding  

\- Offer onboarding incentives  

\- Provide proactive engagement  



\### 📍 3. Customers with High Complaints / Outages

\- Provide priority customer service  

\- Assign a support agent  

\- Offer compensation during repeated outages  



---



\## 📤 Push Final Project to GitHub



git add .

git commit -m "Final submission with notebook, SHAP images, and report"

git push origin main







---



\## 📄 Generate PDF Report



This project includes an automated script that creates a final PDF report containing:



\- SHAP Summary Plot  

\- SHAP Waterfall Plot  

\- Model explanation details  



To generate the report, run:



python src/generate\_pdf\_report.py





The output file will be saved as:



Customer\_Churn\_Report\_FINAL.pdf





in the project root directory.





---



\## 👤 Author  

\*\*Infant Mychiline Priya R\*\*



