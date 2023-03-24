import sd_queue
import time
import requests
import env


def get_runpod_queue_status():
    url = f"{env.RUNPOD_API_BASE}/sdapi/v1/progress?skip_current_image=true"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["state"]["job_count"]
    else:
        return None


def submit_job_to_runpod(payload):
    url = f"{env.RUNPOD_API_BASE}/sdapi/v1/img2img"
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Job submitted successfully")
    else:
        print("Error submitting job:", response.text)


def main():
    while True:
        job_count = get_runpod_queue_status()

        if job_count is not None and job_count == 0:
            job_payload = sd_queue.dequeue()
            if job_payload is not None:
                submit_job_to_runpod(job_payload)
            else:
                print("No jobs in the local queue")
                time.sleep(5)
        else:
            time.sleep(5)


if __name__ == "__main__":
    main()
