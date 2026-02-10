from pipeline.bbc_pipeline import run_bbc_pipeline

def run_daily_job():
    print("Daily adverse media job started")
    run_bbc_pipeline()
    print("Daily adverse media job finished")
