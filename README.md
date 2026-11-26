# Client Credentials and Token Refresh

## Project Description
This project demonstrates OAuth 2.0 Client Credentials flow using a mock authentication server built with Python Flask.

The client gets an access token using a client ID and client secret. The token is valid for 30 seconds. When the token expires, the client automatically requests a new token and retries the API request.

## Technologies Used
- Python
- Flask
- Requests
- VS Code

## Features
- Mock authentication server.
- POST `/token` endpoint to generate access tokens.
- GET `/data` endpoint protected by Bearer token authentication.
- Access token expires after 30 seconds.
- Client Credentials authentication.
- Automatic token refresh when the server returns 401.
- Retry API request once after refreshing the token.
- Token masking to avoid printing the full token.

## Installation

Install the required packages:

```bash
pip install flask requests
```

## How to Run

Start the authentication server:

```bash
python server.py
```

Open another terminal and run the client:

```bash
python client.py
```

## Expected Output

```text
Request number: 1
New token received: abc123****

You accessed the protected data!

Request number: 4
Token expired! Getting a new token...
New token received: xyz789****

You accessed the protected data!
```

*Token values shown above are examples.*

## Learning Outcomes
- Understanding Client Credentials flow.
- Generating and validating access tokens.
- Understanding token expiration.
- Handling 401 Unauthorized responses.
- Automatically refreshing expired tokens.

## Author
Python Learning Project