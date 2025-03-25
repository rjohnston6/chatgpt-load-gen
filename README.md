<!-- About Project -->
## About
To assist in demonstration and testing a basic Python project that executes multiple requests against a OpenWebUI API to generate a number of requests simulating a number of requests against a ChatGPT application. In the initial release a single sample message is submitted multiple times over and synchronously. To simplify use the project is containerized and allows for simply starting the container to execute a number of requests. Should multiple instances be desired the container can be started multiple times to increase the load against the API.

> [!NOTE]
> This is for experimentation, learning and demonstration purposes **ONLY** and is not intended for large scale test or validation for production implementations

## Built With
* [![Python][Python.py]][Python-url]
* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


<!-- Getting Started -->
## Getting Started
To simplify usage, simply clone the repo to your local development machine and build the container and run.

### Requirements
To simplify distribution and use, it is desired to be ran using a container runtime such as Docker or Podman. Instructions to build the container is provided for both Docker or Podman installations.

#### Tested with
* Podman v1.16.0
* Docker version 27.3.1

### Steps
1. Clone Repo to your local development machine 
    ```
    git clone https://github.com/rjohnston6/chatgpt-load-gen.git
    ```
2. Define environment variables for target OpenWebUI Target URL and API Key and desired base request count. A `env_example.list` file is included rename the file to `env.list` and update the variables to set them as part of the container execution process.

    | Variable | Default Value |
    | --- | --- |
    | COUNT | 10 |
    | API_KEY | YOURSUPERSECUREKEY |
    |API_URL | http://localhost:8000/v1 |
    | MODEL | /ai/models/NousResearch/Meta-Llama-3.1-8B-Instruct/ |

3. Build the the container using your preferred container runtime
   - **Docker:**
      ```
      cd chatgpt-load-gen
      docker build -t chatgpt-load:v1.0 .
      ```
   - **Podman:**
      ```
      cd chatgpt-load-gen
      podman build -t chatgpt-load:v1.0 .
      ```
4. Start the continer to generate load.
   - **Docker:**
      ```
      docker run -d --rm --env-file env.list chatgpt-load:v1.0
      ```
   - **Podman:**
      ```
      podman run -d --rm --env-file env.list chatgpt-load:v1.0
      ```  

<!-- Roadmap -->
## Roadmap
- [ ] Add randomized list of prompts for requests made



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org