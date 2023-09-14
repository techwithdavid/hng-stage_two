# Endpoints

### GET /api
Returns all persons

curl command:
```
curl https://twd-hng-crud-app.onrender.com/api
```

response:
```
[
    {
	"id": 1,
	"name": "David"
    },
    {
	"id": 2,
	"name": "Ola"
    },
    {
	"id": 3,
	"name": "Techwithdavid"
    }
]
```

### GET /api/user_id
Returns one person by ID

curl command:
```
curl https://twd-hng-crud-app.onrender.com/api/1
```

response:
```
{
    "id": 1,
    "name": "David"
}
```

### POST /api
Adds a new person to the database

curl command
```
curl -H "Content-Type: application/json" -X POST -d '{"name": "Techwithdavid"}' https://twd-hng-crud-app.onrender.com/api
```

response:
```
{
    "status": "Successful",
    "message": "Techwithdavid created successfully"
}
```

### PUT /api/user_id
Updates the name of a person by ID

curl command
```
curl https://twd-hng-crud-app.onrender.com/api/3 -X PUT -H "Content-Type: application/json" -d '{"name": "Techwithdavid"}'
```

response:
```
{
    "status": "Successful"
    "message": "Name of user with ID 3 changed to Techwithdavid"
}
```

### DELETE /api/user_id
Deletes a person by ID

curl command:
```
curl https://twd-hng-crud-app.onrender.com/api/5 -X DELETE
```

response:
```
{
    "status": "Successful"
    "message": "User with ID 5 deleted"})
}
```

# Deployment

This API is deployed on render and can be accessed [here](https://twd-hng-crud-app.onrender.com/api)
