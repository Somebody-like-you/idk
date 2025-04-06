// CSRF Token Fetching
const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

// Handle sending messages
document.getElementById("sendMessage").addEventListener("click", function () {
    sendMessage();
});

document.getElementById("userInput").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

async function sendMessage() {
    let input = document.getElementById("userInput").value.trim();
    if (input === "") return;

    console.log("Sending message:", input);

    let chatBox = document.getElementById("chatBox");

    // Add User Message (Right Side)
    let userMessage = document.createElement("p");
    userMessage.classList.add("user-message");
    userMessage.innerHTML = `${input}`; // ✅ Corrected string template
    chatBox.appendChild(userMessage);

    fetch("http://localhost:8000/bs/bs/", { // Ensure correct endpoint
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken  // ✅ Add CSRF Token
        },
        body: JSON.stringify({ message: input })  // ✅ Use 'message' key
    })
        .then(response => response.json())
        .then(data => {
            // Add Bot Response
            let botMessage = document.createElement("p");
            botMessage.classList.add("bot-message");
            const result = data.message
  .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>") // Bold
  .replace(/\*(.*?)\*/g, "<em>$1</em>"); // Italic

            console.log(result); 
            botMessage.innerHTML = result;

            console.log(data)
            chatBox.appendChild(botMessage);

            // Scroll to the bottom after bot response
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(error => console.error("Error:", error));

    // Clear input field
    document.getElementById("userInput").value = "";
}

// Voice Recording Variables
let inputsound = false;
let mediaRecorder;
let audioChunks = [];
let stream;

// Start Recording Function
async function startRecording() {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    audioChunks = [];  // Reset chunks each time recording starts

    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
    };

    mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
        const formData = new FormData();
        formData.append("audio", audioBlob, "recording.webm");

        await fetch("http://localhost:8000/upload/audio/", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": csrftoken  // ✅ Correctly fetch CSRF token
            }
        })
            .then(response => response.json())
            .then(data => console.log("Server Response:", data))
            .catch(error => console.error("Upload Error:", error));
    };

    mediaRecorder.start();
}

// Toggle Recording on Button Click
document.getElementById("voiceInput").addEventListener("click", () => {
    if (!inputsound) {
        startRecording();
        console.log("Recording started");
        inputsound = true;
    } else {
        if (mediaRecorder) {
            mediaRecorder.stop();
            console.log("Recording stopped");
        }

        if (stream) {
            stream.getTracks().forEach(track => track.stop());  // ✅ Stop all tracks
            stream = null;  // ✅ Reset stream reference
        }

        inputsound = false;
    }
});
