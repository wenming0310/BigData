import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='iris',
                             cursorclass=pymysql.cursors.DictCursor)
                             #cursorclass=pymysql.cursors.DictCurs表示以字典方式返回数据

try:
    with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #sql = "SELECT * FROM `iris_with_id` WHERE `id`=%s"
        sql = "SELECT * FROM `iris_with_id` WHERE `petal_width`>%s"
        #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        cursor.execute(sql, ('2.0',))
        #result = cursor.fetchone()
        result = cursor.fetchall()  #fetchall返回的是一个列表
        print(len(result))
        #print(result['id'])
        for each_r in result:
            print(each_r['id'])

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

    #with connection.cursor() as cursor:
    #    # Read a single record
    #    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #    cursor.execute(sql, ('webmaster@python.org',))
    #    result = cursor.fetchone()  #fetchall()
    #    print(result)
finally:
    connection.close()