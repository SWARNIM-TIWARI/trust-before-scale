import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

HISTORY_FILE = "history.csv"


def load_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    else:
        df = pd.DataFrame(columns=['Product','Feature','Description','Severity','Color','Recommendation'])
        df.to_csv(HISTORY_FILE, index=False)
        return df

def save_history(df):
    df.to_csv(HISTORY_FILE, index=False)

def plot_heatmap(df):
    """
    Product-level heatmap of risk severity
    """
    if df.empty:
        return None
    severity_map = {'Low':1,'Medium':2,'High':3}
    pivot = df.pivot_table(index='Product', columns='Feature', values='Severity', aggfunc=lambda x: severity_map.get(x.iloc[0],0))
    plt.figure(figsize=(8,4))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="RdYlGn_r")
    plt.tight_layout()
    plt.show()
    return plt

def export_pdf(df, filename="Executive_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200,10,"Executive Risk Report", ln=True, align='C')
    pdf.ln(5)
    for prod in df['Product'].unique():
        pdf.cell(0,10,f"Product: {prod}", ln=True)
        prod_df = df[df['Product']==prod]
        for idx,row in prod_df.iterrows():
            pdf.multi_cell(0,10,f"- {row['Feature']} [{row['Severity']}] : {row['Recommendation']}")
        pdf.ln(5)
    pdf.output(filename)
    return filename
