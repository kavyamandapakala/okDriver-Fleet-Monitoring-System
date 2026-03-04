from fastapi import FastAPI, WebSocket
import asyncio
import random

app = FastAPI()

# [cite_start]This fulfills the requirement for a real-time data sync [cite: 13]
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # [cite_start]1. Generate dummy events every 2 seconds [cite: 16]
        speed = random.randint(60, 100)
        
        # [cite_start]2. Logic: Speed over 80 triggers a Red Alert [cite: 22]
        data = {
            "speed": speed,
            "event": "RED ALERT" if speed > 80 else "Normal",
            "risk_score": 5 if speed > 80 else 1,
            "driver": "Kavya_Driver_01"
        }
        
        # [cite_start]3. Push data to the dashboard instantly [cite: 10, 17]
        await websocket.send_json(data)
        await asyncio.sleep(2)