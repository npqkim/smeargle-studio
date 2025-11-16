// Listen for file upload
document.getElementById("file-upload").addEventListener("change", (event) => {
    const audioFile = event.target.files[0];
    if (audioFile) {
        // File was selected - change button color
        document.getElementById("submitBtn").style.background = "linear-gradient(45deg, #57c785)";
        document.getElementById("submitBtn").style.boxShadow = "0 5px 15px rgba(87, 199, 133, 0.5)";
    } else {
        // No file - revert to original color
        document.getElementById("submitBtn").style.background = "linear-gradient(45deg, rgba(42, 123, 155, 1))";
        document.getElementById("submitBtn").style.boxShadow = "0 5px 15px rgba(0,0,0,0.2)";
    }
});

document.getElementById("submitBtn").addEventListener("click", async () => {
    const audioFile = document.getElementById("file-upload").files[0];
    const genre = document.getElementById("genreCustom").value;

    if (!audioFile) {
        alert("Please upload an audio file!");
        return;
    }

    if (!genre) {
        alert("Please enter a genre!");
        return;
    }

    const formData = new FormData();
    formData.append("audio", audioFile);
    formData.append("genre", genre);  // ✔ sends genre to backend

    try {
        // Change button text to show it's processing
        document.getElementById("submitBtn").innerText = "Generating...";
        document.getElementById("submitBtn").disabled = true;

        const response = await fetch("http://127.0.0.1:5001/generate_art", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            alert(`Error from backend: ${response.status}`);
            document.getElementById("submitBtn").innerText = "Generate";
            document.getElementById("submitBtn").disabled = false;
            return;
        }

        const data = await response.json();

        // store URL for result page
        localStorage.setItem("generatedImageUrl", data.image_url);

        // redirect to results
        window.location.href = "result.html";
    } catch (error) {
        alert(`Request failed: ${error.message}`);
        console.error(error);
    }
});