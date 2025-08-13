const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
app.use(bodyParser.json());
app.use(cors());

// Serve the HTML file
app.use(express.static("public"));

// Handle POST requests to /ask
app.post("/ask", (req, res) => {
    const { prompt } = req.body;
    if (!prompt) {
        return res.json({ error: "Please provide a prompt." });
    }
    // Add your logic here to process the prompt
    const response = `You asked: "${prompt}". Here’s a helpful tip: Always check your console logs for errors!`;
    res.json({ response });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
