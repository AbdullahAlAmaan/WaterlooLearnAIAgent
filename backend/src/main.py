from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services.calendar_service import CalendarService # type: ignore
from .config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
calendar_service = CalendarService(settings.GOOGLE_CALENDAR_CREDENTIALS_PATH)

@app.get("/api/events")
async def get_events():
    """
    Retrieve all upcoming events from the calendar
    """
    return await calendar_service.get_upcoming_events()

@app.get("/api/health")
async def health_check():
    """
    Check if the API is running
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)