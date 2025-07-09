// static/script.js

document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatWindow = document.getElementById('chat-window');
    const themeToggle = document.getElementById('checkbox');
    const body = document.body;

    // Load theme preference from localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.classList.add(savedTheme);
        if (savedTheme === 'dark-mode') {
            themeToggle.checked = true;
        }
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // Check system preference if no theme saved
        body.classList.add('dark-mode');
        themeToggle.checked = true;
    }


    // Function to append messages to the chat window
    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        if (sender === 'user') {
            messageDiv.classList.add('user-message');
            messageDiv.innerHTML = `<p>${message}</p>`;
        } else {
            messageDiv.classList.add('assistant-message');
            messageDiv.innerHTML = `<p>${message}</p>`;
        }
        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight; // Scroll to bottom
    }

    // Handle form submission
    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = userInput.value.trim();
        if (message === '') return;

        appendMessage('user', message);
        userInput.value = ''; // Clear input

        // Display a "typing" indicator or placeholder while waiting for response
        const typingIndicator = document.createElement('div');
        typingIndicator.classList.add('message', 'assistant-message');
        typingIndicator.innerHTML = '<p>Assistant is typing...</p>';
        chatWindow.appendChild(typingIndicator);
        chatWindow.scrollTop = chatWindow.scrollHeight;

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            });

            const data = await response.json();

            // Remove typing indicator
            chatWindow.removeChild(typingIndicator);

            if (response.ok) {
                appendMessage('assistant', data.response);
            } else {
                appendMessage('assistant', `Error: ${data.response || 'Something went wrong.'}`);
            }
        } catch (error) {
            console.error('Error sending message:', error);
            // Remove typing indicator and show error
            chatWindow.removeChild(typingIndicator);
            appendMessage('assistant', 'Sorry, there was an issue connecting to the AI. Please try again later.');
        }
    });

    // Handle theme toggle
    themeToggle.addEventListener('change', () => {
        if (themeToggle.checked) {
            body.classList.add('dark-mode');
            body.classList.remove('light-mode');
            localStorage.setItem('theme', 'dark-mode');
        } else {
            body.classList.add('light-mode');
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light-mode');
        }
    });
});