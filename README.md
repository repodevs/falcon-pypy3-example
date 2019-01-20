Example Falcon, Celery with PyPy3

### Build & Run the Services 
```
$ docker-compose up -d --build 
```

### Available REST API
**Very Recommened to test using `httpie` :)**

#### Ping Services
```
$ http GET 127.0.0.1:9099/ping
```

#### Create Task
```
$ http POST 127.0.0.1:9099/task/create number=4
```
you will get response like

```
{
    "data": {
        "task_id": "40aa7ec6-59a7-4c62-bd86-85a35e8e582d"
    },
    "status": "success"
}
```
and then

#### Check Task Status
```
$ http GET 127.0.0.1:9099/task/status/{TASK_ID}
```
if the task success, will get response

```
{
    "result": [
        0,
        1,
        1,
        2,
        3
    ],
    "status": "SUCCESS"
}
```

#### Create Book Data
```
$ http POST 127.0.0.1:9099/books author="Edi Santoso" name="Buku Apaan Ya" isbn=123321
```
you will get response

```
{
    "book_id": "5c4483e4225b4a0008523dba",
    "message": "book successfully created"
}
```
and you can check detail of the book using

#### Get Book Detail
```
$ http GET 127.0.0.1:9099/book/{BOOK_ID}
```
the response is like 

```
{
    "author": "Edi Santoso",
    "isbn": 123321,
    "name": "Buku Apaan Ya"
}
```

---
Another useful stuff

#### Run Tests
**NOTE: run the test as a module**
```
$ python -m book.test
```

#### Watch Task Status 
```
$ watch -n1 http GET 127.0.0.1:9099/task/status/{TASK_ID}
```

---
### Reference
[https://www.alibabacloud.com/blog/building-very-fast-app-backends-with-falcon-web-framework-on-pypy_594282](https://www.alibabacloud.com/blog/building-very-fast-app-backends-with-falcon-web-framework-on-pypy_594282)
[https://testdriven.io/blog/asynchronous-tasks-with-falcon-and-celery/](https://testdriven.io/blog/asynchronous-tasks-with-falcon-and-celery/)

