from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
import json

with DAG(dag_id='poc_airbyte_airflow',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
         ) as dag:

    airbyte_economy_s3_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_economy_s3',
        airbyte_conn_id='airbyte_connection',
        connection_id='0129d278-7add-4a4d-b166-8e9b4852fafe',
        timeout=3600
    )
	
    airbyte_index_s3_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_index_s3',
        airbyte_conn_id='airbyte_connection',
        connection_id='0130d278-7add-4a4d-b561-8e9b4852atab',
        timeout=3600
    )

    airbyte_demographics_s3_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_demographics_s3',
        airbyte_conn_id='airbyte_connection',
        connection_id='3400d278-8bjj-3d4d-n861-9ak14852k3k3',
        timeout=3600
    )

    airbyte_epidemiology_s3_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_epidemiology_s3',
        airbyte_conn_id='airbyte_connection',
        connection_id='9010d278-7okd-4a9d-b534-3m54k4852yayb',
        timeout=3600
    )


    airbyte_economy_s3_sync >> airbyte_index_s3_sync >> airbyte_demographics_s3_sync >> airbyte_epidemiology_s3_sync
