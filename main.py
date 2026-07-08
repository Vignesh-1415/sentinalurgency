"""Entry point for Railway deployment."""
import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

from database import app

if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.getenv("PORT", 8000))
    host = "0.0.0.0"
    
    uvicorn.run(app, host=host, port=port)
