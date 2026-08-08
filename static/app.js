const chatContainer = document.getElementById("chat-container");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const newChatButton = document.getElementById("new-chat-button");
const pdfInput = document.getElementById("pdf-input");
const uploadButton = document.getElementById("upload-button");

// Conversation history
let history = [];

function addMessage(text, role) {
    const message = document.createElement("div");
    message.classList.add("message", `${role}-message`);

    const avatar = document.createElement("div");
    avatar.classList.add("avatar");
    avatar.textContent = role === "user" ? "You" : "AI";

    const content = document.createElement("div");
    content.classList.add("message-content");
    content.textContent = text;

    message.appendChild(avatar);
    message.appendChild(content);

    chatContainer.appendChild(message);
    chatContainer.scrollTop = chatContainer.scrollHeight;

    return content;
}

async function sendMessage() {
    const message = messageInput.value.trim();

    if (!message) return;

    addMessage(message, "user");

    messageInput.value = "";
    sendButton.disabled = true;

    const loadingMessage = addMessage("Thinking...", "assistant");

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message: message,
                history: history,
            }),
        });

        if (!response.ok) {
            const errData = await response.json().catch(() => null);
            throw new Error(errData?.detail || "Failed to generate response");
        }

        const data = await response.json();

        loadingMessage.textContent = data.response;

        // Save updated conversation history
        history = data.history;

    } catch (error) {
        loadingMessage.textContent =
            "Something went wrong. " + error.message;
    } finally {
        sendButton.disabled = false;
        messageInput.focus();
    }
}
async function uploadPDF() {

    if (!pdfInput.files.length) {

        alert("Choose a PDF.");

        return;

    }

    const formData = new FormData();

    formData.append(
        "file",
        pdfInput.files[0]
    );

    const response = await fetch(
        "/api/storage/uploads",
        {
            method: "POST",

            body: formData
        }
    );

    const data = await response.json();

    alert(`Uploaded! Characters: ${data.characters}`);

}

sendButton.addEventListener("click", sendMessage);

messageInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

newChatButton.addEventListener("click", () => {
    chatContainer.innerHTML = "";
    history = [];
    addMessage("Hello! How can I assist you today?", "assistant");
    messageInput.focus();
});

uploadButton.addEventListener(
    "click",
    uploadPDF
);

// Initial message
addMessage("Hello! How can I assist you today?", "assistant");