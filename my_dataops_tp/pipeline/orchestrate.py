from dagster import job, op
import os

@op
def ingest():
    """Runs the ingestion script"""
    return_code = os.system("python pipeline/ingest.py")
    if return_code != 0:
        raise Exception("Ingestion failed")

@op
def validate(ingest_done):
    """Runs the validation script"""
    return_code = os.system("python pipeline/validate.py")
    if return_code != 0:
        raise Exception("Validation failed")

@op
def transform(validate_done):
    """Runs dbt transformation"""
    # We must go into the folder to run dbt
    return_code = os.system("cd dbt_pipeline && dbt run --profiles-dir .")
    if return_code != 0:
        raise Exception("dbt transformation failed")

@op
def test_data(transform_done):
    """Runs dbt tests"""
    return_code = os.system("cd dbt_pipeline && dbt test --profiles-dir .")
    if return_code != 0:
        raise Exception("dbt tests failed")

@job
def ventes_pipeline():
    # This defines the order: Ingest -> Validate -> Transform -> Test
    test_data(transform(validate(ingest())))