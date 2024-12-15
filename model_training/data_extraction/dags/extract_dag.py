from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import os
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 12, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Extract_historic_clp_usd_data.',
    default_args=default_args,
    description='extrae datos del banco central.',
    schedule_interval=timedelta(days=1),
)

task_start = BashOperator(
     task_id='start',
    bash_command='date', 
    dag=dag
)

get_historic_data = PythonOperator(
    task_id=f'get_historic_data',
    python_callable=lambda: os.system(f'python /opt/airflow/scripts/extract_historic_data.py /opt/airflow/scripts'),
    dag=dag,
)

task_start >> get_historic_data

