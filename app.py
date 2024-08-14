import uvicorn
from main import app
import os
from dotenv import load_dotenv

load_dotenv(override=True)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "127.0.0.1")
    uvicorn.run(app, host=host, port=port)
