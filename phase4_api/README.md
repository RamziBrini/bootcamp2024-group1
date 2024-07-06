# Pizza Recipe API

## Setup Instructions

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Install the VSCode extension for sending HTTP requests:
    - Name: REST Client
    - URL: [REST Client Extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

## Running the API

To start the API server, run the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

##  Querying the API

You can query the API using curl or by using the REST Client extension in VSCode.
Using Curl

Get the root endpoint:

```bash
curl -X GET http://localhost:8000/
```

Get all pizzas:

```bash
curl -X GET http://localhost:8000/pizzas/
```

Get details of a specific pizza (e.g., Margherita):

```bash
curl -X GET http://localhost:8000/pizza/Margherita
```


Using REST Client Extension

Alternatively, you can open the requests.http file in VSCode and click on "Send Request" for the respective endpoints.

![grafik](https://github.com/RamziBrini/bootcamp2024/assets/8480566/8379a923-218f-4bed-86a4-3e477a0b7fb9)
