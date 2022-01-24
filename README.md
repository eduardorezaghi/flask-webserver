# flask-webserver
A simple Flask HTTP web-server, which implements *nearly* all HTTP methods in a Flask web application.
---
## Testing examples
In order to test this simple webserver, you can use _cURL_ or _Postman_.
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
