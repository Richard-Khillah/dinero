# Restaurant Module
---


## Endpoint: GET /restaurants/
**Authentication:** No Auth needed __FOR NOW__

### Response
```javascript
{
  "status" : "success or error",
  "message" : "message of some kind both success or fail",
  "data" : {
    "restaurants" [
      {
        "address": "string",
        "id": "integer",
        "name": "string",
        "owner": {
          "email": "string",
          "id": "integer",
          "name": "string",
          "role": "string",
          "username": "string"
        },
        "restaurant_number": "integer"
      }
    ]
  }
}
```
---

## Endpoint: POST  /restaurants/
**Authentication:** No Auth needed __FOR NOW__

### Request
```JSON
{
  "owner_id" : "integer: greater than 0",
  "name" : "string: min 3",
  "address" : "string: min 3",
  "restaurant_number" : "integer: greater than 0"
}
```

### Response
```javascript
{
  "status" : "success or error",
  "message" : "message of some kind both success or fail",
  "errors" : { //only if there are errors
    "key" : ["error messages"], // if error
  },
  "data" : {
    "restaurant" : {
      "address": "string",
      "id": "integer",
      "name": "string",
      "restaurant_number": "integer"
    }
  }
}
```
---

## Endpoint: GET  /restaurants/<int:restaurantId>

**Authentication:** No Auth needed __FOR NOW__


### Response
```javascript
{
  "status" : "success or error",
  "message" : "message of some kind both success or fail",
  "errors" : { //only if there are errors
    "key" : ["error messages"], // if error
  },
  "data" : {
    "restaurant" : {
      "address": "string",
      "id": "integer",
      "name": "string",
      "restaurant_number": "integer"
    }
  }
}
```
---

## Endpoint: PUT  /restaurants/<int:restaurantId>
**Authentication:** No Auth needed __FOR NOW__

### Request
```JSON
{
  "owner_id" : "integer: greater than 0",
  "name" : "string: min 3",
  "address" : "string: min 3",
  "restaurant_number" : "integer: greater than 0"
}
```

### Response
```javascript
{
  "status" : "success or error",
  "message" : "message of some kind both success or fail",
  "errors" : { //only if there are errors
    "key" : ["error messages"], // if error
  },
  "data" : {
    "restaurant" : {
      "address": "string",
      "id": "integer",
      "name": "string",
      "restaurant_number": "integer"
    }
  }
}
```
---

## Endpoint: DELETE  /restaurants/<int:restaurantId>

**Authentication:** No Auth needed __FOR NOW__


### Response
```javascript
{
  "status" : "success or error",
  "message" : "message of some kind both success or fail",
  "errors" : { //only if there are errors
    "key" : ["error messages"], // if error
  }
}
```
