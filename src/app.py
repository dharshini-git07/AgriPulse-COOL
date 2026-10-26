from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os
from src.processor import CropVisionProcessor
from src.agent_loop import AgenticDecisionLoop

app = FastAPI(
    title="AgriPulse COOL API",
    description="OpenCV 5 & AWS Graviton Powered Precision Agriculture Agent",
    version="1.0.0"
)

# Mount static folder for frontend dashboard
app.mount("/static", StaticFiles(directory="static"), name="static")

processor = CropVisionProcessor()
agent = AgenticDecisionLoop()

class InspectionRequest(BaseModel):
    image_path: str = "data/sample_crop_frame.jpg"

@app.get("/", response_class=HTMLResponse)
def serve_dashboard():
    """Serves the interactive AgriPulse COOL frontend dashboard."""
    html_path = "static/index.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return {"message": "AgriPulse COOL API is running. Visit /docs for Swagger UI."}

@app.post("/api/v1/inspect")
def run_inspection(payload: InspectionRequest):
    try:
        metrics = processor.analyze_frame(payload.image_path)
        decision = agent.evaluate_and_act(metrics)
        return {
            "vision_analysis": metrics,
            "agent_decision": decision,
            "cloud_optimizer": "AWS Graviton + COOL Acceleration Active"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)