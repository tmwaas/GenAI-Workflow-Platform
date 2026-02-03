"""
Multi-agent finance example
Risk Agent + Compliance Agent collaboration
"""

from genai_workflow.llm import chat_completion

def risk_agent(data: str) -> str:
    return chat_completion(
        f"You are a risk analyst. Identify risks in:\n{data}"
    )

def compliance_agent(data: str) -> str:
    return chat_completion(
        f"You are a compliance officer. Identify regulatory concerns in:\n{data}"
    )

if __name__ == "__main__":
    input_data = "SME loan for cross-border logistics expansion"

    risk = risk_agent(input_data)
    compliance = compliance_agent(input_data)

    print("RISK ANALYSIS:\n", risk)
    print("\nCOMPLIANCE ANALYSIS:\n", compliance)
