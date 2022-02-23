"""Application entry point."""

import os

from .api.main import run


HOST = os.environ.get("HOST", "localhost")
PORT = int(os.environ.get("PORT", 8000))


if __name__ == "__main__":
    run(HOST, PORT)
