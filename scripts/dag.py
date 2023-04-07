import subprocess
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'PetroSensor',
    default_args=default_args,
    catchup=False,
    schedule_interval=None
)

start_api_script = BashOperator(
    task_id='start_api_script',
    bash_command='python /Users/gomes/Desktop/Projects/Data\ Engineer/2-Project/scripts/api.py > /dev/null 2>&1 &',
    dag=dag
)

# Add a sleep command to pause for 1 minute
sleep_task = BashOperator(
    task_id='sleep_task',
    bash_command='sleep 60',
    dag=dag
)

send_to_els_task = BashOperator(
    task_id='send_to_els',
    bash_command='python /Users/gomes/Desktop/Projects/Data\ Engineer/2-Project/scripts/s3_to_els.py',
    dag=dag
)

start_api_script >> sleep_task >> send_to_els_task
