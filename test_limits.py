from src.config import MAX_EVENTS_PER_SEC, BURST_CAPACITY


def test_burst_exceeds_rate():
    assert BURST_CAPACITY > MAX_EVENTS_PER_SEC
