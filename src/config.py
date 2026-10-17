"""Pin service configuration."""
from vendor.ratelib import RateLimiter

SERVICE_NAME = "pinsvc"
MAX_EVENTS_PER_SEC = 180
BURST_CAPACITY = 400

limiter = RateLimiter(BURST_CAPACITY, MAX_EVENTS_PER_SEC)
