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
  "user": "Your gmail mail",
  "password": "password for gmail mail",
  "SECRET_KEY": "Your secret app key",
}
```
Next step is to migrate data and initialize database from backend\src directory

```
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

If you want to run unit tests
```
python3 manage.py test
```

First install all npm packages
```npm
npm i
```

To run frontend application
```npm
npm run serve
```

## Database

The database consists of four main collections.

1. Users collection

Example document
```
{
    "_id" : ObjectId("5edd34f030698aae6284e52a"),
    "id" : 1,
    "password" : "pbkdf2_sha256$150000$SxUiEQph53yd$nrqSKPR0jNB6nORvFJbnwMwSUGDZANjE4fNaFq0HdkU=",
    "last_login" : ISODate("2020-06-07T18:42:37.858Z"),
    "is_superuser" : true,
    "is_staff" : true,
    "is_active" : true,
    "date_joined" : ISODate("2020-06-07T18:41:51.786Z"),
    "first_name" : "John",
    "last_name" : "Tester",
    "email" : "test@test.com",
    "is_lecture" : true,
    "is_student" : true
}
```

2. Group collection

Example document
```
{
    "_id" : ObjectId("5edf6c3a842d5e7cdf572ed9"),
    "id" : 1,
    "course" : "Python",
    "date_time" : [ 
        {
            "day_of_week" : "Monday",
            "time" : ISODate("1900-01-01T12:50:00.000Z")
        }
    ],
    "lectures_list" : [ 
        {
            "lecture_id" : 1,
            "main_lecture" : true
        }
    ],
    "enrolled_list" : [ 
        {
            "student_id" : 2,
            "inattendances_list" : [ 
                {
                    "class_num" : 2,
                    "justified" : true
                }
            ],
            "marks_list" : [ 
                {
                    "value" : 50,
                    "max_points" : 100,
                    "for_what" : "Exam",
                    "note" : "Luckily"
                }
            ],
            "final_grade" : null
        }
    ],
    "course_end" : false
}
```

3. Lecture Groups


Example document
```
{
    "_id" : ObjectId("5edf6c3a842d5e7cdf572eda"),
    "id" : 1,
    "user_id" : 1,
    "groups_list_id" : [ 
        1
    ]
}
```

4. Student Groups

Example document
```
{
    "_id" : ObjectId("5ee5f1e83931ad637f50e76b"),
    "id" : 1,
    "user_id" : 2,
    "groups_list_id" : [ 
        1
    ]
}
```

## Backend details

Short description of all REST API endpoints for GET request method
| resource                  | description                   |
|:--------------------------|:------------------------------|
| `/api/users/`              |returns list of all server users       |
| `/api/users/info/`         |returns information about who is user (student/lecture/admin)                               |
| `/api/users/{"students"/"lectures"}/`         |returns list of all students/lectures                               |
| `/api/groups/`             |returns list of groups with basic information about them                               |
| `/api/groups/stats/`       |returns stats from groups which ids are sended in request and link to historgram of average data|
| `/api/groups/{group_id}`   |returns data about this group                                |
| `/api/lecturesGroups/`           |returns list of groups in which user who send request is or was lecture                               |
| `/api/lecturesGroups/list/{user_id}`      |returns list of groups of specified user in which he is or was lecture                               |
| `/api/studentsGroups/`           |returns list of groups in which user who send request is or was student                               |
| `/api/studentsGroups/list/{user_id}`      |returns list of groups of specified user in which he is or was student                               |
| `/api/token/`              |return access token and refresh token to REST API server                               |


Short description of endpoints for other request method

| url                       | description                   |
|:--------------------------|:------------------------------|
| `/api/users/`              |POST - add user to database       |
| `/api/users/{user_id}`     |PATCH - Change info about user permissions         |
| `/api/groups/{group_id}`   |PATCH - update info about this group                                |
| `/api/groups/{group_id}/markAll/`|POST - add mark for all student in group                                |
| `/api/groups/{group_id}/finalGrade/`|POST - calculate final grade for all students in group                                |
| `/api/groups/{group_id}/student/`|POST - add user to group as student who send request                                |
| `/api/token/refresh`       |POST - refresh access token before                        |
| `/api/mail/`               |POST - send mail to users included in request and with specified text                        |


### Implementation description

Backend is divided into apps. Apps contain models mapped to database, serializers for presenting data, and in api subfolders:
permissions, routing and views that expose REST interface.

#### Django Apps

| App                       | Description                   |
|:--------------------------|:------------------------------|
| HallOfFame             | Main component, holds routing, settings  |
| DayTime                | Holds information about class time       |
| Enrolled              | Entry of student in class       |
| Groups                 | Entry about a class, holds students and details      |
| Inattendance           | Holds information about inattendance       |
| Lecturer               | Entry of lecturer in class       |
| LectureGroups          | Holds list of groups of a lecturer       |
| Mail                   | Allows sending mails from app    |
| Marks                  | Holds single mark with details       |
| Media                  | Folder for exposing generated plots     |
| StudentGroups          | Holds list of groups of a student        |
| Users                  | Manages user details, used for authorization       |

## Frontend details

In app user can register to service, and login to it.
As student he can:
- sign up to listed groups, which he isn't already,
- in his groups he can see his marks and inattendances and send mail to lectures,

As lecture he can:
- create new group,
- add mark to specified student or for all student mark with the same name,
- add inattendance to specified student. 
- calculate final grade for all students 
- send mail to specified students.



