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
	"id":1,
	"name":"David"
    },
    {
	"id":2,
	"name":"David"
    },
    {
	"id":3,
	"name":"Ola"
    },
    {
	"id":4,
	"name":"Ola"
    }
]
```

### GET /api/user_id
returns one person by ID

curl command:
```
curl https://twd-hng-crud-app.onrender.com/api/1
```

response:
```
[
    {
        "id":1,
        "name":"David"
    },
]
```
