import os
from dotenv import load_dotenv

load_dotenv()

TITLE:   str | None = os.environ.get("TITLE")
VERSION: str | None = os.environ.get("VERSION")
