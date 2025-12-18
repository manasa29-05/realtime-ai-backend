from fastapi import WebSocket, WebSocketDisconnect
from app.database import save_event, save_session_start
from app.post_session import handle_post_session


async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    print(f"Client connected: {session_id}")

    try:
        save_session_start(session_id)

        while True:
            data = await websocket.receive_text()
            print("Received:", data)

            save_event(session_id, "user_message", data)

            response = f"AI: {data}"
            await websocket.send_text(response)

            save_event(session_id, "ai_response", response)

    except WebSocketDisconnect:
        print(f"Client disconnected: {session_id}")
        await handle_post_session(session_id)

