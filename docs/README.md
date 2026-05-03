# Election Navigator Assistant 🗳️

An AI-powered assistant designed to help users understand the election process in India in an interactive, simple, and personalized way.

## 🌟 Features

- **Chat Assistant**: Ask any questions about the Indian election process (registration, voting, results).
- **Guided Flow**: Personalize the experience by providing your age, state, and whether you are a first-time voter.
- **Dynamic Timeline**: Visually tracks the election stages based on your current inquiry.
- **Multilingual Support**: Supports English, Hindi, and Marathi responses using AI.
- **Modern UI**: Clean, responsive, and accessible interface.

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3 (Custom Variables, Flexbox, Grid)
- Vanilla JavaScript

**Backend:**
- Python 3.9+
- FastAPI
- Uvicorn

**AI Integration:**
- Google Gemini API (`gemini-1.5-flash`)

## 📂 Project Structure

```text
election-navigator/
├── backend/
│   ├── app.py                 # FastAPI application entry point
│   ├── routes/
│   │   └── api.py             # API endpoints
│   ├── services/
│   │   └── ai_service.py      # Gemini API integration
│   ├── models/
│   │   └── models.py          # Pydantic data models
│   ├── .env.example           # Example environment variables
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── index.html             # Main user interface
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic and API calls
└── docs/
    └── README.md              # Project documentation
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

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
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
   uvicorn app:app --reload
   ```
   The backend will start on `http://localhost:8000`.

### 2. Frontend Setup

1. Open a new terminal.
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
3. Open `index.html` in your browser. 
   - You can simply double-click the file, or serve it using a local web server:
     ```bash
     python -m http.server 3000
     ```
     Then open `http://localhost:3000` in your browser.

## 💡 How to Use

1. Ensure the FastAPI backend is running.
2. Open the frontend in your browser.
3. Fill out your profile (Age, State, First-time voter) on the left side.
4. Select your preferred language from the top right dropdown.
5. Start typing your questions in the chat box! Example: *"How do I register to vote?"*

## 🔒 Security Notes
- **API Keys**: Never commit your `.env` file containing actual API keys to version control. The `.gitignore` should include `.env`.
- **Validation**: User inputs are validated on the backend using Pydantic models.
