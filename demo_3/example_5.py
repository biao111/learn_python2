from mongo_db import client

try:
    students = client.school.student.find({}).skip(0).limit(10)
    for one in students:
        print(one["_id"],one["name"])
    print("---------------")
    names = client.school.student.distinct("name")
    for one in names:
        print(one)
    print("---------------")
    students = client.school.student.find({}).sort([("name",-1)])
    for one in students:
        print(one["_id"],one["name"])
except Exception as e:
    print(e)