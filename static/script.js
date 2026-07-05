async function sendMessage() {

    let input = document.getElementById("userInput");
    let message = input.value.trim();


    if (message === "") return;
    

    // Add question to Recent Chats
    let history = document.getElementById("history");

    history.innerHTML += `
        <div class="history-item">
            ${message.substring(0, 25)}
        </div>
    `;

    let chatbox = document.getElementById("chatbox");

    // User message
    chatbox.innerHTML += `
        <div class="user">
            ${message}
        </div>
    `;

    input.value = "";

    chatbox.scrollTop = chatbox.scrollHeight;

    try {

        let response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        let data = await response.json();

        let html = marked.parse(data.reply);

        // Bot message
        chatbox.innerHTML += `
            <div class="bot">
                ${html}
            </div>
        `;

        chatbox.scrollTop = chatbox.scrollHeight;

    } catch (error) {

        chatbox.innerHTML += `
            <div class="bot">
                Error connecting to server.
            </div>
        `;
    }
}


// Send message when Enter is pressed
document.getElementById("userInput").addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});


// New Chat button
function newChat() {

    document.getElementById("chatbox").innerHTML = "";

}