from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)

SECRET = "suprapno"
HASH = hashlib.sha256(SECRET.encode()).hexdigest()
FLAG = "RULLZCTF{suprapno_7F29_a81C}"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>String Challenge</title>
</head>
<body>
    <h1>🔐 STRING CHALLENGE</h1>

    <p>Pecahkan string berikut:</p>

    <code>{{ hash }}</code>

    <form method="POST">
        <input name="answer" placeholder="Masukkan jawaban">
        <button type="submit">SUBMIT</button>
    </form>

    {% if result %}
        <h2>{{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        answer = request.form.get("answer", "")

        if hashlib.sha256(answer.encode()).hexdigest() == HASH:
            result = f"🎉 BENAR! Flag: {FLAG}"
        else:
            result = "❌ Salah!"

    return render_template_string(HTML, hash=HASH, result=result)

app.run(host="0.0.0.0", port=5000)
