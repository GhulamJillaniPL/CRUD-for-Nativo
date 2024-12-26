import httpx
from datetime import datetime
from typing import List, Optional
from ..config import settings
from ..models import Campaign, CampaignCreate, CampaignUpdate, CampaignStatus

class NativoService:
    def __init__(self):
        self.base_url = "https://api.nativo.com/v1"
        self.headers = {
            "Authorization": f"Bearer {settings.nativo_api_key}",
            "Content-Type": "application/json"
        }

    async def create_campaign(self, campaign_data: CampaignCreate) -> Campaign:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/campaigns",
                    headers=self.headers,
                    json=campaign_data.dict()
                )
                response.raise_for_status()
                data = response.json()
                return Campaign(**data)
            except httpx.HTTPError as e:
                raise Exception(f"Failed to create campaign: {str(e)}")

    async def get_campaign(self, campaign_id: str) -> Campaign:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/campaigns/{campaign_id}",
                    headers=self.headers
                )
                response.raise_for_status()
                data = response.json()
                return Campaign(**data)
            except httpx.HTTPError as e:
                raise Exception(f"Failed to get campaign: {str(e)}")

    async def update_campaign(self, campaign_id: str, campaign_data: CampaignUpdate) -> Campaign:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.put(
                    f"{self.base_url}/campaigns/{campaign_id}",
                    headers=self.headers,
                    json=campaign_data.dict(exclude_unset=True)
                )
                response.raise_for_status()
                data = response.json()
                return Campaign(**data)
            except httpx.HTTPError as e:
                raise Exception(f"Failed to update campaign: {str(e)}")

    async def delete_campaign(self, campaign_id: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.delete(
                    f"{self.base_url}/campaigns/{campaign_id}",
                    headers=self.headers
                )
                response.raise_for_status()
            except httpx.HTTPError as e:
                raise Exception(f"Failed to delete campaign: {str(e)}")

    async def pause_campaign(self, campaign_id: str) -> Campaign:
        update_data = CampaignUpdate(status=CampaignStatus.PAUSED)
        return await self.update_campaign(campaign_id, update_data)

    async def activate_campaign(self, campaign_id: str) -> Campaign:
        update_data = CampaignUpdate(status=CampaignStatus.ACTIVE)
        return await self.update_campaign(campaign_id, update_data)
