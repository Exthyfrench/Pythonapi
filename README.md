# Pythonapi

This API has two endpoints:

/items: Accepts GET and POST requests. GET requests return a JSON object containing a list of items, while POST requests add a new item to the list.

/items/<int:index>: Accepts GET, PUT, and DELETE requests. GET requests return a JSON object containing the item at the specified index, 
PUT requests update the item at the specified index, and DELETE requests remove the item at the specified index.

You can test the API by starting the Flask development server and sending requests to the endpoints using a tool such as curl or Postman.
