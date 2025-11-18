{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "74f42a79-3e35-45a2-abf4-a52ad3bf35eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PDF successfully created at: C:\\Users\\GERALD ANTONY\\Documents\\customer-churn-project\\Customer_Churn_Report_FINAL.pdf\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from reportlab.lib.pagesizes import A4\n",
    "from reportlab.pdfgen import canvas\n",
    "from reportlab.lib.utils import ImageReader\n",
    "\n",
    "# Get absolute paths\n",
    "project_root = r\"C:\\Users\\GERALD ANTONY\\Documents\\customer-churn-project\"\n",
    "summary_path = os.path.join(project_root, \"data\", \"shap_summary.png\")\n",
    "waterfall_path = os.path.join(project_root, \"data\", \"waterfall_plot.png\")\n",
    "\n",
    "pdf = canvas.Canvas(os.path.join(project_root, \"Customer_Churn_Report_FINAL.pdf\"), pagesize=A4)\n",
    "\n",
    "pdf.setFont(\"Helvetica-Bold\", 18)\n",
    "pdf.drawString(50, 800, \"Customer Churn Prediction — Final Report\")\n",
    "\n",
    "pdf.setFont(\"Helvetica\", 11)\n",
    "pdf.drawString(50, 770, \"This report contains model evaluation and SHAP visual explanations.\")\n",
    "\n",
    "# SHAP Summary Plot\n",
    "pdf.setFont(\"Helvetica-Bold\", 14)\n",
    "pdf.drawString(50, 740, \"1. SHAP Summary Plot (Global Feature Importance)\")\n",
    "pdf.drawImage(ImageReader(summary_path), 50, 400, width=500, height=300)\n",
    "\n",
    "# SHAP Waterfall Plot\n",
    "pdf.setFont(\"Helvetica-Bold\", 14)\n",
    "pdf.drawString(50, 350, \"2. SHAP Waterfall Plot (Local Explanation)\")\n",
    "pdf.drawImage(ImageReader(waterfall_path), 50, 30, width=500, height=300)\n",
    "\n",
    "pdf.save()\n",
    "\n",
    "print(\"PDF successfully created at:\", os.path.join(project_root, \"Customer_Churn_Report_FINAL.pdf\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "93859266-850c-41b1-a766-2df2ed23b24f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(os.path.exists(r\"C:\\Users\\GERALD ANTONY\\Documents\\customer-churn-project\\data\\shap_summary.png\"))\n",
    "print(os.path.exists(r\"C:\\Users\\GERALD ANTONY\\Documents\\customer-churn-project\\data\\waterfall_plot.png\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9082293c-6a1b-40da-b2d0-e718d0fe78bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
