# risk_rules.py
import pandas as pd

# Risk levels and colors
RISK_LEVELS = {
    'High': 'red',
    'Medium': 'orange',
    'Low': 'green'
}

# --- Enhanced risk evaluation logic ---
HIGH_KEYWORDS = ['personal data', 'sensitive', 'private', 'personally identifiable info', 'without consent', 'no anonymization']
MEDIUM_KEYWORDS = ['analytics', 'prediction', 'automation', 'forecast', 'evaluate']
LOW_KEYWORDS = ['dashboard', 'report', 'summary', 'insight']

def evaluate_feature(feature_name, feature_desc):
    """
    Enhanced heuristic for SaaS AI feature risk evaluation.
    """
    desc = feature_desc.lower()
    if any(k in desc for k in HIGH_KEYWORDS):
        return 'High'
    elif any(k in desc for k in MEDIUM_KEYWORDS):
        return 'Medium'
    else:
        return 'Low'

def evaluate_product(product_name, features_df):
    """
    Evaluates all features for a product.
    Returns DataFrame with Product, Feature, Description, Severity, Color
    """
    df = features_df.copy()
    df['Severity'] = df.apply(lambda row: evaluate_feature(row['Feature'], row['Description']), axis=1)
    df['Color'] = df['Severity'].map(RISK_LEVELS)
    df['Product'] = product_name
    return df[['Product','Feature','Description','Severity','Color']]
