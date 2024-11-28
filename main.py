print("Welcome to AI Chronic Pain Tracker!")

# Function to record pain and mood
def record_pain_mood():
    day = input("What day is it? ")
    pain_level = int(input("On a scale of 1-10, what is your pain level? "))
    mood_level = int(input("On a scale of 1-10, what is your mood? "))
    print(f"Recorded: Day: {day}, Pain: {pain_level}, Mood: {mood_level}")

# Call the function
record_pain_mood()

# Function to record pain and mood
def record_pain_mood():
    day = input("What day is it? ")
    pain_level = int(input("On a scale of 1-10, what is your pain level? "))
    mood_level = int(input("On a scale of 1-10, what is your mood? "))

    # Save to a file
    with open("pain_mood_logs.txt", "a") as file:
        file.write(f"Day: {day}, Pain: {pain_level}, Mood: {mood_level}\n")
    print("Your log has been saved!")

# Call the function
record_pain_mood()

# Function to record pain and mood
def record_pain_mood():
    day = input("What day is it? ")
    pain_level = int(input("On a scale of 1-10, what is your pain level? "))
    mood_level = int(input("On a scale of 1-10, what is your mood? "))

    # Save to a file
    with open("pain_mood_logs.txt", "a") as file:
        file.write(f"Day: {day}, Pain: {pain_level}, Mood: {mood_level}\n")
    print("Your log has been saved!")

    # AI suggestion
    if mood_level <= 5:
        print("Suggestion: Try taking a walk or meditating!")
    else:
        print("Suggestion: Keep up the great mood!")

# Call the function
record_pain_mood()

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")  # Path to your key file
firebase_admin.initialize_app(cred)

db = firestore.client()  # Firestore database client
