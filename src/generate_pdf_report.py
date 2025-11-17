import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# Get absolute paths
project_root = r"C:\Users\GERALD ANTONY\Documents\customer-churn-project"
summary_path = os.path.join(project_root, "data", "shap_summary.png")
waterfall_path = os.path.join(project_root, "data", "waterfall_plot.png")

pdf_path = os.path.join(project_root, "Customer_Churn_Report_FINAL.pdf")
pdf = canvas.Canvas(pdf_path, pagesize=A4)

pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(50, 800, "Customer Churn Prediction — Final Report")

pdf.setFont("Helvetica", 11)
pdf.drawString(50, 770, "This report contains model evaluation and SHAP visual explanations.")

# SHAP Summary Plot
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(50, 740, "1. SHAP Summary Plot (Global Feature Importance)")
pdf.drawImage(ImageReader(summary_path), 50, 400, width=500, height=300)

# SHAP Waterfall Plot
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(50, 350, "2. SHAP Waterfall Plot (Local Explanation)")
pdf.drawImage(ImageReader(waterfall_path), 50, 30, width=500, height=300)

pdf.save()

print("PDF successfully created at:", pdf_path)
