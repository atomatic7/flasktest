// static/script.js
document.getElementById("fetchDataButton").addEventListener("click", async () => {
    try {
        const response = await fetch("/api/data");
        const data = await response.json();
        document.getElementById("apiResponse").innerText = data.message;
    } catch (error) {
        console.error("Error fetching data:", error);
        document.getElementById("apiResponse").innerText = "Error fetching data";
    }
});
