Realtime AI Backend (WebSockets + Supabase)
This project implements a real-time conversational AI backend using FastAPI, WebSockets, and Supabase. It demonstrates low-latency bi-directional communication, session-based state management, event logging, and post-session processing.
The backend accepts user messages over WebSockets, streams AI responses in real time, persists all session data in Supabase Postgres, and generates a session summary after the client disconnects.

Tech Stack:
Python
FastAPI
WebSockets
Supabase (Postgres)
OpenAI API (or mock LLM if quota not available)

Project Structure:
realtime-ai-backend/
app/
main.py – FastAPI app entry point
websocket.py – WebSocket session handling
database.py – Supabase database operations
llm.py – LLM streaming and summary generation (or mock)
post_session.py – Post-session summary logic
frontend/
index.html – simple WebSocket test UI
.env – environment variables
requirements.txt – dependencies

Setup Instructions:
Create a virtual environment and activate it
Install dependencies using: pip install -r requirements.txt
Create a Supabase project and note the Project URL and Anon Key
Create the required tables in Supabase using the SQL below
Create a .env file and add your keys
Run the server using: uvicorn app.main:app --reload

Supabase Database Schema:
CREATE TABLE sessions (
session_id TEXT PRIMARY KEY,
start_time TIMESTAMP DEFAULT NOW(),
end_time TIMESTAMP,
summary TEXT
);

CREATE TABLE events (
id SERIAL PRIMARY KEY,
session_id TEXT,
event_type TEXT,
content TEXT,
timestamp TIMESTAMP DEFAULT NOW()
);

Environment Variables (.env):
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
OPENAI_API_KEY=your_openai_api_key

WebSocket Endpoint:
ws://127.0.0.1:8000/ws/session/{session_id}

How It Works:
When a client connects to the WebSocket endpoint, a new session is started and stored in the database. 
Each user message and AI response is saved as an event. AI responses are streamed token-by-token over the WebSocket connection. 
When the client disconnects, the backend fetches the full conversation history, generates a concise session summary using an LLM (or mock logic), and stores the summary in the session record.

Design Choices:
FastAPI was chosen for its async support and WebSocket integration. 
Supabase provides a simple hosted Postgres database with a Python client. 
The system separates session metadata and event logs to allow detailed conversation tracking and post-session analysis. 
A simple frontend is included only for testing WebSocket connectivity.

