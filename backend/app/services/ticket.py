from sqlalchemy.orm import Session
import uuid
from app.schemas.tickets import TicketCreate, TicketUpdate
from app.models.tickets import Ticket


def get_all_tickets(user_id: str,db:Session):
    return db.query(Ticket).filter(Ticket.user_id == user_id).all()

def get_ticket_by_id(ticket_id:str, db: Session):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def create_ticket(data:TicketCreate,db: Session):

    new_ticket = Ticket(
        id = str(uuid.uuid4()),
        user_id = data.user_id,
        ticket_content = data.ticket_content,
    )

    db.add(new_ticket)
    db.commit()

    return new_ticket

def update_ticket(data:TicketUpdate,db:Session):
    ticket = get_ticket_by_id(data.id,db)
    if not ticket:
        return None
    
    if data.ticket_content is not None:
        ticket.ticket_content = data.ticket_content
    
    if data.category is not None:
        ticket.category = data.category
    
    if data.status is not None:
        ticket.status = data.status
    
    if data.resolved_by_type is not None:
        ticket.resolved_by_type = data.resolved_by_type
    
    if data.resolved_by_human_id is not None:
        ticket.resolved_by_human_id = data.resolved_by_human_id

    db.commit()
    db.refresh(ticket)
    return ticket


