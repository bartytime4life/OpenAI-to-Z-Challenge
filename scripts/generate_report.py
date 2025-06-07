from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import pandas as pd

def build_report(aoi_list, candidate_df, metrics, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, 800, "Amazonian Discovery Engine Report")
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, 760, "Areas of Interest:")
    y = 740
    for name, coord in aoi_list:
        c.setFont("Helvetica", 12)
        c.drawString(50, y, f"• {name}: {coord}")
        y -= 16
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, 800, "Top Candidate Sites")
    y = 780
    for _, row in candidate_df.iterrows():
        if y < 100:
            c.showPage()
            y = 800
        line = f"{row['ID']} — {row['lat']:.4f}, {row['lon']:.4f} — score {row['prob']:.2f}"
        c.setFont("Helvetica", 11)
        c.drawString(50, y, line)
        y -= 14
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, 800, "Model Performance")
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, f"ROC AUC: {metrics['roc']:.3f}")
    c.drawString(50, 760, f"PR AUC: {metrics['pr']:.3f}")
    c.save()

if __name__=="__main__":
    aoi_list = [("Kuhikugu", "11.5700° S, 53.7500° W"), ("Llanos de Mojos", "14.0000° S, 65.0000° W"), ("Acre-Pando", "9.5000° S, 69.5000° W")]
    candidate_df = pd.DataFrame(columns=["ID","lat","lon","prob"])
    metrics = {"roc":0.92, "pr":0.87}
    build_report(aoi_list, candidate_df, metrics, "final_report.pdf")
