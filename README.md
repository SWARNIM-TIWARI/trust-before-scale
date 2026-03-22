# ⚖️ Trust Before Scale — AI Feature Risk Intelligence

A rule-based AI feature risk assessment tool for SaaS teams to identify ethical, privacy, and governance risks in AI-enabled features **before launch** — fully offline, zero-cost, no API keys required.

> **Design Philosophy:** Risk assessment should happen before scale, not after. This tool is built to surface ethical and governance concerns at the feature level, early in the product lifecycle.

---

## 🚀 Features

- 🔴 **High / Medium / Low risk classification** using deterministic keyword-based heuristics
- 🧠 **Mock LLM advisory interface** — governance-recommended mitigations without model inference
- 📊 **Multi-product dashboard** with aggregated risk summaries across products
- 🧾 **Executive view** — top high-risk features surfaced for decision-makers
- 📥 **CSV export** of full evaluation history
- 📄 **PDF report generation** for offline governance review
- 🌡️ **Risk heatmap** — product-level visualization of feature severity
- 🐳 **Fully containerized** with Docker

---

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| **UI** | Streamlit |
| **Data** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Reporting** | FPDF, OpenPyXL |
| **Risk Engine** | Rule-based heuristics (deterministic) |
| **Advisory** | Mock LLM interface (no inference) |
| **Deployment** | Docker |

---

## 📂 Project Structure

```
ai_ethics_evaluator/
├── app.py              # Streamlit UI — main application entry point
├── risk_rules.py       # Keyword-based risk classification engine
├── mock_openai.py      # Mock LLM advisory interface for recommendations
├── utils.py            # PDF export, CSV history, heatmap generation
├── requirements.txt
├── Dockerfile
├── README.md
└── data/
    └── history.csv     # Auto-created after first evaluation run
```

---

## ⚙️ Installation & Running

### Option 1 — Local

1. **Clone the repository**

```bash
git clone https://github.com/SWARNIM-TIWARI/trust-before-scale.git
cd trust-before-scale
```

2. **Create a virtual environment** (recommended)

```bash
python -m venv venv
```

3. **Activate the virtual environment**

- Windows (PowerShell):
  ```bash
  .\venv\Scripts\Activate.ps1
  ```
- Windows (CMD):
  ```bash
  .\venv\Scripts\activate.bat
  ```
- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run the app**

```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

---

### Option 2 — Docker

1. **Build the image**

```bash
docker build -t trust-before-scale .
```

2. **Run the container**

```bash
docker run -p 8501:8501 trust-before-scale
```

3. Open your browser at `http://localhost:8501`

---

## 🔍 How Risk Classification Works

Risk is evaluated at the **individual feature level** based on textual descriptions using deterministic keyword matching — no model inference involved.

| Risk Level | Triggered By | Example Keywords |
|---|---|---|
| 🔴 High | Privacy & consent signals | `personal data`, `sensitive`, `without consent`, `no anonymization` |
| 🟡 Medium | Automation & prediction signals | `analytics`, `prediction`, `automation`, `forecast` |
| 🟢 Low | Reporting & insight signals | `dashboard`, `report`, `summary`, `insight` |

High-risk features are automatically flagged with governance-recommended mitigations such as audit trails, human review, and data minimization.

---

## 📊 Dashboard Views

- **Evaluation Results** — color-coded feature risk table per product
- **Multi-product Dashboard** — aggregated severity counts across all evaluated products
- **Executive View** — top high-risk features sorted by product for decision-makers
- **Risk Heatmap** — product × feature severity matrix

---

## ⚠️ Explicit Limitations

Documented intentionally and transparently:

- Risk classification is keyword-based and does not perform cross-feature reasoning
- The advisory interface is a mock — no LLM inference occurs
- Severity is determined solely by feature description text, not product context
- This tool is a **learning-focused approximation** of real-world AI risk workflows, not a compliance certification system
- Does not currently integrate with regulatory frameworks (SOC 2, ISO 42001) — planned for future versions

---

## 🔭 Future Direction

- **LLM-powered mitigations** replacing the mock advisory interface
- **Regulatory framework integration** — SOC 2, ISO 42001, EU AI Act alignment
- **Cross-feature reasoning** for systemic risk detection
- **Role-based access control** via FastAPI backend
- **Streamlit Community Cloud** deployment for live demo

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

*Built to demonstrate that ethical AI governance starts at the feature level — before scale, not after.*