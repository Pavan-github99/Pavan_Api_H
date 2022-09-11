def addSingleUser():
    body = {
        "id": 111222,
        "username": "pavan1",
        "firstName": "pavan2",
        "lastName": "dev1",
        "email": "jdsn1@gmail.com",
        "password": "pavan3",
        "phone": "04564554551",
        "userStatus": 1
    }
    return body

def addMultipleUsers():
    body = [
    {
        "id": 2,
        "username": "jdsn2",
        "firstName": "pavan4",
        "lastName": "dev2",
        "email": "pavan@gmail.com",
        "password": "pavan",
        "phone": "04564554552",
        "userStatus": 1
    },
    {
        "id": 3,
        "username": "jdsn3",
        "firstName": "pavan5",
        "lastName": "dev3",
        "email": "jdsn3@gmail.com",
        "password": "janardandev3",
        "phone": "04564554553",
        "userStatus": 1
    },
    {
        "id": 3,
        "username": "jdsn3",
        "firstName": "pavan6",
        "lastName": "dev3",
        "email": "jdsn3@gmail.com",
        "password": "janardandev3",
        "phone": "04564554553",
        "userStatus": 1
    }
]
    return body


def addmodifiedUser():
    body = {
  "id": 2,
  "username": "jdsn2",
  "firstName": "pavanupdated",
  "lastName": "dev2updated",
  "email": "jdsn2@gmail.com",
  "password": "pavanpass",
  "phone": "04564554552",
  "userStatus": 1}
    return body