from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.agent import (
    create_agent_controller,
    delete_agent_controller,
    get_agent_controller,
    list_agents_controller,
    update_agent_controller,
)
from app.core.database import get_db
from app.core.security import get_current_user
from app.schemas.agent import AgentCreate, AgentRead, AgentUpdate

router = APIRouter(prefix="/agents", tags=["agents"])


@router.post("/", response_model=AgentRead, status_code=status.HTTP_201_CREATED)
def create_agent(data: AgentCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return create_agent_controller(data, db, current_user)


@router.get("/", response_model=List[AgentRead])
def list_agents(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return list_agents_controller(db, current_user)


@router.get("/{agent_id}", response_model=AgentRead)
def retrieve_agent(agent_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_agent_controller(agent_id, db, current_user)


@router.put("/{agent_id}", response_model=AgentRead)
def update_agent(agent_id: str, data: AgentUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return update_agent_controller(agent_id, data, db, current_user)


@router.delete("/{agent_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_agent(agent_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    delete_agent_controller(agent_id, db, current_user)
