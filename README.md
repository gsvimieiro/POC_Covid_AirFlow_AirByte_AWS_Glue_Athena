# Poc_Covid_AirFlow_AirByte_AWS_Glue_Athena

Este pequeno projeto foi baseado no curso ministrado pelo Giuliano Ferreira (Data Engineering usando a Modern Data Stack da Stack Academy - https://stack-academy.memberkit.com.br/)

Estudo de caso COVID utilizando Airbyte para extração, Airflow como orquestrador, AWS Glue/Krawler para catalogar, inferir o schema e realizar transformação e por fim Athena para análise. 

![image](https://github.com/gsvimieiro/POC_Covid_AirFlow_AirByte_AWS_Glue_Athena/assets/25323854/238e1e48-fe31-40ff-84b3-82bd0f593450)


- Observação importante : Neste exemplo, por ser mais didático eu não estou preocupado com Segurança pois meu intuíto é mostrar o funcionamento de ponta a ponta da minha solução, então, questões como secret's, bucket privado, etc eu não adotei

Tecnologias utilizadas :

- DrawIO: Desenho da arquitetura
- GitHub: Repositório do projeto
- GitPod: Desenvolvimento das DAGS, etc
- Docker: Imagens e containers
- Airbyte: Extrator dos arquivos para o projeto
- Airflow: Orquestração das Pipelines do Airbyte
- AWS Glue/Krawler: Catalogar, inferir schema e as transformações
- AWS Athena: Análise dos dados

Tarefas :

- Setar permissões do Gitpod para o GitHub - OK
- Subir Airbyte via Docker - OK
    - Dar fork no github do airbyte, criar uma branch (branch_airbyte)
    - git clone -b branch_airbyte https://github.com/gsvimieiro/airbyte.git

- Subir Airflow via Docker - OK
- Criar conta na AWS - OK
- Na AWS
    - Criar o repositório OK
    - Criar dentro do repositorio as pastas raw e processed OK
- No Airbyte :
    - Preparar a extração dos CSV's COVID  OK
    - Configurar o target S3 OK
- No Airflow :
    - Criar as DAG'S de orquestração
    - Instalar a lib para conexão Airbyte
        - procurar o container airflow-airflow-webserver 
        - botao direito --> Attach Shell
        - pip install apache-airflow-providers-airbyte
        - restarta o container
- No Docker :
    - Criar uma rede no docker ex.: poc-airbyte-airflow
        - docker network create poc-airbyte-airflow
    - Adicionar os containers nesta rede 
        - docker network connect poc-airbyte-airflow airbyte-proxy
        - docker network connect poc-airbyte-airflow airbyte-worker
        - docker network connect poc-airbyte-airflow airflow-airflow-worker-1
        - docker network connect poc-airbyte-airflow airflow-airflow-webserver-1

- Pode-se instalar a lib para conexão do airbyte/airflow 

    - docker-compose run airflow-webserver airflow connections add 'airbyte_connection' --conn-uri 'airbyte://airbyte-proxy:8000'

- AWS Glue Crawler:
    - Esta ferramenta irá classificar e inferir o schema dos arquivos Parquet (Economy, Index Demographics e Epidemiology), ao término ele irá catalogar todos os 4 arquivo no Data Catalog como na imagem abaixo :

![image](https://github.com/gsvimieiro/POC_Covid_AirFlow_AirByte_AWS_Glue_Athena/assets/25323854/40cc46b9-89e1-4c49-adb0-355e167a7239)
      
    - Com o Glue Crawler podemos fazer pequenas transformações como : eliminar colunas, trocar tipo de coluna, etc

- AWS Glue ETL

    - Ferramenta para criar ETL's completos e complexos visualmente e formando scripts

    Um exemplo visual :

![image](https://github.com/gsvimieiro/POC_Covid_AirFlow_AirByte_AWS_Glue_Athena/assets/25323854/14dca5e6-272f-4f1a-b2c0-b3280b30f94b)

Colocamos o Target do Script para gravar no diretório processed do S3
Após rodar o Script os arquivos Parquet's já gravados

![image](https://github.com/gsvimieiro/POC_Covid_AirFlow_AirByte_AWS_Glue_Athena/assets/25323854/ee53f3aa-ff12-407c-8a65-f06368ff188f)

Após o processamento, iremos novamente editar o nosso Crawler inserindo o schema da tabela recem processada  no S3

![image](https://github.com/gsvimieiro/POC_Covid_AirFlow_AirByte_AWS_Glue_Athena/assets/25323854/bb55dc96-20a0-4cb5-b8eb-c4536fdf6bc9)


- AWS Athena
  


    


