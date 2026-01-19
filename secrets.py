import os
import json
import boto3


def get_database_credentials():
    """
    Recupera as credenciais do banco de dados
    armazenadas no AWS Secrets Manager.
    """

    secret_name = os.getenv("RDS_SECRET_NAME")
    region_name = os.getenv("AWS_REGION", "us-east-1")

    if not secret_name:
        raise RuntimeError("Variável de ambiente RDS_SECRET_NAME não definida")

    client = boto3.client(
        service_name="secretsmanager",
        region_name=region_name
    )

    response = client.get_secret_value(
        SecretId=secret_name
    )

    secret = json.loads(response["SecretString"])

    return {
        "username": secret["username"],
        "password": secret["password"],
        "host": secret["host"],
        "port": secret.get("port", 5432),
        "database": secret["dbname"]
    }
