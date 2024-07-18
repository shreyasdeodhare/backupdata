from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from your_python_script import backup_postgresql_db

# Replace these values with your PostgreSQL connection details
host = 'localhost'
port = 5432
username = 'your_username'
password = 'your_password'
database = 'your_database'

# Specify the directory where you want to store the backup file
backup_path = '/path/to/backup/directory/'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 21, 18, 30, 0),  # 6:30 PM IST
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'postgresql_backup_dag',
    default_args=default_args,
    description='DAG to trigger PostgreSQL backup',
    schedule_interval='30 18 * * *',  # Daily at 6:30 PM IST
)

backup_task = PythonOperator(
    task_id='backup_postgresql_db_task',
    python_callable=backup_postgresql_db,
    op_kwargs={
        'host': host,
        'port': port,
        'username': username,
        'password': password,
        'database': database,
        'backup_path': backup_path,
    },
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()  # Uncomment if you want to use command-line features of the DAG
