#!/usr/bin/env python3
import subprocess
import sys
import os

def run_server():
    """
    Run the FastAPI application using uvicorn with reload enabled.
    """
    try:
        # Get the absolute path to the project root
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Change to the project root directory
        os.chdir(project_root)
        
        # Run uvicorn with the specified configuration
        subprocess.run([
            "uvicorn",
            "app.main:app",
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error running server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_server() 