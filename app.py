from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# in-memory storage (برای دمو) — در دنیای واقعی DB جایگزین می‌شود
tasks = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({"title": title})
    return redirect(url_for("home"))

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
