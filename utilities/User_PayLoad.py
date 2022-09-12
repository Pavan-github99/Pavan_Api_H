def addSingleUser():
    body = {
        "id": 111222,
        "username": "pavan1",
        "firstName": "pavan2",
        "lastName": "dev1",
        "email": "pavan1@gmail.com",
        "password": "pavan3",
        "phone": "04564554551",
        "userStatus": 1
    }
    return body

def addMultipleUsers():
    body = [
    {
        "id": 2,
        "username": "pavan3",
        "firstName": "pavan4",
        "lastName": "dev2",
        "email": "pavan@gmail.com",
        "password": "pavanpass",
        "phone": "04564554552",
        "userStatus": 1
    },
    {
        "id": 3,
        "username": "pavan4",
        "firstName": "pavan4",
        "lastName": "dev3",
        "email": "pavan4@gmail.com",
        "password": "pavanpass",
        "phone": "04564554553",
        "userStatus": 1
    },
    {
        "id": 3,
        "username": "pavan6",
        "firstName": "pavan6",
        "lastName": "dev3",
        "email": "pavan6@gmail.com",
        "password": "pavanpass",
        "phone": "04564554553",
        "userStatus": 1
    }
]
    return body


def addmodifiedUser():
    body = {
  "id": 2,
  "username": "pavan2",
  "firstName": "pavanupdated",
  "lastName": "dev2updated",
  "email": "pavan2@gmail.com",
  "password": "pavanpass",
  "phone": "04564554552",
  "userStatus": 1}
    return body