from fastapi import Depends,APIRouter,HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.schemas.tickets import TicketCreate
from app.services.ticket import get_all_tickets,get_ticket_by_id,create_ticket

router = APIRouter(prefix = "/tickets")

@router.get("/")
def get_all_tickets_route(user_id:str,db: Session = Depends(get_db)):
    all_tickets = get_all_tickets(user_id,db)

    if not all_tickets:
        raise HTTPException(status_code=404, detail="No tickets found")
    return {"tickets" : all_tickets}

@router.get("/{ticket_id}")
def get_ticket_route(ticket_id:str, db: Session = Depends(get_db)):
    ticket = get_ticket_by_id(ticket_id,db)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"ticket": ticket}

@router.post("/")
def create_ticket_route(data:TicketCreate,db: Session = Depends(get_db)):
    ticket = create_ticket(data,db)
    if not ticket:
        raise HTTPException(status_code=500, detail="Failed to create ticket")
    return {
        "ticket_id": ticket.id,
        "status": ticket.status,
        "category": ticket.category,
        "message": "Ticket created successfully"
    }