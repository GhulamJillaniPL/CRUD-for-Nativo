# Nativo Campaign Management API

A FastAPI-based application for managing native advertising campaigns using the Nativo API.

## Features

- Complete CRUD operations for advertising campaigns
- Campaign status management (pause/activate)
- Async HTTP client for better performance
- Input validation using Pydantic models
- Error handling and logging
- SQLite database for local storage
- Auto-generated API documentation

## Prerequisites

- Python 3.8+
- pip package manager
- Nativo API credentials
- Linux environment

## Installation

1. Update system packages:
```bash
sudo apt-get update
sudo apt-get upgrade
```

2. Install Python and required system packages:
```bash
sudo apt-get install python3.8 python3.8-venv python3-pip
```

3. Create project directory:
```bash
mkdir nativo_api
cd nativo_api
```

4. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Create project structure:
```bash
mkdir -p app/api app/services
touch app/__init__.py app/main.py app/config.py app/models.py app/schemas.py
touch app/api/__init__.py app/api/endpoints.py
touch app/services/__init__.py app/services/nativo_service.py
touch requirements.txt .env
```

6. Copy the code files from the codebase to their respective locations in the project structure.

7. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create .env file with your Nativo API credentials:
```bash
nano .env
```

2. Add the following content (replace with your actual credentials):
```
NATIVO_API_KEY=your_nativo_api_key
NATIVO_API_SECRET=your_nativo_api_secret
DATABASE_URL=sqlite:///./campaigns.db
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Access the API:
- API endpoints: `http://localhost:8000/api/v1/`
- API documentation: `http://localhost:8000/docs`
- Alternative documentation: `http://localhost:8000/redoc`

## API Usage Examples

### Create a new campaign
```bash
curl -X POST "http://localhost:8000/api/v1/campaigns" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Summer Campaign 2024",
           "description": "Native ads for summer products",
           "type": "native",
           "budget": 10000,
           "start_date": "2024-06-01T00:00:00Z",
           "end_date": "2024-08-31T23:59:59Z",
           "daily_budget": 500,
           "targeting": {
             "countries": ["US", "CA"],
             "devices": ["mobile", "desktop"],
             "languages": ["en"]
           }
         }'
```

### Get campaign details
```bash
curl "http://localhost:8000/api/v1/campaigns/{campaign_id}"
```

### Update campaign
```bash
curl -X PUT "http://localhost:8000/api/v1/campaigns/{campaign_id}" \
     -H "Content-Type: application/json" \
     -d '{
           "daily_budget": 600,
           "targeting": {
             "countries": ["US", "CA", "UK"],
             "devices": ["mobile", "desktop"],
             "languages": ["en"]
           }
         }'
```

### Pause campaign
```bash
curl -X POST "http://localhost:8000/api/v1/campaigns/{campaign_id}/pause"
```

### Activate campaign
```bash
curl -X POST "http://localhost:8000/api/v1/campaigns/{campaign_id}/activate"
```

### Delete campaign
```bash
curl -X DELETE "http://localhost:8000/api/v1/campaigns/{campaign_id}"
```

