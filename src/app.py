"""
AgriPulse COOL - FastAPI Backend Telemetry & Processing Server
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.processor import CropVisionProcessor
from src.agent_loop import AgenticDecisionLoop

app = FastAPI(
    title="AgriPulse COOL API",
    description="OpenCV 5 & AWS Graviton Powered Precision Agriculture Agent",
    version="1.0.0"
)

processor = CropVisionProcessor()
agent = AgenticDecisionLoop()

class InspectionRequest(BaseModel):
    image_path: str = "data/sample_crop_frame.jpg"

@app.get("/")
def root():
    return {
        "project": "AgriPulse COOL",
        "sponsor": "OpenCV AI Competition 2026 powered by AWS",
        "status": "Operational"
    }

@app.post("/api/v1/inspect")
def run_inspection(payload: InspectionRequest):
    try:
        # Step 1: Perception (OpenCV 5 + COOL)
        metrics = processor.analyze_frame(payload.image_path)
        
        # Step 2: Agentic Reasoning & Decision Loop
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