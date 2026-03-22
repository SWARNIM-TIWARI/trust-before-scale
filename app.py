# app.py
import streamlit as st
import pandas as pd
import os
from risk_rules import evaluate_product
from mock_openai import get_recommendation

# --- Streamlit page config ---
st.set_page_config(page_title="SaaS AI Feature Risk Evaluator", layout="wide")

# --- Title ---
st.title("⚡ SaaS AI Feature Risk Evaluator")
st.markdown("Evaluate features for High/Medium/Low risk and get offline mock recommendations.")

# --- Initialize or load history (fresh every session) ---
history_df = pd.DataFrame(columns=['Product','Feature','Description','Severity','Color','Recommendation'])

# --- Product input ---
product_name = st.text_input("Enter Product Name", "DataSecure CRM")

# --- Number of features input ---
num_features = st.number_input("Number of Features", min_value=1, max_value=20, value=4, step=1)

# --- Dynamic feature inputs ---
feature_names = []
feature_descs = []

st.subheader("📝 Feature Details")
for i in range(num_features):
    feature_name = st.text_input(f"Feature {i+1} Name", key=f"name_{i}")
    feature_desc = st.text_area(f"Feature {i+1} Description", key=f"desc_{i}", height=50)
    feature_names.append(feature_name)
    feature_descs.append(feature_desc)

# --- Evaluate button ---
if st.button("Evaluate Product"):
    if not product_name.strip():
        st.error("Please enter a product name.")
    else:
        # Prepare input DataFrame
        df = pd.DataFrame({'Feature': feature_names, 'Description': feature_descs})

        # Evaluate features using enhanced rules
        eval_df = evaluate_product(product_name, df)

        # Add mock LLM recommendations
        eval_df['Recommendation'] = eval_df['Severity'].apply(lambda s: get_recommendation(s))

        # --- Save to history ---
        history_df = pd.concat([history_df, eval_df], ignore_index=True)

        # --- Color-coded evaluation table ---
        st.subheader("✅ Evaluation Results")
        def style_row(row):
            return ['background-color: {}'.format(row.Color)]*len(row)
        st.dataframe(eval_df.style.apply(style_row, axis=1))

        # --- Multi-product dashboard (summary) ---
        st.subheader("📊 Multi-product Dashboard")
        summary = history_df.groupby(['Product','Severity']).size().unstack(fill_value=0)
        st.dataframe(summary)

        # --- Executive view: Top N High-Risk Features ---
        st.subheader("🧾 Executive View - Top High-Risk Features")
        top_high = history_df[history_df['Severity']=='High'].sort_values(by='Product')
        if top_high.empty:
            st.info("No High-Risk features found.")
        else:
            st.dataframe(top_high[['Product','Feature','Severity','Recommendation']])

        # --- CSV Export ---
        csv = history_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Evaluation History", data=csv, file_name="evaluation_history.csv", mime="text/csv")
