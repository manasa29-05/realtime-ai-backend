import os
from supabase import create_client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# ---------- EVENTS ----------

def save_event(session_id, event_type, content):
    supabase.table("events").insert({
        "session_id": session_id,
        "event_type": event_type,
        "content": content
    }).execute()

def get_session_events(session_id):
    res = supabase.table("events") \
        .select("event_type, content") \
        .eq("session_id", session_id) \
        .order("id") \
        .execute()
    return res.data

# ---------- SESSIONS ----------

def save_session_start(session_id):
    # avoid duplicate session error
    existing = supabase.table("sessions") \
        .select("session_id") \
        .eq("session_id", session_id) \
        .execute()

    if not existing.data:
        supabase.table("sessions").insert({
            "session_id": session_id,
            "start_time": datetime.utcnow().isoformat()
        }).execute()

def save_session_summary(session_id, summary):
    supabase.table("sessions").update({
        "summary": summary
    }).eq("session_id", session_id).execute()
