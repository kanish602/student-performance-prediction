
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Performance Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            text-align: center;
            padding: 40px;
        }
        .card {
            background: white;
            max-width: 450px;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 15px #ccd;
        }
        input, button {
            width: 90%;
            padding: 12px;
            margin: 10px;
            box-sizing: border-box;
        }
        button {
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        .result { color: #166534; font-weight: bold; }
    </style>
</head>
<body>
<div class="card">
    <h1>Student Performance Predictor</h1>
    <p>Enter your academic details</p>
    <form method="POST">
        <input type="number" name="hours" min="0" max="24"
               step="0.5" placeholder="Daily study hours" required>
        <input type="number" name="attendance" min="0" max="100"
               placeholder="Attendance (%)" required>
        <input type="number" name="previous" min="0" max="100"
               placeholder="Previous marks (%)" required>
        <button type="submit">Predict Performance</button>
    </form>
    {% if result is not none %}
        <p class="result">Estimated performance: {{ result }}%</p>
        <p>This is a simple demo estimate, not an ML prediction yet.</p>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        previous = float(request.form["previous"])

        if 0 <= hours <= 24 and 0 <= attendance <= 100 and 0 <= previous <= 100:
            result = round(
                0.4 * previous +
                0.3 * attendance +
                0.3 * (hours / 24 * 100), 2
            )

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
