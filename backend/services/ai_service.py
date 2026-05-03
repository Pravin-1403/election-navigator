import google.generativeai as genai
from core.config import settings
import logging

# Set up simple logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Gemini API
if settings.GEMINI_API_KEY and settings.GEMINI_API_KEY != "your_google_gemini_api_key_here":
    genai.configure(api_key=settings.GEMINI_API_KEY)
    logger.info("Gemini API Key configured.")
else:
    logger.warning("Gemini API Key is not set or is using the placeholder.")

def _get_system_instruction(user_info: dict) -> str:
    """Helper function to build the system instruction based on user context."""
    context = []
    if user_info:
        if user_info.get("age"):
            context.append(f"Age: {user_info.get('age')}")
        if user_info.get("state"):
            context.append(f"State: {user_info.get('state')}")
        if user_info.get("is_first_time_voter") is not None:
            voter_status = "Yes" if user_info.get("is_first_time_voter") else "No"
            context.append(f"First-time voter: {voter_status}")
        if user_info.get("language"):
            context.append(f"Preferred Language: {user_info.get('language')}")

    context_str = ", ".join(context)
    
    return f"""
    You are 'Election Navigator', a highly interactive, friendly, and expert AI assistant that helps users understand the Indian election process.
    
    CRITICAL INSTRUCTIONS FOR YOUR BEHAVIOR:
    1. Be conversational and engaging. Do not just output long paragraphs or essays.
    2. Guide the user step-by-step. If they ask a broad question, give a concise summary and ask a follow-up question to help narrow down what they need.
    3. Keep responses structured and easy to read using short sentences or bullet points.
    
    User Profile Context: {context_str if context_str else 'Not provided'}
    
    - Always tailor your responses based on their state and if they are a first-time voter (if provided).
    - If the user's preferred language is not English, you MUST translate your entire response into that language (e.g., Hindi or Marathi).
    - Remain neutral and factual. Do not provide political opinions or endorse candidates.
    """

def get_mock_response(query: str, history: list) -> str:
    """Returns a mock response for UI testing when the API key is not present."""
    lower_query = query.lower()
    if "register" in lower_query or "card" in lower_query:
        return "**(Mock AI Response)** To register to vote in India, you need to be an Indian citizen, 18 years of age or older. You can apply online through the Voter Portal. Do you want me to explain how to fill out Form 6 online?"
    elif "campaign" in lower_query:
        return "**(Mock AI Response)** Election campaigns involve rallies and manifestos. The Election Commission sets rules known as the Model Code of Conduct. Would you like to know what is allowed during campaigns?"
    elif "vote" in lower_query:
        return "**(Mock AI Response)** On voting day, you go to your polling booth with your Voter ID (EPIC) and cast your vote on an EVM. Have you ever seen an EVM before?"
    elif "result" in lower_query:
        return "**(Mock AI Response)** Election results are declared after counting votes from the EVMs. The candidate with the most votes wins. Do you want to know how counting is supervised?"
    else:
        return f"**(Mock AI Response)** You asked: '{query}'. In the real application, I would be engaging in a conversation with you!"

def generate_election_response(query: str, user_info: dict, history_dicts: list = None) -> str:
    """Generates a response using the Gemini API via a ChatSession."""
    if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == "your_google_gemini_api_key_here":
        logger.info("Using mock response because API key is missing.")
        return get_mock_response(query, history_dicts or [])

    system_instruction = _get_system_instruction(user_info)

    # Format history for Gemini SDK
    # SDK expects: [{"role": "user", "parts": ["..."]}, {"role": "model", "parts": ["..."]}]
    formatted_history = []
    if history_dicts:
        for msg in history_dicts:
            role = "model" if msg.get("role") in ["ai", "model"] else "user"
            formatted_history.append({"role": role, "parts": [msg.get("content", "")]})

    try:
        model = genai.GenerativeModel('gemini-2.5-flash', system_instruction=system_instruction)
        chat = model.start_chat(history=formatted_history)
        response = chat.send_message(query)
        return response.text
    except Exception as e:
        logger.error(f"Error calling Gemini API: {str(e)}")
        raise RuntimeError(f"Failed to generate response from AI service: {str(e)}")
