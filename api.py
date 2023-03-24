from flask import Flask, request, jsonify
import sd_queue
import env


app = Flask(__name__)


@app.route('/api/v1/enqueue', methods=['POST'])
def enqueue():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON object received"}), 400

    filename, size = sd_queue.enqueue(data)

    return jsonify({"filename": filename, "queue_size": size}), 200


@app.route('/api/v1/queue', methods=['GET'])
def get_queue_state():
    return jsonify({"queue": sd_queue.get_queue_files()}), 200


@app.route('/api/v1/queue/size', methods=['GET'])
def get_queue_size():
    queue_size = len(sd_queue.get_queue_files())
    return jsonify({"queue_size": queue_size}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=env.API_PORT)


# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=API_PORT)
