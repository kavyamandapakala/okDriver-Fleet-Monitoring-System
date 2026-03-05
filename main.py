from fastapi import FastAPI, WebSocket
import asyncio
import random

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        
        speed = random.randint(60, 100)
        
        
        data = {
            "speed": speed,
            "event": "RED ALERT" if speed > 80 else "Normal",
            "risk_score": 5 if speed > 80 else 1,
            "driver": "Kavya_Driver_01"
        }
        
        
        await websocket.send_json(data)

        await asyncio.sleep(2)
