# bakery

The app bakery have following functionality

FOR ADMIN (using django admin)-

1. Add Ingredients to bakery
2. Create BakeryItem from a list of ingredients
3. Get the detail of BakeryItem 
4. Manage inventory

FOR CUSTOMER (using APIs)-

1. Register and Login    (/register/   , /login/,  /api-token-auth/)
2. Get a list of available products (/get_items/)
3. Place an Order and get the bill  (/order_item/)
4. See order history  (/check_order_history/)


Here is the description,request headers, body for various APIs used to perfom the above functionality-

To register a user use register API-

endpoint- /register/
method - POST
Request body-

{
    "username": "some_user",
    "email": "some_email@some_domain.com",
    "password": "somepassword"
}

Success Response-

{
    "username": "some_user",
    "email": "some_email@some_domain.com",
    "password": "somepassword"
}
with status code 201

-------------------------------------------------

To login a user use LOGIN API-

endpoint- /login/
method - POST
Request body-

{
    "username": "some_user",
    "password": "somepassword"
}

Success Response-

"Hi some_user! Please generate token"

with status code 200

-------------------------------------------------

To generate token use api-token-auth API-

endpoint- /api-token-auth/
method - POST
Request body-

{
    "username": "some_user",
    "password": "somepassword"
}

Success Response-
{
    "token": "379000000000000000000000some_token"
}
with status code 200

--------------------------------------------------
Use this token for authorization in headers for APIs hereafter as shown below-

 Authorization: Token 379000000000000000000000some_token
--------------------------------------------------


To get items use GET_ITEMS API-

endpoint- /get_items/
method - GET
Request headers-
    Authorization: Token 379000000000000000000000some_token


Success Response-
[
    {
        "id": 5,
        "name": "Cupcake",
        "sell_price": 100.0
    }
]
with status code 200

-------------------------------------------------


To order item use ORDER_ITEM API-

endpoint- /order_item/
method - POST
Request headers-
    Authorization: Token 379000000000000000000000some_token

Request body-
    {
        "bakeryitem": 5, 
        "quantity_ordered":"1",
        "payable_amount":100
    }

Success Response-
    {
        "bakeryitem": 5,
        "quantity_ordered": 1,
        "payable_amount": 100.0
    }
    with status code 200
    
#This api has validations for verifying payment amount and verifying if we have stock to provide this order.

--------------------------------------------------


To check order history use CHECK_ORDER_HISTORY API-

endpoint- /check_order_history/
method - GET
Request headers-
    Authorization: Token 379000000000000000000000some_token


Success Response-
[
    {
        "id": 10,
        "bakeryitem": 5,
        "quantity_ordered": 1,
        "payable_amount": 100.0
    },
    {
        "id": 11,
        "bakeryitem": 5,
        "quantity_ordered": 1,
        "payable_amount": 100.0
    }
]
with status code 200
