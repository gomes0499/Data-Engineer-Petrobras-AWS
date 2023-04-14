# Data-Engineer - Petrobras - Study Case

## Petrobras
The proposed data engineering pipeline will ingest, process, and analyze real-time sensor data from Petrobras' oil and gas pipelines. The pipeline will monitor the data and optimize maintenance schedules. This project will enhance Petrobras' ability to proactively address potential issues and improve overall operational efficiency.

### Data Pipeline Steps
1. Terraform was used to provision the cloud infrastructure required for the pipeline.
2. GitHub Actions served as a CI/CD platform for the Terraform infrastructure.
3. Python was used to generate streaming dummy data for Petrobras sensors in JSON format.
4. The generated data was put into a Kinesis Data Stream.
5. Kinesis Firehose consumed Kinesis Data Stream as a source and stored the data into Data Lake S3.
6. Docker was used to deploy Airflow, ElasticSearch, and Kibana.
7. A Python script was used to read the contents of the Data Lake and load it into ElasticSearch.
8. Kibana was used to monitor the sensor data and create dashboards for operational efficiency.
9. Finally, the entire pipeline was orchestrated using Apache Airflow, deployed on a container.

### Pipeline Diagram
![alt text](https://github.com/makima0499/2.Data-Engineer/blob/main/2.DataPipeline.png)

### Tools
* Python
* Airflow
* Terraform
* Github Actions
* Docker
* AWS Kinesis Data Stream
* AWS Kinesis Firehose
* AWS S3
* ElasticSearch
* Kibana

### Note
This repository is provided for study purposes only, focusing on data engineering pipelines.

## License

[MIT](https://choosealicense.com/licenses/mit/)
