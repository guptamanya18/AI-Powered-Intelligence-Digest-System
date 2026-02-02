from src.services.database import Database
from src.utils.loggers import log_info, log_step
from src.services.filtering import PreFilterService
import asyncio

class IngestionService:

    def __init__(self, adapters: list):
        self.db = Database()
        self.adapters = adapters
        self.filter = PreFilterService()

    async def run(self):
        log_step("Starting ingestion pipeline")

        for adapter in self.adapters:
            log_info(f"Fetching from {adapter.__class__.__name__}")
            items = await adapter.fetch_items()

            filtered_items = self.filter.apply(items)
            log_info(f"Filtered {len(filtered_items)} relevant items")

            for item in filtered_items:
                self.db.insert_item(item)

        log_info("Ingestion completed")

    def run_sync(self):
        
        asyncio.run(self.run())

