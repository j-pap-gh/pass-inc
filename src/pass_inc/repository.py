from typing import Dict, List

from .models import IncomeStream, IncomeStreamCreate


class IncomeRepository:
    """Simple in-memory repository. Replace with real DB later."""

    def __init__(self) -> None:
        self._streams: Dict[int, IncomeStream] = {}
        self._next_id = 1

    def list_streams(self) -> List[IncomeStream]:
        return list(self._streams.values())

    def add_stream(self, payload: IncomeStreamCreate) -> IncomeStream:
        stream = IncomeStream(id=self._next_id, **payload.dict())
        self._streams[self._next_id] = stream
        self._next_id += 1
        return stream

    def delete_stream(self, stream_id: int) -> None:
        if stream_id in self._streams:
            del self._streams[stream_id]
        else:
            raise KeyError(f"Income stream {stream_id} not found")


# Singleton for now; for real apps use dependency injection
income_repo = IncomeRepository()
