# Data2bots 
## Clone or download this repo and create a virtual environment in the folder
### Run
> **pip install -r requirements.txt**
### Run 
> **python manage.py runserver**
### Go to **"127.0.0.1:8000"** on your browser (or whatever localhost it is running)
<br>

## Docs
###  **Swagger**: 127.0.0.1:8000/
### **Redoc**: 127.0.0.1:8000/redoc  
<br>

## Admin Details: 127.0.0.1:8000/admin
#
> username: admin  
> password: admin12345

<br>


## Login Method and Instructions
#
1. Go to 127.0.0.1:8000/ which will open the Swagger Interactable Docs.
2. Go to the Login endpoint under accounts.
3. Use the following details to login:
   > username: testuser  
   > password: testpass123
4. Copy the Token and scroll to the top of the page, look for "Authorize" and click it.
5. Insert **Token {the token you copied} e.g. Token 2163y18hidiodj30ji30** and click "Authorize".
6. Head over to orders and click execute under the endpoint to get your orders.

**Note**: Dummy data already exists in the database.

## Custom Commands
#
### You can create dummy users by typing:
> python manage.py createusers

### You can also create dummy products and orders as many times as you want by using:
> python manage.py createdata

## Tests
#
## To run tests, use:
> python manage.py test
## It will run the tests for all the apps available.  
<br>

## Necessary Endpoints
#
1.  For clients to **register**: 127.0.0.1:8000/api/v1/auth/register/
2.  To see your order history: 127.0.0.1:8000/api/v1/orders/ <br>~ *you must be logged in*
3.  For clients to edit their information: 127.0.0.1:8000/api/v1/auth/update/ <br>~ *you must also be logged in*
