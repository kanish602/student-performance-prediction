from flask import Flask, render_template_string, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Performance Prediction</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            text-align: center;
            padding: 30px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            max-width: 450px;
            margin: auto;
            box-shadow: 0 4px 15px #ccc;
        }
        input, select, button {
            width: 90%;
            padding: 10px;
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
        h2 { color: #2563eb; }
    </style>
</head>
<body>
<div class="container">
    <h2>Student Performance Prediction</h2>
    <p>Enter the student's academic details</p>

    <form method="POST">
        <label>Study Time (1-4)</label>
        <select name="studytime" required>
            <option value="1">1 - Less than 2 hours/week</option>
            <option value="2">2 - 2 to 5 hours/week</option>
            <option value="3">3 - 5 to 10 hours/week</option>
            <option value="4">4 - More than 10 hours/week</option>
        </select>

        <label>Number of Absences</label>
        <input type="number" name="absences"
               min="0" max="100" value="0" required>

        <label>First Period Grade (0-20)</label>
        <input type="number" name="G1"
               min="0" max="20" required>

        <label>Second Period Grade (0-20)</label>
        <input type="number" name="G2"
               min="0" max="20" required>

        <button type="submit">Predict Final Grade</button>
    </form>

    {% if prediction is not none %}
        <h3>Predicted Final Grade: {{ prediction }} / 20</h3>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        studytime = int(request.form["studytime"])
        absences = int(request.form["absences"])
        g1 = int(request.form["G1"])
        g2 = int(request.form["G2"])

        student_data = pd.DataFrame(
            [[studytime, absences, g1, g2]],
            columns=["studytime", "absences", "G1", "G2"]
        )

        result = model.predict(student_data)[0]
        prediction = round(max(0, min(20, result)), 2)

    return render_template_string(HTML, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

