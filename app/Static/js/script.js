// Function to handle sending chat messages
function sendMessage() {
    const input = document.getElementById('chat-input').value;
    const chatWindow = document.getElementById('chat-messages');
    
    // Display user's message
    const userMessage = document.createElement('div');
    userMessage.textContent = "You: " + input;
    chatWindow.appendChild(userMessage);

    // Send the message to the backend (using fetch for AJAX request)
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({message: input})
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        const botMessage = document.createElement('div');
        botMessage.textContent = "Bot: " + data.response;
        chatWindow.appendChild(botMessage);
    });

    document.getElementById('chat-input').value = ''; // Clear input field
}

// Function to handle form submission (optional, if you want to interact with the backend)
document.getElementById('insuranceForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const formData = new FormData(this);

    fetch('http://127.0.0.1:5000/submit-form', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert("Form submitted successfully!");
    })
    .catch(error => {
        alert("Error submitting the form");
        console.error("Form submission error:", error);
    });
});
