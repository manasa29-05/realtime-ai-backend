# app/post_session.py

from app.database import get_session_events, save_session_summary
from app.llm import generate_summary

async def handle_post_session(session_id: str):
    events = get_session_events(session_id)

    conversation = ""
    for e in events:
        if e["event_type"] == "user_message":
            conversation += f"User: {e['content']}\n"
        elif e["event_type"] == "ai_response":
            conversation += f"AI: {e['content']}\n"

    summary = await generate_summary(conversation)
    save_session_summary(session_id, summary)
