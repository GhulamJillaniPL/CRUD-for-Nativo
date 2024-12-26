from datetime import datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, constr, conint

class CampaignStatus(str, Enum):
    DRAFT = 'draft'
    ACTIVE = 'active'
    PAUSED = 'paused'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class CampaignType(str, Enum):
    DISPLAY = 'display'
    VIDEO = 'video'
    NATIVE = 'native'
    SPONSORED = 'sponsored'

class Campaign(BaseModel):
    id: str
    name: str
    description: Optional[str]
    status: CampaignStatus
    type: CampaignType
    budget: float
    start_date: datetime
    end_date: Optional[datetime]
    daily_budget: Optional[float]
    targeting: dict
    created_at: datetime
    updated_at: datetime

class CampaignCreate(BaseModel):
    name: constr(min_length=3, max_length=100)
    description: Optional[str]
    type: CampaignType
    budget: conint(gt=0)
    start_date: datetime
    end_date: Optional[datetime]
    daily_budget: Optional[float]
    targeting: dict

class CampaignUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    status: Optional[CampaignStatus]
    budget: Optional[float]
    daily_budget: Optional[float]
    targeting: Optional[dict]
    end_date: Optional[datetime]
