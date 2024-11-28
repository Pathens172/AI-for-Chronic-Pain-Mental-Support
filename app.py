from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")  # Path to your key file
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    day = request.form["day"]
    pain_level = int(request.form["pain_level"])
    mood_level = int(request.form["mood_level"])

    # Save to Firebase
    log_data = {
        "day": day,
        "pain_level": pain_level,
        "mood_level": mood_level
    }
    db.collection("pain_logs").add(log_data)
    return "Your log has been saved!"

if __name__ == "__main__":
    app.run(debug=True)
