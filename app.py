from flask import Flask, request, jsonify, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

# In-memory data storage (for now)
logs = []

# Endpoint to log data
@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    
    # Validate incoming data
    if not data or not all(key in data for key in ("date", "pain_level", "mood_level")):
        return jsonify({"error": "Invalid data. Fields 'date', 'pain_level', and 'mood_level' are required."}), 400
    
    try:
        pain_level = int(data['pain_level'])
        mood_level = int(data['mood_level'])

        # Check if pain_level and mood_level are between 1 and 10
        if not (1 <= pain_level <= 10 and 1 <= mood_level <= 10):
            return jsonify({"error": "Pain level and mood level must be between 1 and 10."}), 400
    except ValueError:
        return jsonify({"error": "Pain level and mood level must be integers."}), 400

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
        return jsonify({"message": "No data to visualize."})

    # Extract data for plotting
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

# Endpoint to delete a log by date
@app.route('/delete', methods=['DELETE'])
def delete_log():
    data = request.json
    date_to_delete = data.get('date')

    # Filter logs to exclude the one with the date to delete
    global logs
    logs = [log for log in logs if log['date'] != date_to_delete]

    return jsonify({"message": f"Logs for {date_to_delete} deleted.", "logs": logs})

# Endpoint to edit an existing log
@app.route('/edit', methods=['PUT'])
def edit_log():
    data = request.json
    date_to_edit = data.get('date')
    new_pain_level = data.get('pain_level')
    new_mood_level = data.get('mood_level')

    # Find the log and update the pain and mood levels
    for log in logs:
        if log['date'] == date_to_edit:
            log['pain_level'] = new_pain_level
            log['mood_level'] = new_mood_level
            break

    return jsonify({"message": f"Log for {date_to_edit} updated.", "logs": logs})

# Endpoint to filter logs by date range
@app.route('/filter', methods=['GET'])
def filter_logs():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Filter logs based on the date range
    filtered_logs = [
        log for log in logs
        if start_date <= log['date'] <= end_date
    ]

    return jsonify({"filtered_logs": filtered_logs})

# Start the app
if __name__ == '__main__':
    app.run(debug=True)
