from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta  # Ensure timedelta is imported

# Simple Python function that will run as a task
def my_task():
    print("Hello from Airflow! Task executed successfully.")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # Corrected here
}

# Create a DAG instance
with DAG(
    'simple_dag',
    default_args=default_args,
    description='A simple DAG that prints a message every minute',
    schedule_interval='* * * * *',  # Runs every minute
    start_date=datetime(2025, 4, 27),
    catchup=False,
) as dag:

    # Task definition
    task_1 = PythonOperator(
        task_id='print_message_task',
        python_callable=my_task,
    )

    task_1