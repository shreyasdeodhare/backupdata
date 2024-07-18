# from datetime import datetime, timedelta
# import time
# import os
# import mysql.connector
#
# host = '172.25.128.1'
# port = 3306
# username = 'root'
# password = 'shreyas'
# database = 'ecommerce'
#
# backup_path = 'D:\\airflow_tut'
#
# def backup_mysql_db():
#     try:
#         conn = mysql.connector.connect(
#             host=host,
#             port=port,
#             user=username,
#             password=password,
#             database=database
#         )
#
#         cursor = conn.cursor()
#         print(cursor)
#
#         backup_command = f"mysqldump -h {host} -P {port} -u {username} -p{password} {database} > {backup_path}/backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql"
#
#         os.system(backup_command)
#
#         cursor.close()
#         conn.close()
#
#         print("MySQL database backup completed successfully!")
#     except Exception as e:
#         print(f"An error occurred during MySQL database backup: {str(e)}")
#
# backup_mysql_db()
#


from datetime import datetime
import time
import os
import mysql.connector

host = '172.25.128.1'
port = 3306
username = 'root'
password = 'shreyas'
database = 'ecommerce'

backup_path = 'D:\\airflow_tut'

def backup_mysql_db():
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database
        )

        cursor = conn.cursor()

        backup_file_name = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql"
        backup_command = f"mysqldump -h {host} -P {port} -u {username} -p{password} {database} > {backup_path}/{backup_file_name}"

        os.system(backup_command)

        cursor.close()
        conn.close()

        print(f"MySQL database backup '{backup_file_name}' completed successfully!")
    except Exception as e:
        print(f"An error occurred during MySQL database backup: {str(e)}")

# Specify the interval for backups in seconds
backup_interval =10  # One hour

while True:
    backup_mysql_db()
    print(f"Waiting for next backup in {backup_interval} seconds...")
    time.sleep(backup_interval)
