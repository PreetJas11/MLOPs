from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; }
        h1   { color: #1a237e; }
        input { padding: 8px; font-size: 16px; width: 100px; }
        button { padding: 8px 20px; background: #1565c0; color: white; 
                 border: none; font-size: 16px; cursor: pointer; margin-left: 10px; }
        table { border-collapse: collapse; margin-top: 20px; width: 100%; }
        th    { background: #1a237e; color: white; padding: 10px; }
        td    { padding: 8px 14px; border: 1px solid #ddd; text-align: center; }
        tr:nth-child(even) { background: #e3f2fd; }
    </style>
</head>
<body>
    <h1>Multiplication Table</h1>
    <form method="POST">
        <input type="number" name="number" placeholder="Enter number" value="{{ number }}">
        <button type="submit">Generate</button>
    </form>

    {% if number %}
    <h3>Table of {{ number }}</h3>
    <table>
        <tr><th>Expression</th><th>Result</th></tr>
        {% for i in range(1, 11) %}
        <tr>
            <td>{{ number }} x {{ i }}</td>
            <td>{{ number * i }}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    number = None
    if request.method == "POST":
        number = int(request.form["number"])
    return render_template_string(HTML, number=number)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)