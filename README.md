# Simple HTTP Server

This project is a simple HTTP server implemented in Python using the `http.server` module. It handles both GET and POST requests and stores data in a JSON file.

## Features

- **GET /**: Returns the contents of `file.json` as a JSON response.
- **POST /**: Accepts a `link` parameter (either as form data or JSON) and appends it to `file.json`.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/simple-http-server.git
    cd simple-http-server
    ```

2. Ensure you have Python 3 installed. You can check your Python version with:
    ```sh
    python --version
    ```

## Usage

1. Run the server:
    ```sh
    python app/main.py
    ```

2. The server will start on `0.0.0.0:8000`.

## Endpoints

### GET /

Returns the contents of `file.json`.

**Example Request:**
```sh
curl http://localhost:8000/
```

**Example Response:**
```json
[
    "http://example.com",
    "http://anotherexample.com"
]
```

### POST /

Accepts a `link` parameter and appends it to `file.json`.

**Example Request:**
```sh
curl -X POST -H "Content-Type: application/json" -d '{"link": "http://example.com"}' http://localhost:8000/
```

**Example Response:**
```
Link added successfully
```

## Error Handling

- **404 Not Found**: Returned if the requested path is not `/`.
- **400 Bad Request**: Returned if the `link` parameter is missing in the POST request.
- **500 Internal Server Error**: Returned if there is an error processing the request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
