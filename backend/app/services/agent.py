import uuid
from typing import Optional
from sqlalchemy.orm import Session
from app.models.agent import Agent


def _build_config(data) -> dict:
    if hasattr(data, "config") and data.config is not None:
        return data.config

    config = {}
    if hasattr(data, "nodes"):
        config["nodes"] = data.nodes
    if hasattr(data, "edges"):
        config["edges"] = data.edges
    return config


def create_agent(data, db: Session, user_id: str) -> Agent:
    agent_id = str(uuid.uuid4())
    new_agent = Agent(
        id=agent_id,
        user_id=user_id,
        name=data.name,
        description=data.description,
        system_prompt=data.system_prompt,
        config=_build_config(data),
        status=getattr(data, "status", "active") or "active",
        endpoint=f"/api/agents/{agent_id}/run",
        total_runs=0,
        total_cost=0.0,
    )

    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)
    return new_agent


def get_agents_for_user(user_id: str, db: Session) -> list[Agent]:
    return db.query(Agent).filter(Agent.user_id == user_id).all()


def get_agent_by_id(agent_id: str, db: Session) -> Optional[Agent]:
    return db.query(Agent).filter(Agent.id == agent_id).first()


def update_agent(agent: Agent, data, db: Session) -> Agent:
    if hasattr(data, "name") and data.name is not None:
        agent.name = data.name
    if hasattr(data, "description") and data.description is not None:
        agent.description = data.description
    if hasattr(data, "system_prompt") and data.system_prompt is not None:
        agent.system_prompt = data.system_prompt
    if hasattr(data, "status") and data.status is not None:
        agent.status = data.status
    if hasattr(data, "config") and data.config is not None:
        agent.config = data.config
    if hasattr(data, "nodes") or hasattr(data, "edges"):
        built_config = _build_config(data)
        if built_config:
            agent.config = built_config

    db.commit()
    db.refresh(agent)
    return agent


def delete_agent(agent: Agent, db: Session) -> None:
    db.delete(agent)
    db.commit()
