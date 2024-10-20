import threading
import concurrent.futures

import openai
from logger import logger as log


def ai_client(api_key, api_url):

    # Attempt to create a client connection to Open WebUI API
    try:
        client = openai.OpenAI(api_key=api_key, base_url=api_url)
        return client
    except Exception as e:
        log.error("Error Connecting to Web Open WebUI API", exc_info=True)


def make_request(client):
    try:
        response = client.chat.completions.create(
            model="/ai/models/Meta-Llama-3-8B-Instruct/",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "San Francisco is",
                },
            ],
        )
        log.info(f"Response: {response}")
        return response
    except Exception as e:
        log.error(f"Error making request: {e}")


def threaded_requests(client, num_requests):
    try:
        response_bodies = []

        lock = threading.Lock()

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # Submit the requests to the pool
            futures = [
                executor.submit(make_request, client) for _ in range(num_requests)
            ]

            # Wait for the requests to complete
            for future in concurrent.futures.as_completed(futures):
                response = future.result()
                with lock:
                    response_bodies.append(response)

        return response_bodies

    except Exception as e:
        log.error("Error sending request to Open WebUI", exc_info=True)
