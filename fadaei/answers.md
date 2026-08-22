# API Design Concepts

## 1. API

An API (Application Programming Interface) is an interface that allows two applications to communicate with each other. One side sends a request, the other side returns a response. The requesting side does not need to know how the other side works internally; it only needs to know how to ask.

## 2. Client and Server

The Client is the side that sends the request, such as a mobile application or a web browser.

The Server is the side that receives the request, processes it, and returns the result.

The Client always initiates the communication. The Server only answers.

## 3. Request and Response

A Request is the message the Client sends to the Server, describing what it needs. A request contains:

- The target address
- The method
- Headers
- Optionally a body

A Response is the message the Server sends back. A response contains:

- A status code
- Headers
- Usually a body

Every request produces exactly one response.

## 4. JSON

JSON (JavaScript Object Notation) is a text format used to exchange structured data. It is lightweight, human readable, and supported by every major programming language, which makes it the standard format for request and response bodies.

```json
{
  "id": 101,
  "name": "Ali",
  "email": "ali@example.com",
  "active": true
}
```

## 5. HTTP Methods

An HTTP method declares the type of operation the Client wants to perform on a resource.

- `GET` — Retrieve a resource without changing it
- `POST` — Create a new resource
- `PUT` — Replace an existing resource completely
- `PATCH` — Update part of an existing resource
- `DELETE` — Remove a resource

## 6. Status Codes

A status code is a three digit number in the response that tells the Client the outcome of the request.

Common codes:

- `200 OK` — The request succeeded
- `201 Created` — A new resource was created
- `204 No Content` — The request succeeded, no body returned
- `400 Bad Request` — The request is malformed or invalid
- `401 Unauthorized` — Identity is missing or not valid
- `403 Forbidden` — Identity is valid but access is denied
- `404 Not Found` — The requested resource does not exist
- `500 Internal Server Error` — The server failed while processing

Codes are grouped by their first digit:

- `2xx` — Success
- `3xx` — Redirection
- `4xx` — Client error
- `5xx` — Server error

## 7. Authentication and Authorization

Authentication answers the question *who are you*. The Client proves its identity, usually with a token, an API key, or credentials, and the Server verifies it.

Authorization answers the question *what are you allowed to do*. It happens after authentication and decides whether the identified Client may perform the requested operation on the requested resource.

## 8. Security

Security means protecting the API and its data from unauthorized access and misuse. The main measures are:

- Serving all traffic over HTTPS so data is encrypted in transit
- Requiring authentication for every protected endpoint
- Enforcing authorization rules on each resource
- Validating and sanitizing all incoming data
- Never exposing internal details such as stack traces in responses
- Storing secrets and keys outside the source code

## 9. API Documentation

Documentation explains how to use the API so that a developer can consume it without reading its source code. Complete documentation includes:

- The purpose and scope of the API
- The base URL and versioning scheme
- Every endpoint with its method and path
- Required and optional parameters with their types
- The structure of the request body
- The structure of the response body
- The list of possible status codes and errors
- Authentication requirements
- Working request and response examples

## 10. Error Handling

Error handling means returning a clear, consistent, and predictable message when a request cannot be completed, instead of failing silently or crashing. A well formed error response carries the correct status code and a body that explains the cause.

```json
{
  "error": "validation_failed",
  "message": "The email field is not a valid email address.",
  "field": "email"
}
```

The same error structure should be used across the whole API so clients can handle failures in one place.

## 11. Best Practices

- Name resources with plural nouns, for example `/users` instead of `/getUser`
- Use lowercase paths and hyphens rather than underscores
- Let the HTTP method express the action, not the URL
- Version the API in the path, for example `/api/v1/users`
- Keep the response format identical across all endpoints
- Paginate any endpoint that can return a large collection
- Return the most specific status code available
- Apply rate limiting to protect the service from abuse
- Use caching for data that does not change often
- Keep the documentation updated together with the code