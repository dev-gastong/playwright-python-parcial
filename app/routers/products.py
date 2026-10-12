from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
    tags=["events"],
    
)

@router.get("/{evento_id}")
def get_events(event_id: int):
    return {"event_id": event_id}