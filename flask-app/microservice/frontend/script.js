document.getElementById("dataForm").addEventListener("submit", async function (e) {
    e.preventDefault();  // stop default form submission

    const name = document.getElementById("name").value;
    console.log("JS loaded");


    try {
        const response = await fetch("http://localhost:5000/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name })
        });

        const data = await response.json();

        if (response.ok) {
            // Redirect to success page
            window.location.href = "success.html";
        } else {
            document.getElementById("error").innerText = data.error;
        }

    } catch (err) {
        document.getElementById("error").innerText = "Server error. Check backend.";
    }
});
