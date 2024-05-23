from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run-task', methods=['POST'])
def run_task():
    # Your task logic here
    data = request.json
    print("Received data:", data)
    # Simulate a task
    result = {"status": "Task completed", "data": data}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
