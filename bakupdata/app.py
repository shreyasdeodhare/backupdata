from datetime import datetime
import os
import mysql.connector
import pytz
import time

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
        print(cursor)

        backup_file_path = os.path.join(backup_path, f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql")

        backup_command = f"mysqldump -h {host} -P {port} -u {username} -p{password} {database} > {backup_file_path}"

        os.system(backup_command)

        cursor.close()
        conn.close()

        print(f"MySQL database backup completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST")
    except Exception as e:
        print(f"An error occurred during MySQL database backup: {str(e)}")

# Define a function to schedule the backup process
def schedule_backup():
    while True:
        # Get the current time in IST
        current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
        # Set the time for 1:00 PM IST
        scheduled_time = current_time.replace(hour=13, minute=0, second=0, microsecond=0)

        # Check if the current time is equal to the scheduled time
        if current_time == scheduled_time:
            print(f"Starting backup process at {current_time.strftime('%Y-%m-%d %H:%M:%S')} IST")
            backup_mysql_db()
            # Wait for the next day
            time.sleep(86400)  # 86400 seconds = 24 hours
        else:
            # Calculate the time until the next scheduled backup
            time_until_next_backup = (scheduled_time - current_time).total_seconds()
            print(f"Next backup scheduled at {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')} IST. Waiting for {time_until_next_backup} seconds...")
            # Wait until the next scheduled backup time
            time.sleep(time_until_next_backup)

# Start the backup scheduling process
schedule_backup()