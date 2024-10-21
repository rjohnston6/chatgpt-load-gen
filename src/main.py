#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python example script showing proper use of the Cisco Sample Code header.

Copyright (c) 2024 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""


from __future__ import absolute_import, division, print_function


__author__ = "Russell Johnston <rujohns2@cisco.com>"
__contributors__ = [
    "Patrick leMaistre <plemaist@cisco.com>",
]
__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


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
