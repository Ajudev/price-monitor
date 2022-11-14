# Task - Ajudev

## Description

Django application that consists of API endpoints which will fetch live rates from alphavantage endpoint. The rates will show exchange convertion rate information for BTC/USD. The application will also expose a websocket endpoint which if users can subscribe to and receive updates of live rates every 1 minute. I have used Celery for scheduling and fetching data from alphavantage endpoint, Django channels for creating and managing websocket connection. Redis as a channel layer for django channels and broker for celery.

## List of Tasks achieved

- Create an API endpoint with GET method which will return an exchange rate history filled by 10, 30 and all time records from database
- Create an API endpoint with POST method which will return fetch the updated rates from alphavantage api, record the data into database and display the same as response.
- Create API endpoint with POST menthod which will create a new user who can access the HTTP endpoints, fetch JWT access and refresh token api for user to access HTTP endpoint, refresh access token api by providing the refresh token that was provided when fetching the access and refresh tokens.
- Implement JWT authentication for the API endpoints mentioned above.
- Added error handling for both the API endpoints mentioned.
- Implement pagination on both the GET method of API endpoint to avoid having to load a huge amount of data all at once. Users can request for 10 items per page, 30 items per page or fetch all of the data from the database using the GET method.
- Refactor code to follow DRY principle by moving frequently used code to **helpers.py** file and calling them from the view responsible for rendering the data for the api endpoints.
- Create websocket endpoint which will show live exchange rate, bid price & ask price along with timestamp received on a simple HTML page on every 1 minute from alphavantage endpoint. Websocket endpoint is created using Django-Channels and Celery is being used to run task of fetching the rates from alphavantage endpoint every 1 minute.
- Store sensitive data like DB credentials, API Key for alphavantage endpoint in .env file and load it from Django application.
- Create docker-compose file which when run will containerize Django app, Database, Redis and Celery services which are required to run the django application.

## Assumptions

- GET method of **/api/v1/quotes** displays 10, 30 items per page or how much ever is needed needs to be passed to **per_page** parameter and that many items will be displayed in a page with pagination or shows all data from database without pagination.
- JWT authentication is only implemented for **/api/v1/quotes** endpoint. Websocket endpoint won't have authentication.

## Instructions to run application

- Please make sure you have docker and docker-compose extention installed before running the application
- Please make sure to give **run.sh** file executable permissions and then you can execute **run.sh** file which will run compose build and up commands to launch the containers which will host the components required for the application to run.
- After running the application if you want to stop the application service please execute **docker-compose down** command to shutdown and remove the containers.

## Endpoint Details

- Please make sure to use **http://localhost:5678**, **http://127.0.0.1:5678** as base domain when trying to access the http endpoint. You can access the websocket using the same way mentioned above but replace http with ws
- If you are accessing the application for the first time you need to make sure you create a user who can access the HTTP endpoint (**/api/v1/quotes**) since this endpoint require JWT authentication.
- Create a user by calling POST method **/users/auth/register api endpoint**. This endpoint requires **"username"**, **"password"**, **"email"** information passed as json data to the endpoint for the api to create a new user.
- After creating a new user you can obtain the access and refresh token required to access the HTTP endpoints by calling the POST method of **/users/auth/token api endpoint**. This endpoint requires **"username"**, **"password"** information passed as json data to the endpoint for the api to issue access and refresh token. Access token will be returned in response which is a json data under parameter **access** and Refresh token will be returned in response which is a json data under parameter **refresh**
- To fetch existing rates data from database use GET method of **/api/v1/quotes**. This endpoint expects access token created earlier as bearer token under authorization section of the headers for the api endpoint. This way the application will check if the user is a registered user and send the data to the user if he is registered. I have added pagination to this API, so if you want to access 10 items per page pass 10 to **per_page** parameter to the API request. This will return the data with total number of pages and 10 rates record from the database in response. You can also pass **page** parameter to the api to access the page you want data from if there are multiple pages. ex: page=1 or page=5. If you omit **per_page** parameter then you can access all of the rates data present in the database.
- To get latest rates use POST method of **/api/v1/quotes**. This endpoint expects access token created earlier as bearer token under authorization section of the headers for the api endpoint. This way the application will check if the user is a registered user and send the data to the user if he is registered. The api will fetch the latest rates data from alphavantage api and store it in the database after which it will display the data as response to the api call.
- If your access token expires the api endpoint mentioned above will return with **"Invalid Authentication Credentials"** message as response. You can call POST method of **/users/auth/refresh** api endpoint to get a new access token. Please make sure to pass **refresh** in json data which contains the refresh token that was obtained initially from **/users/auth/token** api endpoint.
- If the refresh token expires then please use **/users/auth/token** api endpoint and follow the process mentioned in the above for this endpoint to get new access and refresh token.
- Refresh token is valid for 7 days and access token is valid for 30 minutes.
- To access the html page which will fetch the rates data every 1 minute from alphavantage api endpoint please visit **http://localhost:5678/rates/live** link. The page will connect with websocket built using Django channels for receiving the lates rates data from alphavantage api. The page gets updated every 1 minute with the live exchange rate, bid price & ask price along with timestamp received from alphavantage api endpoint.
