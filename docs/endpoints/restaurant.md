# Restaurant Module
---


## Endpoint: GET /restaurants/
**Authentication:** OWNER or ADMIN

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
**Authentication:** USER

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

## Endpoint: GET  /restaurants/{ int:restaurantId }

**Authentication:** USER


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

## Endpoint: PUT  /restaurants/{ int:restaurantId }
**Authentication:** OWNER.id == user.id  or ADMIN

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

## Endpoint: DELETE  /restaurants/{ int:restaurantId }

**Authentication:** OWNER.id == user.id or ADMIN


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
