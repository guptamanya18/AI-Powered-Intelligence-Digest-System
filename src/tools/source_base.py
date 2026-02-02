from abc import ABC, abstractmethod

class SourceAdapter(ABC):

    @abstractmethod
    async def fetch_items(self, hours: int = 24) -> list[dict]:
        pass
