from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from app.services.llm import generate_json
from app.agents.billing_agent import billing_agent
from app.agents.general_agent import general_agent
from app.agents.technical_agent import technical_agent

class AgentState(TypedDict):
    ticket_id: str
    ticket_content: str
    category: Optional[str]
    confidence: Optional[str]
    ai_reply: Optional[str]
    status: Optional[str]

def classify_node(state: AgentState):
    prompt = f"""You are a support ticket classifier.

        Analyze this ticket and respond with JSON only:
        {{
            "category": "billing" | "technical" | "general",
            "confidence": 0.0 to 1.0,
            "reason": "brief explanation"
        }}

        Rules:
            - billing: payment, refund, charge, invoice, subscription
            - technical: API, error, bug, crash, integration, not working
            - general: account, password, login, feature request, other

        Ticket: "{state['ticket_content']}"
        """
    result = generate_json(prompt)

    if result is None:
        return {"category" : "general", "confidence": 0.5}
    
    return {
        "category" : result.get("category","general"),
        "confidence": result.get("confidence",0.5)
    }

    