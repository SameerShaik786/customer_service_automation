from app.agents.langgraph_orchestrator import AgentState
from app.services.llm import generate_json

def billing_agent(state: AgentState):
    prompt = f"""You are a billing support specialist.

        Respond to this customer ticket professionally and concisely.
        If you cannot answer confidently, respond with exactly: ESCALATE

        Ticket: "{state['ticket_content']}"
    """

    response = generate_json(prompt)
    
    if response is None:
        return {"ai_reply" : "ESCALATE","confidence" : 0.0}
    
    return {
        "ai_reply" : response.get("reply","ESCALATE"),
        "confidence" : response.get("confidence",0.0)
    }