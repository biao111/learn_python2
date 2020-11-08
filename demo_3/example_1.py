from mongo_db import client
client.school.teacher.insert_one({"name":"李璐"})
client.school.teacher.insert_many([
    {"name":"李刚"},
    {"name":"郭丽丽"}
])
client.school.student.insert_many([
    {"name":"Scott","age":"24","city":"Beijing","class":"2-1"},
    {"name":"刘娜","age":"23","city":"Beijing","class":"2-2"},
    {"name":"陈浩","age":"23","city":"Beijing","class":"2-3"},
    {"name":"赵婷婷","age":"22","city":"Beijing","class":"2-4"},
    {"name":"韩梅梅","age":"21","city":"Beijing","class":"2-5"}

])