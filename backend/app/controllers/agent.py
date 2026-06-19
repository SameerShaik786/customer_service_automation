from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.agent import Agent
from app.services.agent import (
    create_agent,
    get_agents_for_user,
    get_agent_by_id,
    update_agent,
    delete_agent,
)


def create_agent_controller(data, db: Session, current_user) -> Agent:
    return create_agent(data, db, current_user.id)


def list_agents_controller(db: Session, current_user) -> list[Agent]:
    return get_agents_for_user(current_user.id, db)


def get_agent_controller(agent_id: str, db: Session, current_user) -> Agent:
    agent = get_agent_by_id(agent_id, db)
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found",
        )
    if agent.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this agent",
        )
    return agent


def update_agent_controller(agent_id: str, data, db: Session, current_user) -> Agent:
    agent = get_agent_by_id(agent_id, db)
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found",
        )
    if agent.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this agent",
        )
    return update_agent(agent, data, db)


def delete_agent_controller(agent_id: str, db: Session, current_user) -> None:
    agent = get_agent_by_id(agent_id, db)
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found",
        )
    if agent.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this agent",
        )
    delete_agent(agent, db)
