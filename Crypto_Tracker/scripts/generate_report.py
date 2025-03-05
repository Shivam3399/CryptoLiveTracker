from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import pandas as pd
from analysis import analyze_crypto_data

EXCEL_FILE = "data/crypto_data.xlsx"
REPORT_FILE = "data/analysis_report.pdf"

def generate_pdf_report():
    """Generates a structured and readable PDF report from cryptocurrency analysis."""
    # Load analyzed data
    df = pd.read_excel(EXCEL_FILE, engine='openpyxl')
    
    if df.empty:
        print("No data available for report generation.")
        return
    
    # Perform analysis
    top_5 = df.nlargest(5, "Market Cap")[["Name", "Market Cap"]]
    avg_price = df["Price (USD)"].mean()
    highest_change = df.loc[df["24h % Change"].idxmax(), ["Name", "24h % Change"]]
    lowest_change = df.loc[df["24h % Change"].idxmin(), ["Name", "24h % Change"]]

    # Create PDF canvas
    c = canvas.Canvas(REPORT_FILE, pagesize=A4)
    width, height = A4
    y_position = height - 50  # Start position

    # Report Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y_position, "Cryptocurrency Market Analysis Report")
    y_position -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y_position, f"Report Generated: Live Data")
    y_position -= 20

    # Section: Top 5 Cryptos
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_position, "🔹 Top 5 Cryptocurrencies by Market Cap:")
    y_position -= 20

    c.setFont("Helvetica", 12)
    for _, row in top_5.iterrows():
        c.drawString(50, y_position, f"{row['Name']} - Market Cap: ${row['Market Cap']:,}")
        y_position -= 20

    # Section: Average Price
    y_position -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_position, "📊 Average Price of Top 50 Cryptocurrencies:")
    y_position -= 20

    c.setFont("Helvetica", 12)
    c.drawString(50, y_position, f"${avg_price:,.2f}")
    y_position -= 30

    # Section: Highest & Lowest Change
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_position, "📈 Highest & Lowest 24h Price Change:")
    y_position -= 20

    c.setFont("Helvetica", 12)
    c.drawString(50, y_position, f"📈 Highest: {highest_change['Name']} ({highest_change['24h % Change']:.2f}%)")
    y_position -= 20
    c.drawString(50, y_position, f"📉 Lowest: {lowest_change['Name']} ({lowest_change['24h % Change']:.2f}%)")
    y_position -= 30

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 50, "Report generated using live cryptocurrency data.")

    # Save the PDF
    c.save()
    print(f"✅ Report generated successfully: {REPORT_FILE}")

if __name__ == "__main__":
    generate_pdf_report()
