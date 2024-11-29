# AI-for-Chronic-Pain-Mental-Support

Project Overview
This is a web-based application designed to help users track their chronic pain and mood levels over time. The app allows users to log their daily pain and mood levels, visualize trends over time, and receive helpful suggestions based on their mood.

The application is built using Flask for the backend, Plotly for data visualization, and uses in-memory storage to save the logs for now. The goal is to help individuals who suffer from chronic pain and mental health challenges by providing a way to track their symptoms and improve their well-being over time.

Features
Log Data: Allows users to log their pain and mood levels.
View Logs: Users can view all previously logged entries.
Visualize Data: Displays an interactive graph showing the pain and mood levels over time.
Edit and Delete Logs: Modify or delete previously logged data.
Filter Logs: Filter logs by a date range to analyze data over specific periods.
Suggestions Based on Mood: Offers simple, personalized suggestions based on the logged mood.
Technologies Used
Flask: Web framework for building the backend API.
Plotly: Data visualization library for creating interactive charts.
Python: Programming language used for the project.
HTML/CSS: Basic frontend to display the data.
Firestore (Optional): Can be integrated for cloud-based data storage.
Setup and Installation
1. Clone the Repository
First, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/AI-for-Chronic-Pain-Mental-Support.git
cd AI-for-Chronic-Pain-Mental-Support
2. Install Dependencies
Make sure you have Python installed (preferably version 3.8 or higher). Then, install the necessary dependencies using pip:

bash
Copy code
pip install -r requirements.txt
This will install the following dependencies:

Flask
Plotly
Firebase Admin SDK (if using Firebase)
Any other required dependencies for the project
3. Set Up Firebase (Optional)
If you plan to integrate Firebase for data storage (instead of using in-memory storage), you’ll need to:

Create a Firebase project at Firebase Console.
Download the Firebase service account key (serviceAccountKey.json) and place it in the project directory.
Update the Firebase initialization in app.py.
4. Run the Application
After setting up the environment, run the Flask application:

bash
Copy code
python app.py
This will start the Flask server at http://127.0.0.1:5000/.

5. Access the Application
Open your browser and go to the following URL:

Log Data: POST http://127.0.0.1:5000/log
View Logs: GET http://127.0.0.1:5000/logs
Visualize Data: GET http://127.0.0.1:5000/visualize
Delete Log: DELETE http://127.0.0.1:5000/delete
Edit Log: PUT http://127.0.0.1:5000/edit
Filter Logs: GET http://127.0.0.1:5000/filter
You can use cURL or tools like Postman to make requests to these endpoints.

Endpoints
POST /log: Log pain and mood levels.

Body: { "date": "YYYY-MM-DD", "pain_level": 1-10, "mood_level": 1-10 }
Response: Success message and updated logs.
GET /logs: View all logged entries.

Response: Returns all logs in JSON format.
GET /visualize: Visualize pain and mood levels over time in a graph.

Response: Displays an interactive Plotly graph.
DELETE /delete: Delete a log by date.

Body: { "date": "YYYY-MM-DD" }
Response: Success message and updated logs.
PUT /edit: Edit an existing log.

Body: { "date": "YYYY-MM-DD", "pain_level": 1-10, "mood_level": 1-10 }
Response: Success message and updated logs.
GET /filter: Filter logs by a date range.

Query Params: start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
Response: Returns filtered logs.
Future Improvements
User Authentication: Implement user authentication to allow multiple users to log their data securely.
Persistent Storage: Use a database (e.g., Firebase, SQLite, or PostgreSQL) for storing data permanently.
Machine Learning: Add machine learning features to provide personalized suggestions based on logged data.
Mobile App: Build a mobile application using frameworks like React Native or Flutter for easier data logging.
Contributing
Feel free to contribute by submitting issues or pull requests. If you have any suggestions or feature requests, please open an issue in the issues section.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Flask: A micro web framework written in Python.
Plotly: A graphing library for making interactive, online visualizations.
Firebase: A platform for building mobile and web applications.
