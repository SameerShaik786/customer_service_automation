from app.agents.langgraph_orchestrator import AgentState
from app.services.llm import generate_json

def technical_agent(state: AgentState):
    prompt = f"""You are a technical support engineer.

Respond to this customer ticket with clear steps.
If you cannot answer confidently, respond with exactly: ESCALATE

Ticket: "{state['ticket_content']}"
"""
    response = generate_json(f'{prompt}\nRespond with JSON: {{"reply": "your response", "confidence": 0.0 to 1.0}}')
    
    if response is None:
        return {"ai_reply": "ESCALATE", "confidence": 0.0}
    
    return {
        "ai_reply": response.get("reply", "ESCALATE"),
        "confidence": response.get("confidence", 0.0)
    }