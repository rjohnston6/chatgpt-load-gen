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


import logging

from rich.logging import RichHandler


fmt = "%(asctime)s - %(message)s"

logging.basicConfig(
    level="WARNING",
    format=fmt,
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger(__name__)
