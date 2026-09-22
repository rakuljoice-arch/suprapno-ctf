cd ~/suprapno-ctf

cat > app.py <<'PY'
from flask import Flask, request, render_template_string
import hashlib
import os

app = Flask(__name__)

SECRET = os.environ["SECRET"]
HASH = hashlib.sha256(SECRET.encode()).hexdigest()
FLAG = os.environ["FLAG"]

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
PY

printf "flask\ngunicorn\n" > requirements.txt

git add app.py requirements.txt
git commit -m "Secure challenge secrets"
git push
