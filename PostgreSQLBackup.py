import subprocess
import datetime


def backup_postgresql_db(host, port, username, password, database, backup_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{database}_{timestamp}.sql"

    # Construct the pg_dump command
    pg_dump_cmd = [
        'pg_dump',
        '-h', host,
        '-p', str(port),
        '-U', username,
        '-d', database,
        '-Fc',  # Custom format
        '-f', backup_filename,
    ]

    # Add password if provided
    if password:
        pg_dump_cmd.extend(['-W', password])

    try:
        # Run the pg_dump command
        subprocess.run(pg_dump_cmd, check=True)
        print(f"Backup completed successfully. Backup file: {backup_filename}")

    except subprocess.CalledProcessError as e:
        print(f"Backup failed. Error: {e}")


if __name__ == "__main__":
    # Replace these values with your PostgreSQL connection details
    host = 'localhost'
    port = 5432
    username = 'your_username'
    password = 'your_password'
    database = 'your_database'

    # Specify the directory where you want to store the backup file
    backup_path = '/path/to/backup/directory/'

    backup_postgresql_db(host, port, username, password, database, backup_path)
