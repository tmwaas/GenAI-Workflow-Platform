"""
CrewAI-style summarization agent
Enterprise-ready example (no hard dependency on CrewAI runtime)
"""

from typing import List
from genai_workflow.llm import chat_completion

class SummaryAgent:
    def __init__(self, role: str = "Policy Summary Agent"):
        self.role = role

    def summarize(self, document: str) -> str:
        prompt = f"""
You are a senior banking analyst.
Summarize the following internal document in a concise, structured way.

Document:
{document}
"""
        return chat_completion(prompt)

if __name__ == "__main__":
    agent = SummaryAgent()
    print(
        agent.summarize(
            "This policy defines SME loan approval thresholds and risk scoring rules."
        )
    )
