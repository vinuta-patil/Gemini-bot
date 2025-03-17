function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let responseBox = document.getElementById("response-box");

    if (userInput.trim() === "") {
        responseBox.value = "Please enter a prompt.";
        return;
    }

    responseBox.value = "Generating response...";

    // Send message to Flask API
    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        responseBox.value = data.response;
    })
    .catch(error => {
        console.error("Fetch error:", error);
        responseBox.value = "Error: Failed to fetch response.";
    });
}

// Function to clear chat
function clearChat() {
    document.getElementById("user-input").value = "";
    document.getElementById("response-box").value = "";
}
