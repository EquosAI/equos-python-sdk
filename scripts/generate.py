import subprocess
import sys
from pathlib import Path

API_URL = "http://localhost:3001/docs/v3-json"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "src/equos"


def generate_client():
    print("Generating Python API client...")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    try:
        command = [
            "openapi-python-client",
            "generate",
            "--url",
            API_URL,
            "--output-path",
            str(OUTPUT_DIR),
            "--overwrite",
            "--config",
            "openapi-python-client.yaml",
        ]

        subprocess.run(command, check=True)
        print("Client generated successfully!")

    except subprocess.CalledProcessError as e:
        print("Failed to generate client")
        sys.exit(e.returncode)


if __name__ == "__main__":
    generate_client()
