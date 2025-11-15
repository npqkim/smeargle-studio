document.getElementById("submitBtn").addEventListener("click", async () => {
    const audioFile = document.getElementById("audioInput").files[0];
    const dropdownGenre = document.getElementById("genreSelect").value;
    const customGenre = document.getElementById("genreCustom").value;

    if (!audioFile) {
        alert("Please upload an audio file!");
        return;
    }

    // Use custom if filled, else dropdown
    const finalGenre = customGenre !== "" ? customGenre : dropdownGenre;

    const formData = new FormData();
    formData.append("audio", audioFile);
    formData.append("genre", finalGenre);

    const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("output").innerHTML = `
        <h3>Prompt:</h3>
        <pre>${data.prompt}</pre>

        <h3>Generated Image:</h3>
        <img src="${data.image_url}" />
    `;
});
