import click

from logger import logger
import chat_request

# Define API Key and URL for Open WebUI
OPENAI_API_KEY = "LLM"
OPENAI_API_BASE = "http://64.101.169.102:8000/v1"


@click.command()
@click.option("-c", "--count", default=1, help="Number of Requests to Make")
def main(count):

    # Create Connection to Open WebUI API
    client = chat_request.ai_client(OPENAI_API_KEY, OPENAI_API_BASE)

    chat_responses = chat_request.threaded_requests(client, count)
    for response in chat_responses:
        logger.warning(f"Chat-ID: {response.id}")
        logger.info(f"Response:\n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
