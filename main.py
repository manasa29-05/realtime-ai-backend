from fastapi import FastAPI, WebSocket
from app.websocket import websocket_endpoint

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.websocket("/ws/session/{session_id}")
async def ws_endpoint(websocket: WebSocket, session_id: str):
    await websocket_endpoint(websocket, session_id)
