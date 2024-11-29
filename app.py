from flask import Flask, request, jsonify, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

# In-memory data storage
logs = []

# Endpoint to log data
@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    
    # Validate incoming data
    if not data or not all(key in data for key in ("date", "pain_level", "mood_level")):
        return jsonify({"error": "Invalid data. Fields 'date', 'pain_level', and 'mood_level' are required."}), 400
    
    # Append to logs
    logs.append(data)
    return jsonify({"message": "Data logged successfully!", "logs": logs})

# Endpoint to get all logs
@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify({"logs": logs})

# Endpoint to visualize data
@app.route('/visualize', methods=['GET'])
def visualize_data():
    if not logs:
        return "No data to visualize."
    
    # Extract data
    dates = [log['date'] for log in logs]
    pain_levels = [log['pain_level'] for log in logs]
    mood_levels = [log['mood_level'] for log in logs]
    
    # Create Plotly graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=pain_levels, mode='lines+markers', name='Pain Level'))
    fig.add_trace(go.Scatter(x=dates, y=mood_levels, mode='lines+markers', name='Mood Level'))
    fig.update_layout(
        title='Pain and Mood Levels Over Time',
        xaxis_title='Date',
        yaxis_title='Level',
        template='plotly_dark'
    )
    
    # Return graph as HTML
    return pio.to_html(fig, full_html=True)

if __name__ == '__main__':
    app.run(debug=True)
