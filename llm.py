# app/llm.py

async def generate_summary(conversation: str) -> str:
    """
    Mock summary generator (NO OpenAI call)
    """
    return f"""
Session Summary:
- Total messages exchanged: {conversation.count('User:')}
- Conversation was successful
- User interacted normally with the assistant
"""
