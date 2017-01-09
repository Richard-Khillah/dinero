# Bill Module
---


## Endpoint: GET /bills/
**Authentication:** ADMIN

### Response
```javascript
{
  "status": "success or error",
  "errors" : {// if errors
    "key" : ["values"]
  },
  "meta": {
    "page": "int: current page",
    "pages": "int: total number of pages",
    "total": "int: total documents in table"
  },
  "data": {
    "bills": [
      {
        "created_at": "string:time created",
        "updated_at": "string:time updated",
        "id": "int",
        "message": "string: testing",
        "paid": "boolean",
        "num_of_items": "int: number of items on bill",
        "receipt_number": "string"
      }
    ]
  }
}
```
---


## Endpoint: GET bills/restaurant/{ int:restaurantId }
**Authentication:** SERVER+

### Response
```javascript
{
  "status": "success or error",
  "errors" : { // if errors
    "key" : ["values"]
  },
  "meta": {
    "page": "int: current page",
    "pages": "int: total number of pages",
    "total": "int: total documents in table"
  },
  "data": {
    "bills": [
      {
        "created_at": "string:time created",
        "updated_at": "string:time updated",
        "id": "int",
        "message": "string: testing",
        "paid": "boolean",
        "num_of_items": "int: number of items on bill",
        "receipt_number": "string"
      }
    ],
    "restaurant": {
      "address": "string",
      "id": "int",
      "name": "string",
      "restaurant_number": "int"
    }
  }
}
```
---

## Endpoint: POST bills/restaurant/{ int:restaurantId }
**Authentication:** SERVER+

### Request
```javascript
{
  "customer_id" : "int > 0",
  "receipt_number" : "string: max=120",
  "paid" : "boolean",
  "message" : "string: max=120", // optional
  "items" : ["int > 0"] // optional
}
```


### Response
```javascript
{
  "status": "success or error",
  "errors" : {// if errors
    "key" : ["values"]
  },
  "data": {
    "bill": {
      "created_at": "string:time created",
      "updated_at": "string:time updated",
      "id": "int",
      "message": "string: testing",
      "paid": "boolean",
      "receipt_number": "string"
    },
    "items" : [
      {
        "category": "string",
        "cost": "int",
        "date_created": "datetime",
        "description": "string",
        "id": "int",
        "name": "string"
      }
    ]  
  }
}
```

---

## Endpoint: GET /bills/{ int:billId }
**Authentication:** CUSTOMER == CUSTOMER_ID or SERVER+

### Response
```javascript
{
  "status": "success or error",
  "errors" : {// if errors
    "key" : ["values"]
  },
  "data": {
    "bill": [
      {
        "created_at": "string:time created",
        "updated_at": "string:time updated",
        "id": "int",
        "message": "string: testing",
        "paid": "boolean",
        "receipt_number": "string"
      }
    ],
    "items" : [
      {
        "category": "string",
        "cost": "int",
        "date_created": "datetime",
        "description": "string",
        "id": "int",
        "name": "string"
      }
    ]
  }
}
```
---

## Endpoint: PUT /bills/{ int:billId }
**Authentication:** SERVER+

### Request
```javascript
{
  "customer_id" : "int > 0",
  "receipt_number" : "string: max=120",
  "paid" : "boolean",
  "message" : "string: max=120", // optional
  "items" : ["int > 0"] // optional
}
```


### Response
```javascript
{
  "status": "success or error",
  "errors" : {// if errors
    "key" : ["values"]
  },
  "data": {
    "bill": {
      "created_at": "string:time created",
      "updated_at": "string:time updated",
      "id": "int",
      "message": "string: testing",
      "paid": "boolean",
      "receipt_number": "string"
    },
    "items" : [
      {
        "category": "string",
        "cost": "int",
        "date_created": "datetime",
        "description": "string",
        "id": "int",
        "name": "string"
      }
    ]  
  }
}
```

---

## Endpoint: DELETE /bills/{ int:billId }
**Authentication:** SERVER+

### Response
```javascript
{
  "status": "success or error",
  "errors" : {// if errors
    "key" : ["values"]
  },
}
```
