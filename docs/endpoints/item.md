# Item Module

---

## Endpoint: POST /item/
### request:
```JSON
{
    "restaurant_id": "integer greater than 0",
    "name": "string between 2 and 50 characters",
    "cost": "float greater than 0",
    "description": "any length string",
    "category": "lowercase string written exactly"
}
```
### response:
```JavaScript
{
  "errors": ["error messages (if any)"]
  "data": {
    "added item": {
      "category": "string",
      "cost": "integer",
      "date_created": "DateTime",
      "description": "string",
      "id": integer,
      "name": "string"
    }
  },
  "message": "message to caller",
  "status": "success or error"
}
```

---

# Endpoint: GET   /item/
**Authroization:** MANAGER+ *(requred)*
## Response:
```JavaScript
{
  "error": ["list of errors, if any"]
  "data": [
    "List of items in the following form",
    "<Item 1 'string' 'float' 'string' 'Category' 'DateTime'>"
  ],
  "status": "success or error"
}
```

---

# Endpoint: GET   /item/<int>
**Authroization:** MANAGER+ *(requred)*
## Response:
```JavaScript
{
  "error": ["list of errors, if any"]
  "data": [
    "List of items in the following form",
    "<Item 1 'string' 'float' 'string' 'Category' 'DateTime'>"
  ],
  "status": "success or error"
}
```

---
# Endpoint: PUT /item/<int>
**Authorization:** MANAGER+ *(required)*
## request:
```JSON
{
    "restaurant_id": "integer",
    "name": "string between 2 and 50 characters",
    "cost": 12.99,
    "description": "white sauce with lovely aftertaste",
    "category": "dinner"
}
```JavaScript
{
  "data": {
    "category": "appetizer",
    "cost": 12.99,
    "date_created": "Sat, 31 Dec 2016 06:23:45 GMT",
    "description": "white sauce with lovely aftertaste",
    "id": 15,
    "name": "fettuccini alf"
  },
  "message": "updated item",
  "status": "success"
}
```

---

# Endpoint: DELETE /<int>
**Authorization:** MANAGER+ *(required)*
## request:
```JavaScript
{
  "error": ["list of errors, if any"],
  "message": "1 deleted from the database.",
  "status": "success or error"
}
```
