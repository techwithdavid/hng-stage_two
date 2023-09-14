# Endpoints

### GET /api
returns all persons

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
	"name": "David"
    },
    {
	"id": 3,
	"name": "Ola"
    },
    {
	"id": 4,
	"name": "Ola"
    }
]
```

### GET  /api/user_id
returns one person by ID

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

### POST    /api
Adds a new person to the database

curl command
```
curl -H "Content-Type: application/json" -X POST -d '{"name": "Techwithdavid"}' https://twd-hng-crud-app.onrender.com/api
```

response:
```
{
    "status": "Successful"
}
```
