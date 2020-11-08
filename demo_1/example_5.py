import mysql.connector.pooling

confing={
    "host":"localhost","port":"3306",
    "user":"root","password":"123456",
    "database":"demo"
}
try:
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **confing,
        pool_size=10
    )
    con=pool.get_connection()
    # con.start_transaction()
    cursor=con.cursor()
    # sql="DELETE e,d FROM t_emp e JOIN t_dept d ON e.deptno=d.deptno WHERE d.deptno=20"
    sql="TRUNCATE TABLE t_emp"
    cursor.execute(sql)
    con.commit()
except Exception as e:
    # if "con" in dir():
    #     con.rollback
    print(e)