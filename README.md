\# Customer Churn Prediction with SHAP Explainability



This project predicts customer churn using machine learning models and explains model predictions using SHAP (SHapley Additive exPlanations).  



The main goals are:



\- Build a machine learning model to predict churn  

\- Analyze feature importance using SHAP  

\- Visualize predictions and key business insights  

\- Provide a clear, organized structure for deployment  



---



\## 📂 Project Structure



customer-churn-project/

│── data/

│ └── project\_customer\_churn\_dataset.csv

│── notebooks/

│ ├── churn\_analysis.ipynb

│ └── SHAP\_analysis\_of\_customer\_churn\_prediction.ipynb

│── src/

│ ├── preprocess.py

│ ├── train\_model.py

│ └── explain\_model.py

│── requirements.txt

│── README.md





---



\## 🚀 How to Run



\### 1️⃣ Install dependencies





pip install -r requirements.txt





\### 2️⃣ Run preprocessing





python src/preprocess.py





\### 3️⃣ Train the model





python src/train\_model.py





\### 4️⃣ Generate SHAP explainability report





python src/explain\_model.py





---



\## 📊 SHAP Explainability



This project generates:



\- Global feature importance  

\- SHAP summary plot  

\- SHAP force plot  

\- Individual prediction explanations  



---



\## 📌 Dataset



Make sure your dataset is stored here:







customer-churn-project/data/project\_customer\_churn\_dataset.csv





---



\## ✨ Author



Created by \*\*infantpriya73\*\*  

