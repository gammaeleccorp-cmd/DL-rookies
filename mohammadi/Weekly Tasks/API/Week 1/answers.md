# Week 1 - API

Contents:

[1. What is API?](#1.-What-is-API?)

[2. Client and Server](##-2.-Client-and-Server)

[3. Request and Response](##-3.-Request-and-Response)

[4. JSON](##-4-JSON)

[5. HTTP Methods](##5.-HTTP-Methods)

[6. HTTP Status Codes](##6.-HTTP-Status-Codes)

[7. REST API](##7.-REST-API)

[8. Design RESTful endpoints](##8.-Design-RESTful-endpoints)

[9. DRF vs FastAPI](##9.-DRF-vs-FastAPI)

[10. GraphQL vs REST](##10.-GraphQL-vs-REST)

[11. SOAP vs REST](##11.-SOAP-vs-REST)

## 1. What is API?

**API** (Application Programming Interface) is a way for two software applications to communicate with each other and **exchange** data or services.

For example, suppose we want to translate an English text into Persian using Google Translate. When we enter the text, instead of translating itself, it sends a request to a Google server containing the text and the target language. The server processes the translation and sends that back to the application in its response.

So, an API acts as an interface between different software systems, allowing them to communicate without needing to know how each system works internally.

## 2. Client and Server

A **Client** is the application or device that sends a **request** and uses a service.

Examples:

Mobile application               
Web browser                
Python program                  
Frontend application               

A **Server** is a system that receives requests, processes them, and sends **responses** back to the Client.

``` 
Client → Request → Server → Response → Client
```
In an online shopping application, the mobile app is the Client, while the backend server manages products, users, orders, and other data.

## 3. Request and Response

Communication between a Client and Server commonly happens using **HTTP**.

### HTTP Request

A Request is sent from the Client to the Server.

Important components include:

**HTTP Method:** specifies what action the client wants to perform.                              
**URL:** the location of the resource the client wants to access.                                 
**HTTP Version:** specifies the HTTP protocol version being used, such as HTTP/1.1 or HTTP/2                           
**Headers:** additional information about the request, such as authentication, content type,...                          
**Request Body (when needed):** data sent from the client to the server.

Example:

``` 
POST /students HTTP/1.1
Content-Type: application/json

{
  "name": "Sina",
  "age": "22",
  "email": "Sina@ut.ac.ir"
}
```

Here:

```  
Method: POST                     
URL: /users                               
Header: Content-Type: application/json → tells the server the body contains JSON.                         
Request Body: {"name": "Sina", "age": "22", "email": "Sina@ut.ac.ir"}
```

### HTTP Response

A Response is sent from the Server back to the Client.

Important components include:

**HTTP Version**                              
**Status Code:** a number indicating the result of the request.                  
**Status Text:** a short description of the status code.                             
**Headers**                           
**Response Body (when needed):** the actual data returned by the server.          

Example:

``` 
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 10,
  "name": "Sina",
  "age": "22",
  "email": "Sina@ut.ac.ir"
}
```

Here:

``` 
Status Code: 201                         
Status Text: Created                                               
Response Body: {"id":10, "name":"Sina", "age": "22", "email": "Sina@ut.ac.ir"}
```

## 4. JSON

**JSON** (JavaScript Object Notation) is a lightweight **text format** used to represent and exchange data which both humans and machines can write and read.

It is like dictionaries consists of **key-value** pairs.       
Each **key** is a string, followed by a colon and a corresponding value.        
**Values** can be strings, numbers, booleans, objects, arrays, or null, and commas are used to separate key-value pairs within objects, as well as values within arrays.        

Consider the following example:

``` 
{
  "name": "Amir",
  "age": 31,
  "Job": Data Scientist,
  "interests": ["Tennis", "running", "dogs"],
  "address": {
      "street": "123 Main St",
      "zipCode": "12345"
  }
}
```

This example represents a person as a JSON object. 

As we can see, JSON supports **nesting**, which allows you to create complex data structures by including objects and arrays within other objects or arrays.

JSON is widely used in APIs because:

It is simple and easy to read.                       
It is relatively lightweight.                         
It has a clear structure.                          
Almost every programming language supports it.                    
It is convenient for transferring data between Client and Server.

## 5. HTTP Methods

The **HTTP method** represents the action the client expects the server to perform on the resource. 

The common HTTP request methods are:

**GET**: Is used when the client tries to retrieve a specific resource from the server.

Request:
``` 
GET /products
```

It means give me the information about all products.

or we can get a specific product:

``` 
GET /products/101
```

Response:

``` 
200 OK
```

``` 
{
  "id": 101,
  "name": "AirPods",
  "price": 99.99,
  "category": "Electronics",
  "stock": 25
}
```

**POST**: When the client wants to create a new resource.

``` 
POST /products
```

Request body:
``` 
{
  "name": "Mechanical Keyboard",
  "price": 89.99,
  "category": "Electronics",
  "stock": 15
}
```

The Server creates the product and generates an id.

**PUT**: Indicates that the client would like to replace or completely update a resource.

Suppose product 101 currently looks like this:

``` 
{
  "id": 101,
  "name": "AirPods",
  "price": 99.99,
  "category": "Electronics",
  "stock": 25
}
```

We want to replace its information.

``` 
PUT /products/101
```

Request body:

``` 
{
  "name": "Galaxy Buds",
  "price": 49.99,
  "category": "Audio",
  "stock": 30
}
```

Response:

``` 
200 OK
```

``` 
{
  "id": 101,
  "name": "Galaxy Buds",
  "price": 49.99,
  "category": "Audio",
  "stock": 30
}
```

**PATCH**: When the client wants to partially update a resource.

``` 
PATCH /products/101
```

Body:

``` 
{
  "price": 79.99
}
```

Response:

``` 
200 OK
```

``` 
{
  "id": 101,
  "name": "AirPods",
  "price": 79.99,
  "category": "Electronics",
  "stock": 25
}
```

**DELETE**: Indicates that the client is trying to delete a resource from the server.

``` 
DELETE /products/101
```

Response:

``` 
204 No Content
```

The product is now deleted.

## 6. HTTP Status Codes

HTTP status codes are **three-digit numbers** that indicate whether a request **succeeded**, **failed**, or **requires additional steps**.

They are grouped into **five classes**, each beginning with a number that represents the type of response.

1xx informational responses              
2xx success responses                       
3xx redirection responses                        
4xx client error responses                       
5xx server error responses                 

**200 - OK**

The request was successful and the server returned the requested data.

**201 - Created**

A new resource was successfully created.

**202 - Accepted**

The request has been accepted for processing but hasn’t been completed yet.

**204 - No Content**

Confirms that the request was successful, but the server did not return any data.

**400 - Bad Request**

It means the server couldn’t understand the request due to invalid syntax, malformed JSON, or missing required fields. 

**401 - Unauthorized**

Signals that authentication is required and either wasn’t provided or was invalid.

**403 - Forbidden**

The client is authenticated but doesn’t have permission to access the requested resource. 

**404 - Not Found**

It means the requested resource doesn’t exist. This could be because the resource was deleted, never existed, or the URL is incorrect.

**405 Method Not Allowed**

Tells the client that the HTTP method used isn’t supported for this endpoint.

**408 Request Timeout**

Indicates the server timed out waiting for the client to send the complete request. 

**429 Too Many Requests**

It means the client has exceeded rate limits.

**500 Internal Server Error**

It is a generic error indicating something went wrong on the server. 

**502 Bad Gateway** 

Occurs when a server acting as a gateway or proxy receives an invalid response from an upstream server.

**503 Service Unavailable**

It Means the server is temporarily unable to handle requests, often due to maintenance or overload.

**504 Gateway Timeout** 

Indicates that a gateway or proxy server didn’t receive a timely response from an upstream server.

## 7. REST API

**REST** (Representational State Transfer) is an **architectural style** for designing APIs which introduced by Roy Fielding in 2000.

In REST, the data or objects that an API manages are treated as **Resources**.

An **Endpoint** is a URL through which the Client access that Resource.

REST supports JSON, XML, HTML and plain text formats.

For example, in an educational system:

```
Student             
Teacher                    
Course                       
University
```

can all be resources.

If Student is our resource, we can represent it with:

```
/students
```

and 

```
GET /students
```

is an endpoint.

We can use HTTP methods to perform operations on the Resource.

To call an API **RESTful**, it should respect these constraints:

**1. Uniform interface**          
Resources are identified with URIs, and the interface is consistent across the API. Clients use the same methods in the same ways, which improves learnability and interoperability.

**2. Client-Server separation**             
The client handles the UI and request orchestration. the server handles data storage, security, and workload. Decoupling lets each evolve independently.

**3. Stateless operations**            
Every request carries the information needed to process it. Servers don’t store client session state, which simplifies scaling.

**4. Cacheable responses**                    
Responses explicitly declare whether and how they can be cached. Proper caching reduces latency and server load.

**5. Layered system**                  
Intermediaries like load balancers, gateways, and caches can sit between client and server without changing the contract.

## 8. Design RESTful endpoints

Suppose our Resource is:

```
Student
- id
- name
- email
- level
```

A RESTful design could be:

Get all students
```
GET /students
```

Get one student
```
GET /students/{id}
```

Create a student

```
POST /students
```

Completely update a student

```
PUT /students/{id}
```

Partially update a student

```
PATCH /students/{id}
```

Delete a student

```
DELETE /students/{id}
```

## 9. DRF vs FastAPI  

**DRF (Django REST Framework)** is a toolkit for building REST APIs on top of Django.

DRF adds API-specific features such as:

Serializers               
API views                       
ViewSets                      
Routers                        
Permissions                      
Authentication                  
Browsable API                 

For example, we might define a Django model and then create a serializer and ViewSet around it. DRF handles a lot of the repetitive API work for us.

**FastAPI** (released in 2018) is a modern Python web framework designed particularly well for building APIs.

It makes heavy use of Python type hints and automatically generates:

Request validation                 
JSON serialization                       
OpenAPI documentation                   
Swagger UI                   
ReDoc documentation                

And async support is a first-class feature.

This makes FastAPI particularly attractive for high-concurrency APIs, microservices, and services that make lots of external/network calls.

FastAPI is generally faster than DRF in raw API benchmarks, particularly when using async endpoints appropriately.

If the API spends most of its time querying PostgreSQL, running business logic, or calling another service, the framework's raw benchmark difference may not matter much.

DRF's ecosystem and Django's built-in functionality can be far more valuable than squeezing out maximum request throughput.

## 10. GraphQL vs REST

**GraphQL** (created by Facebook in 2012 and open-sourced in 2015) is a data query and manipulation **language** that allows specifying what data is to be retrieved or modified.       
A GraphQL server can process a client query using data from separate sources and present the results in a unified graph.    

In REST, when the client requests to get a student email, the server responses the whole resourse:

Request:

```
GET /students/10
```

Response:

```
{
  "id": 10,
  "name": "Emad",
  "email": "emad@ut.ac.ir",
  "level": "Graduate"
}
```

But with GraphQL, the client can query and get just the email:

```
POST /graphql
```

Request Body:

```
query {
  student(id: 10) {
    email
  }
}
```

Response:

```
"student":{
  "email": "emad@ut.ac.ir"
}
```

This problem that GraphQL solves is called **Over-fetching**.

Note that GraphQL usually has a single endpoint (POST /graphql), but the endpoint name is not universally fixed.

There is another problem called **Under-fetching** that the client must request multiple times to retreive the information it wants but with GraphQL, with just one query can get them.

If we want to create, update or delete, we should do the following:

To create:

```
POST /graphql
```

```
mutation {
  createStudent(
    name: "Reza"
    email: "Reza@ut.ac.ir"
    level: "Undergraduate"
  ) {
    id
    name
    email
    level
  }
}
```

To update:

```
mutation {
  updateStudent(
    id: 10
    level: "Graduate"
  ) {
    id
    name
    level
  }
}
```

And to delete:

```
mutation {
  deleteStudent(id: 10) {
    id
  }
}
```

Note that create/update/deleteStudent are defined by API designer and not universally fixed.

## 11. SOAP vs REST

**SOAP** (Simple Object Access Protocol) was published in 1998 which is a message specification for exchanging information between systems and applications . 

SOAP API is developed in a **more structured** and formalized way.  
Think of it as being like the national postal service: It provides a reliable and trusted way to send and receive messages between systems (and within enterprise applications).

It is older, established, and dependable but it can be **slower** than REST.

SOAP uses **XML** as the data format for messages being sent and received by an API client, and it provides four distinct dimensions to the API protocol:

**Envelope**: Defining the structure of the message.            
**Encoding**: Rules for expressing the type of data.                   
**Requests**: How each SOAP API request is structured.            
**Responses**: How each SOAP API response is structured.             

Let’s take a look at an example of a SOAP API in an ISBN book validation service, which provides validation using a simple URL:

```
http://webservices.daehosting.com/services/isbnservice.wso
```

This ISBN validation service uses a POST HTTP method to pass the following structured snippet of XML to the service using the body of the HTTP request. It provides a structured request for the server to process and return a response:

```
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
 <soap:Body>
  <IsValidISBN10 xmlns="http://webservices.daehosting.com/ISBN">
   <sISBN>0-19-852663-6</sISBN>
  </IsValidISBN10>
 </soap:Body>
</soap:Envelope>
```

This then returns the following XML response, which confirms that the ISBN number is valid:

```text
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <m:IsValidISBN10Response xmlns:m="http://webservices.daehosting.com/ISBN">
         <m:IsValidISBN10Result>true</m:IsValidISBN10Result>
      </m:IsValidISBN10Response>
   </soap:Body>
</soap:Envelope>
```

This ISBN validation service uses a standardized SOAP envelope to pass a structured message as part of the request, resulting in a standardized response sent in the same way.       
The SOAP response structure makes it easy for developers to understand and put to work in their applications and integrations.

Some of the most common use cases for SOAP APIs include:

Transfers at banks          
Booking flights                  
Billing services           
City management

In conclusion, both SOAP and REST are useful for developing web services, but they serve different purposes. REST is simpler, faster, and more flexible, making it a popular choice for modern web and mobile applications. SOAP is more complex but provides strong standards, security, and reliability, making it suitable for enterprise and transaction-based systems. Therefore, the choice between SOAP and REST depends on the specific requirements of the application.