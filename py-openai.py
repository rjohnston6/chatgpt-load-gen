import openai
import threading
import concurrent.futures
import random
import time

# Set your OpenAI API key
openai_api_key = "LLM"
openai_api_base = "http://64.101.169.102:8000/v1"

# Set the number of requests to make
NUM_REQUESTS = 1000

# Set the delay between requests (in seconds)
DELAY = 0.1

# Create an OpenAI API client
client = openai.OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)


# Define a function to make a single request
def make_request():
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
        return response
    except Exception as e:
        print(f"Error making request: {e}")


# Create a list to store the response bodies
response_bodies = []

# Create a lock to synchronize access to the list
lock = threading.Lock()

# Create a pool of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Submit the requests to the pool
    futures = [executor.submit(make_request) for _ in range(NUM_REQUESTS)]

    # Wait for the requests to complete
    for future in concurrent.futures.as_completed(futures):
        response = future.result()
        with lock:
            response_bodies.append(response)

# Print the response bodies
for response in response_bodies:
    print(f"Chat-ID: {response.id}, Response: {response.choices[0].message.content}")
