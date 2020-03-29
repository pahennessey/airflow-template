from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
import airflow.utils.dates
from datetime import datetime

# create a dictionary of default typical args to pass to the dag
# default_args = {
#     'owner': 'patrick hennessey',
#     'depends_on_past': False,
#     'email': ['test@test.com'],
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1
# }

default_args = {
    'owner': 'patrick hennessey',
    'start_date': datetime(2019, 10, 24)
}


# define the dag
dag = DAG(dag_id='simple_bq_select',
          schedule_interval="*/2 * * * *",
          default_args=default_args,
          catchup=False
          )


def test_script(**kwargs):
    from google.cloud import bigquery

    q1 = 'select current_timestamp()'

    def return_data(query, projectid):
        client = bigquery.Client()
        return client.query(query, project=projectid).to_dataframe()

    return_data(query=q1, projectid='toptal.com:api-project-726361118046')
    print('This Test Script should be logged')

    return True


op = DummyOperator(task_id='dummy', dag=dag)

t1 = PythonOperator(task_id='execute_simple_function', dag=dag, python_callable=test_script, provide_context=True)

op >> t1
