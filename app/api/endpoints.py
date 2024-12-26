from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from ..services.nativo_service import NativoService
from ..models import Campaign, CampaignCreate, CampaignUpdate

router = APIRouter()
nativo_service = NativoService()

@router.post("/campaigns", response_model=Campaign)
async def create_campaign(campaign_data: CampaignCreate):
    try:
        campaign = await nativo_service.create_campaign(campaign_data)
        return campaign
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/campaigns/{campaign_id}", response_model=Campaign)
async def get_campaign(campaign_id: str):
    try:
        campaign = await nativo_service.get_campaign(campaign_id)
        return campaign
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/campaigns/{campaign_id}", response_model=Campaign)
async def update_campaign(campaign_id: str, campaign_data: CampaignUpdate):
    try:
        campaign = await nativo_service.update_campaign(campaign_id, campaign_data)
        return campaign
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/campaigns/{campaign_id}")
async def delete_campaign(campaign_id: str):
    try:
        await nativo_service.delete_campaign(campaign_id)
        return {"message": f"Campaign {campaign_id} has been deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/campaigns/{campaign_id}/pause", response_model=Campaign)
async def pause_campaign(campaign_id: str):
    try:
        campaign = await nativo_service.pause_campaign(campaign_id)
        return campaign
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/campaigns/{campaign_id}/activate", response_model=Campaign)
async def activate_campaign(campaign_id: str):
    try:
        campaign = await nativo_service.activate_campaign(campaign_id)
        return campaign
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
