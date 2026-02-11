from pipeline.bbc_pipeline import run_bbc_pipeline
import logging

logging.basicConfig(level=logging.INFO)

def run_daily_job():
    logging.info("Daily adverse media job started")
    run_bbc_pipeline()
    logging.info("Daily adverse media job finished")
