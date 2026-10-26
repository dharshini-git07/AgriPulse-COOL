"""
AgriPulse COOL - Agentic Vision Decision Loop
Perceives visual output from OpenCV 5, reasons about actions, and triggers IoT responses.
"""

class AgenticDecisionLoop:
    def __init__(self):
        print("[INFO] Initializing Agentic Vision Orchestrator...")

    def evaluate_and_act(self, vision_metrics: dict):
        """
        Multi-step perception-decision-action loop:
        Visual evidence changes what the system does next.
        """
        score = vision_metrics.get("crop_health_score", 100)
        
        if score < 50:
            action = "TRIGGER_HIGH_FLOW_IRRIGATION"
            reason = f"Crop health score dropped to {score}%. Initiating targeted drip irrigation."
            actuator_signal = {"valve_id": 4, "flow_rate_lpm": 15.0, "duration_mins": 30}
        elif score < 75:
            action = "SCHEDULE_MODERATE_WATERING"
            reason = f"Moderate vegetation stress detected ({score}%). Scheduling evening watering."
            actuator_signal = {"valve_id": 2, "flow_rate_lpm": 8.0, "duration_mins": 15}
        else:
            action = "MAINTAIN_CURRENT_STATE"
            reason = f"Crops healthy at {score}%. No intervention needed."
            actuator_signal = {"valve_id": 0, "flow_rate_lpm": 0.0, "duration_mins": 0}

        return {
            "agent_action": action,
            "decision_reasoning": reason,
            "actuator_payload": actuator_signal
        }