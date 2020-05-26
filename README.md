# Hall-of-Fame

## Introduction

Hall of fame is the service allowing lecturers to efficiently eneter marks received by students, students to see individual marks, and create aggegates of collected data.

This project consists from two parts. First part is backend application as REST API created in python with use of Django and Django Rest Framework, all data are stored in MongoDB database. To connect MongoDB to Django and still use Django ORM we use djongo connector. The second part is simple frontend application in Vue js.

## To run application

First you have to install requirements for backend, from backend directory.

```bash
pip3 install -r requirements.txt
```

Then you need to add file credentials.json in backend\src
You don't have to add user and password if you don't want send mail by this app.
```json
{
  "user": ### Your gmail mail,
  "password": ### password for gmail mail,
  "SECRET_KEY": ### Your secret app key,
}
```
Next step is to migrate data and initialize database

```python
python3 manage.py migrate
```

Finally you can run django server
```
python3 manage.py runserver
```

If you want to see django admin-page you have to create super-user
```
python3 manage.py createsuperuser
```

To run frontend application
```npm
npm run serve
```

## Backend details

Short description of all REST API endpoints for GET request method
| resource                  | description                   |
|:--------------------------|:------------------------------|
| `/api/users/`              |returns list of all server users       |
| `/api/users/info/`         |returns information about who is user (student/lecture/admin)                               |
| `/api/groups/`             |returns list of groups with basic information about them                               |
| `/api/groups/stats/`       |returns stats from groups which ids are sended in request and link to historgram of average data|
| `/api/groups/{group_id}`   |returns data about this group                                |
| `/api/lectures/`           |returns list of groups in which user who send request is or was lecture                               |
| `/api/lectures/list/`      |returns list of all lectures and groups in which they are or were lecture                               |
| `/api/students/`           |returns list of groups in which user who send request is or was student                               |
| `/api/students/list/`      |returns list of all lectures and groups in which they are or were lecture                               |
| `/api/token/`              |return access token and refresh token to REST API server                               |


Short description of endpoints for other request method

| url                       | description                   |
|:--------------------------|:------------------------------|
| `/api/users/`              |POST - add user to database       |
| `/api/users/{user_id}`     |UPDATE - Change info about user permissions         |
| `/api/groups/{group_id}`   |PATCH - update info about this group                                |
| `/api/groups/{group_id}/markAll/`|POST - add mark for all student in group                                |
| `/api/groups/{group_id}/finalGrade/`|POST - calculate final grade for all students in group                                |
| `/api/groups/{group_id}/student/`|POST - add user to group as student who send request                                |
| `/api/token/refresh`       |POST - refresh access token before                        |
| `/api/mail/`               |POST - send mail to users included in request and with specified text                        |



## Frontend details

In app user can register to service, and login to it.
After he is logged in, he can sign up to listed groups. In groups which he is include he can see his marks and inattendances and send mail to lectures.
Lecture can create new group, add mark to specified student or for all student mark with the same name. He can add inattendance to specified student. Calculate final grade for all students and send mail to specified students.



