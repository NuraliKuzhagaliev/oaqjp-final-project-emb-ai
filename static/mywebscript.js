"use strict";

document.getElementById("emotion-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const text = document.getElementById("textToAnalyze").value;
    const output = document.getElementById("system_response");
    const button = document.getElementById("analyze-button");
    button.disabled = true;
    output.textContent = "Analyzing...";
    try {
        const response = await fetch(
            "/emotionDetector?" + new URLSearchParams({textToAnalyze: text})
        );
        output.textContent = await response.text();
    } catch (_error) {
        output.textContent = "Cannot reach the server. Please try again.";
    } finally {
        button.disabled = false;
    }
});
