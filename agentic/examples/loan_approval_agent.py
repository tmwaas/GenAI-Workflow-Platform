"""
A simple agentic workflow that evaluates SME loan applications.
This mimics a real bank workflow:
- Document extraction
- Risk scoring
- Compliance evaluation
- Final decision synthesis
"""

from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

def analyze_risk(data):
    prompt = f"""
    You are a risk officer for SME loans. Analyze the risk level.

    Application data:
    {data}

    Return: risk score 1–10 + justification.
    """
    return client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message["content"]

def check_compliance(data):
    prompt = f"""
    Evaluate compliance risks (AML, fraud, missing docs) for:
    {data}
    """
    return client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message["content"]

def final_decision(risk, compliance):
    prompt = f"""
    You are the decision engine. Based on this:

    Risk:
    {risk}

    Compliance:
    {compliance}

    Output a final approval decision (Approve / Decline / Manual Review)
    with 3 bullet points justification.
    """
    return client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message["content"]

if __name__ == "__main__":
    sample = {
        "revenue": 95000,
        "industry": "Logistics",
        "credit_score": 680,
        "loan_amount": 30000
    }

    risk = analyze_risk(sample)
    compliance = check_compliance(sample)
    decision = final_decision(risk, compliance)

    print("\nRISK ANALYSIS:\n", risk)
    print("\nCOMPLIANCE:\n", compliance)
    print("\nFINAL DECISION:\n", decision)
