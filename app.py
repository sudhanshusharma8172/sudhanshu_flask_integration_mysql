from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import get_db_connection

app = Flask(__name__)
app.secret_key = "secret123"

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Show Events
@app.route("/events")
def events():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events")
    data = cursor.fetchall()
    conn.close()
    return render_template("events.html", events=data)

# Register for Event
@app.route("/register/<int:event_id>", methods=["GET", "POST"])
def register(event_id):
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO participants (event_id, name, email) VALUES (%s, %s, %s)", 
                       (event_id, name, email))
        conn.commit()
        conn.close()

        flash("Registration successful!", "success")
        return redirect(url_for("events"))
    return render_template("register.html", event_id=event_id)

# Show Participants
@app.route("/participant/<int:event_id>")
def participant(event_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM participant WHERE event_id=%s", (event_id,))
    data = cursor.fetchall()
    conn.close()
    return render_template("participant.html", participant=data)

if __name__ == "__main__":
    app.run(debug=True)