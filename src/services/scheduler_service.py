import schedule
import time
from src.services.ingestion import IngestionService
from src.tools.hackernews import HackerNewsAdapter

class SchedulerService:
    def start(self, run_time: str):
        def job():
            print("⏰ Running daily GenAI digest job...")
            ingestion = IngestionService(
                adapters=[HackerNewsAdapter()]
            )
            ingestion.run_sync()  # we will add this method

        schedule.every().day.at(run_time).do(job)
        print(f"✅ Scheduler started. Daily run at {run_time}")

        while True:
            schedule.run_pending()
            time.sleep(30)
