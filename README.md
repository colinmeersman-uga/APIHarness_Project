# API Test Harness

A reusable and flexible command-line tool for testing REST APIs. This harness reads endpoint configurations from a YAML file, issues HTTP requests, and logs the responses for debugging and analysis.

## Features
* **Reusable:** Define target APIs and endpoints entirely in `config.yaml` without touching the codebase.
* **Flexible:** Supports multiple HTTP methods (GET, POST, PUT, DELETE), custom headers, and JSON body payloads.
* **Observable:** Outputs request execution details and response status/bodies to both the console and a local `api_test.log` file.

## Setup Instructions

1. **Prerequisites:** Ensure you have Python 3 installed. 
2. **Install Dependencies:**
   Run the following command to install the required libraries:
   `pip install requests pyyaml`

## Configuration (`config.yaml`)

The harness is driven entirely by `config.yaml`. Place this file in the root directory alongside the main script.

**Example Configuration:**
```yaml
base_url: "[https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)"

headers:
  Content-Type: "application/json"
  Authorization: "Bearer your-token-here"

endpoints:
  - path: "/users/1"
    method: "GET"
  - path: "/posts"
    method: "POST"
    body: 
      title: "API Harness Test"
      body: "Testing our new CLI tool"
      userId: 1

```

### Description
This PR introduces a reusable API Test Harness capable of reading configurations from a `config.yaml` file, executing HTTP requests (GET, POST, PUT, DELETE), and logging the results. 

### Proof of Functionality
Below is a snippet from the `api_test.log` demonstrating successful GET and POST requests to the JSONPlaceholder API:

@colinmeersman-uga ➜ /workspaces/CRUD_Project (main) $ python harness.py

2026-04-26 20:30:57,513 [INFO] Starting API Test Harness

2026-04-26 20:30:57,515 [INFO] --- Sending GET request to https://jsonplaceholder.typicode.com/users/1 ---

2026-04-26 20:30:57,589 [INFO] Status Code: 200

2026-04-26 20:30:57,590 [INFO] Response Body: {

  "id": 1,

  "name": "Leanne Graham",

  "username": "Bret",

  "email": "Sincere@april.biz",

  "address": {

    "street": "Kulas Light",

    "suite": "Apt. 556",

    "city": "Gwenborough",

    "zipcode": "92998-3874",

    "geo": {

      "lat": "-37.3159",

      "lng": "81.1496"

    }

  },

  "phone"...

2026-04-26 20:30:57,590 [INFO] --- Sending POST request to https://jsonplaceholder.typicode.com/posts ---

2026-04-26 20:30:57,649 [INFO] Status Code: 201

2026-04-26 20:30:57,650 [INFO] Response Body: {

  "title": "API Harness Test",

  "body": "Testing new CLI tool",

  "userId": 1,

  "id": 101

}...

2026-04-26 20:30:57,650 [INFO] API Test Harness execution completed.

### Known Limitations & Future Improvements

* **Limitation:** The tool currently processes requests synchronously. (Does exactly one thing at a time)

* **Future Idea 1:** Implement concurrency (using `asyncio` or threading) to allow for basic load testing across multiple endpoints at once. (Make the system do a bunch of things at the same time and see if it breaks)

* **Future Idea 2:** Add response validation so users can define expected status codes in the YAML file to automatically flag tests as Pass/Fail. (Letting the system autotest to see if it passed or failed rather than having to look through manually for the answer to see if it was correct)
