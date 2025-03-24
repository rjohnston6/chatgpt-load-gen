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


import threading
import concurrent.futures

import openai
from logger import logger as log


def ai_client(api_key, api_url):

    # Attempt to create a client connection to Open WebUI API
    try:
        client = openai.OpenAI(api_key=api_key, base_url=api_url)
        return client
    except Exception:
        log.error("Error Connecting to Web Open WebUI API", exc_info=True)


def make_request(client, model):
    try:
        test_content = """"write me a random short story that
         is 500 words and about IT."""

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": test_content,
                },
            ],
        )
        log.info(f"Response: {response}")
        return response
    except Exception as e:
        log.error(f"Error making request: {e}")


def threaded_requests(client, num_requests, model):
    try:
        response_bodies = []

        lock = threading.Lock()

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            # Submit the requests to the pool
            futures = [
                executor.submit(
                    make_request,
                    client, model) for _ in range(num_requests)
            ]

            # Wait for the requests to complete
            for future in concurrent.futures.as_completed(futures):
                response = future.result()
                with lock:
                    response_bodies.append(response)

        return response_bodies

    except Exception:
        log.error("Error sending request to Open WebUI", exc_info=True)
