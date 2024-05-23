from flask import Flask, request, jsonify
from detect_and_track import mymain

app = Flask(__name__)

@app.route('/run-task', methods=['POST'])
def run_task():
    data = request.get_json()
    print(f"Received data: {data}")
    
    loop = data.get('loop')
    source = data.get('source')
    task_id = data.get('task_id')
    
    result = mymain(cmd=False, custom_arg=['--loop', loop, '--source', source, '--filename', task_id])
    return jsonify({"message": "Hello World", "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
