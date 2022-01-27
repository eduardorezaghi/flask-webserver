# flask-webserver
A simple Flask HTTP web-server, which implements *nearly* all HTTP methods in a Flask web application.  
This Flask web-server has been updated with:
- [X] Pydantic validation
- [X] Simple TinyDB JSON database
- [X] API Specification (Swagger route testing)
> **_NOTE:_**  This Flask-webserver specification is a simple implementation of a API documentation, and may be prone to errors.
---
## API Specification
In order to access and test the web-server routes, enter in your browser:
- **127.0.0.1:5000/apidoc/swagger**  
  or
- **127.0.0.1:5000/apidoc/redoc**
## Testing examples
In order to test this simple web-server, you can use _cURL_, _Postman_ or _httpie_.
- Testing using cURL:
  - GET 
    ```console 
    $  curl -i -X GET 127.0.0.1:5000/carrinho/
    ```
    ```console
    $  curl -i -X GET 127.0.0.1:5000/carrinho/<int:id>
    ```

  - OPTIONS:
    ```console
    $  curl -i -X OPTIONS 127.0.0.1:5000/
    ```

  - POST: 
    ```console
    $  curl -i -X POST 127.0.0.1:5000/carrinho/post/ -H "Content-Type: application/json" -d '{\"nome\":\"notebook avell\"}'
    ```

  - PUT:
    ```console
    $  curl -i -X PUT 127.0.0.1:5000/carrinho/put/2 -H "Content-Type: application/json" -d '{\"nome\":\"blu-ray player\"}' 
    ```

  - PATCH:
    ```console
    $  curl -i -X PATCH 127.0.0.1:5000/carrinho/patch/2 -H "Content-Type: application/json" -d '{\"nome\":\"blu-ray player\"}'
    ```

  - DELETE:
    ```console
    $  curl -i -X DELETE 127.0.0.1:5000/carrinho/delete/99
    ```
