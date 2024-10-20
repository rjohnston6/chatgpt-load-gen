import click

from logger import logger
import chat_request


@click.command()
@click.option("-c", "--count", default=1, help="Number of Requests to Make")
@click.option(
    "-k", "--key", default="LLM", help="Enter API Key for Open WebUI test Server"
)
@click.option(
    "--url", default="http://localhost:8080/v1", help="URL of Open WebUI Test Server"
)
def main(count, key, url):

    # Define API Key and URL for Open WebUI
    OPENAI_API_KEY = key
    OPENAI_API_BASE = url

    # Create Connection to Open WebUI API
    client = chat_request.ai_client(OPENAI_API_KEY, OPENAI_API_BASE)

    chat_responses = chat_request.threaded_requests(client, count)
    for response in chat_responses:
        logger.warning(f"Chat-ID: {response.id}")
        logger.info(f"Response:\n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
