import os
import env
import json
import time


def generate_filename():
    timestamp = int(time.time() * 1000)
    index = 0
    filename = f'{timestamp}.json'
    file_path = os.path.join(env.QUEUE_FOLDER, filename)

    while os.path.exists(file_path):
        index += 1
        filename = f'{timestamp}_{index}.json'
        file_path = os.path.join(env.QUEUE_FOLDER, filename)

    return file_path


def enqueue(data):
    file_path = generate_filename()
    filename = os.path.basename(file_path)

    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)

    return filename, len(get_queue_files())


def dequeue():
    json_files = get_queue_files()
    if not json_files:
        return None

    first_file = json_files[0]
    file_path = os.path.join(env.QUEUE_FOLDER, first_file)

    with open(file_path, 'r') as infile:
        data = json.load(infile)

    os.remove(file_path)
    return data


def get_queue_files():
    json_files = [f for f in os.listdir(
        env.QUEUE_FOLDER) if f.endswith('.json')]
    return json_files
