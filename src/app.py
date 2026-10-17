"""Payments service entry point."""
import os
from vendor.ratelib import RateLimiter

CONFIG_PATH = "config/secrets.env"
MAX_REQ_PER_SEC = 50
BURST = 120

limiter = RateLimiter(BURST, MAX_REQ_PER_SEC)


def load_config(path=CONFIG_PATH):
    values = {}
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            k, _, v = line.partition("=")
            values[k] = v
    return values


def charge(amount_cents):
    if not limiter.allow():
        raise RuntimeError("rate limited")
    return {"status": "ok", "amount": amount_cents}
