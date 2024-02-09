# Poc_Covid_AirFlow_AirByte_AWS_Glue_Athena
Estudo de caso COVID utilizando Airbyte para extração, Airflow como orquestrador, AWS Glue/Krawler para catalogar, inferir o schema e realizar transformação e por fim Athena para análise. 

Tarefas :

- Setar permissões do Gitpod para o GitHub - OK
- Subir Airbyte via Docker - 
- Subir Airflow via Docker - 
- Criar conta na AWS - OK
- Na AWS
    Criar o repositório
    Criar dentro do repositorio as pastas raw e processed
- No Airbyte :
    Preparar a extração dos CSV's COVID
    Configurar o target S3
- No Airflow :
    Criar as DAG'S de orquestração
