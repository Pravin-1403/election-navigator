# Election Navigator Assistant 🗳️

An AI-powered, interactive chat assistant designed to help users understand the election process in India in a personalized, simple, and conversational way.

## 🌟 Features

- **Conversational AI Chat**: A fully interactive chat system that remembers your conversation history and provides step-by-step guidance rather than overwhelming text dumps.
- **Guided Profile Flow**: Personalize the experience by providing your Age, State, and First-time voter status. The AI automatically adapts its answers to your profile!
- **Interactive Timeline**: Clickable timeline tracking the election stages (Registration, Campaign, Voting, Results). Clicking a step instantly asks the AI for guidance on that specific phase.
- **Multilingual Support**: Supports English, Hindi, and Marathi. The AI dynamically translates its responses based on your selection.
- **Modern UI/UX**: Clean interface featuring typing indicators, avatars, responsive design, and smooth auto-scrolling chat bubbles.
- **Robust Backend**: Built on FastAPI with strict input validation using Pydantic models.

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3 (Custom Variables, Flexbox, Animations)
- Vanilla JavaScript (Fetch API, DOM manipulation)

**Backend:**
- Python 3.9+
- FastAPI & Uvicorn
- Pydantic (Data validation)
- Google GenAI SDK

**AI Integration:**
- Google Gemini API (`gemini-2.5-flash`) with advanced `ChatSession` history tracking.

## 📂 Project Structure

```text
election-navigator/
├── backend/
│   ├── app.py                 # FastAPI application entry point
│   ├── routes/
│   │   └── api.py             # API endpoints and routing
│   ├── services/
│   │   └── ai_service.py      # Gemini API configuration and prompt logic
│   ├── models/
│   │   └── models.py          # Pydantic data models (ChatRequest, Message)
│   ├── core/
│   │   └── config.py          # Environment variables and app settings
│   ├── .env.example           # Example environment variables
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── index.html             # Main user interface
│   ├── style.css              # Styling and animations
│   └── script.js              # Frontend logic and API calls
└── README.md                  # Project documentation
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.9 or higher
- A Google Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/))

### 1. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure Environment Variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and add your Gemini API Key:
     ```env
     GEMINI_API_KEY=your_actual_api_key_here
     ```

5. Run the Backend Server:
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```
   The backend will start on `http://localhost:8000`.

### 2. Frontend Setup

1. Open a new terminal window.
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
3. Start a local web server:
   ```bash
   python -m http.server 3000
   ```
4. Open `http://localhost:3000` in your web browser.

## 💡 How to Use

1. Ensure both the FastAPI backend and Python HTTP server are running.
2. Open the frontend in your browser.
3. Fill out your profile (Age, State, First-time voter) on the left panel.
4. Select your preferred language from the top right dropdown.
5. Start typing your questions in the chat box or click on the interactive timeline to get started! Example: *"How do I register to vote?"*

## 🔒 Security Notes
- **API Keys**: Never commit your `.env` file to version control. The `.gitignore` file automatically excludes it.
- **Validation**: All user inputs (profile data and chat history) are strictly validated on the backend using Pydantic fields before processing.
