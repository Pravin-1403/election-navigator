const chatBox = document.getElementById('chatBox');
const chatForm = document.getElementById('chatForm');
const queryInput = document.getElementById('queryInput');
const sendBtn = document.getElementById('sendBtn');

// Profile Elements
const ageInput = document.getElementById('age');
const stateSelect = document.getElementById('state');
const firstTimeCheckbox = document.getElementById('firstTimeVoter');
const languageSelector = document.getElementById('languageSelector');

// API URL
const API_URL = 'http://localhost:8000/api/ask';

let chatHistory = [];

// Add a message to the chat box
function addMessage(text, sender, isError = false) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', sender);
    
    // Add Avatar
    const avatar = document.createElement('div');
    avatar.classList.add('avatar');
    avatar.textContent = sender === 'ai' ? '🤖' : '👤';
    
    const textDiv = document.createElement('div');
    textDiv.classList.add('text-content');
    
    // Simple markdown parsing for bold text from Gemini
    let formattedText = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    formattedText = formattedText.replace(/\n/g, '<br>');

    textDiv.innerHTML = formattedText;
    
    msgDiv.appendChild(avatar);
    msgDiv.appendChild(textDiv);
    
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Save to history if it's not an error message
    if (!isError && text !== 'Thinking...') {
        chatHistory.push({
            role: sender === 'ai' ? 'model' : 'user',
            content: text
        });
    }
}

// Get user profile data
function getUserProfile() {
    return {
        age: ageInput.value ? parseInt(ageInput.value) : null,
        state: stateSelect.value || null,
        is_first_time_voter: firstTimeCheckbox.checked,
        language: languageSelector.value
    };
}

// Update Timeline visually based on keywords (simple mock logic)
function updateTimeline(query) {
    const lowerQuery = query.toLowerCase();
    const steps = document.querySelectorAll('.timeline-step');
    
    steps.forEach(step => step.classList.remove('active'));

    if (lowerQuery.includes('register') || lowerQuery.includes('card') || lowerQuery.includes('voter id')) {
        steps[0].classList.add('active');
    } else if (lowerQuery.includes('campaign') || lowerQuery.includes('party')) {
        steps[1].classList.add('active');
    } else if (lowerQuery.includes('vote') || lowerQuery.includes('booth') || lowerQuery.includes('evm')) {
        steps[2].classList.add('active');
    } else if (lowerQuery.includes('result') || lowerQuery.includes('win')) {
        steps[3].classList.add('active');
    } else {
        // Keep the last active or default to 0
        steps[0].classList.add('active');
    }
}

function showTypingIndicator() {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', 'ai', 'typing-indicator-wrapper');
    msgDiv.id = 'typingIndicator';
    
    const avatar = document.createElement('div');
    avatar.classList.add('avatar');
    avatar.textContent = '🤖';
    
    const typing = document.createElement('div');
    typing.classList.add('typing-indicator');
    typing.innerHTML = '<span></span><span></span><span></span>';
    
    msgDiv.appendChild(avatar);
    msgDiv.appendChild(typing);
    
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) {
        indicator.remove();
    }
}

// Handle form submission
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = queryInput.value.trim();
    if (!query) return;

    // Add user message
    addMessage(query, 'user');
    queryInput.value = '';
    sendBtn.disabled = true;

    // Update timeline based on user query
    updateTimeline(query);

    // Show loading state
    showTypingIndicator();

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                query: query,
                user_info: getUserProfile(),
                history: chatHistory.slice(0, -1) // Send all history except the latest query which is sent as 'query'
            })
        });

        const data = await response.json();
        
        removeTypingIndicator();

        if (response.ok) {
            addMessage(data.response, 'ai');
        } else {
            addMessage('Sorry, I encountered an error. Please ensure the backend is running and the API key is configured.', 'ai', true);
            console.error('API Error:', data);
        }
    } catch (error) {
        removeTypingIndicator();
        addMessage('Failed to connect to the server. Make sure the FastAPI backend is running on http://localhost:8000', 'ai', true);
        console.error('Fetch Error:', error);
    } finally {
        sendBtn.disabled = false;
        queryInput.focus();
    }
});
