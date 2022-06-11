import pymysql
from config import HOST, PORT, USER, PASSWORD, DB_NAME


try:
    connection = pymysql.connect(
        host = HOST,
        port = PORT,
        user = USER,
        password = PASSWORD,
        database = DB_NAME,
        cursorclass = pymysql.cursors.DictCursor
    )
    print('Connection success')
    try:
        with connection.cursor() as cursor:
            request = "SELECT COUNT('МРТ за 2020 год')"\
                      " FROM action INNER JOIN actiontype ON action.action_type = actiontype.id"\
                      " WHERE actiontype.name = 'МРТ' AND action.beg_date BETWEEN '2020-01-01' and '2020-12-31';"
            cursor.execute(request)
            rows = cursor.fetchall()
            for row in rows:
                print(f'Response: {row}')
    finally:
        connection.close()
except Exception as ex:
    print('Connection failed')
    print(ex)
