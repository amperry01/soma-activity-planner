from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Recommendation(BaseModel):
    id: int
    activity_type: str # e.g., "cardio", "yoga", "running"
    optimal_start: datetime # when the activity should ideally start
    optimal_end: datetime # when the activity should ideally end
    intensity: str # e.g., "low", "medium", "high"
    reason: Optional[str] = None # explanation based on health data
    priority: Optional[int] # priority level for the recommendation

