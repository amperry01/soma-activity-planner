from fastapi import APIRouter
from app.utils.oura_loader import load_oura_data

router = APIRouter()

@router.get("/oura-data")
def read_export():
    """Endpoint to read Oura data export.
    Returns:
        dict: Parsed Oura data.
    """
    #TODO: replace with actual export path
    filepath = "backend/data/oura_export.json"
    return load_oura_data(filepath)