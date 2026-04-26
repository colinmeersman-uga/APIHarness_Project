import yaml
import requests
import logging
import sys

# 1. Configure Observable Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("api_test.log"),  # Saves to a file
        logging.StreamHandler(sys.stdout)     # Prints to the console
    ]
)
logger = logging.getLogger(__name__)

def load_config(filepath="config.yaml"):
    """Reads the YAML configuration file and handles potential errors."""
    try:
        with open(filepath, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logger.error(f"Configuration file not found: {filepath}")
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        sys.exit(1)

def run_harness():
    """Main execution flow for the API harness."""
    logger.info("Starting API Test Harness")

    # 2. Load the configuration data
    config = load_config()
    base_url = config.get("base_url")
    default_headers = config.get("headers", {})
    endpoints = config.get("endpoints", [])

    if not base_url:
        logger.error("No base_url found in configuration.")
        sys.exit(1)

    # 3. Iterate through endpoints and construct requests
    for endpoint in endpoints:
        path = endpoint.get("path")
        method = endpoint.get("method", "GET").upper()
        body = endpoint.get("body", None)
        
        url = f"{base_url}{path}"
        logger.info(f"--- Sending {method} request to {url} ---")
        
        try:
            # requests.request dynamically handles GET, POST, PUT, DELETE, etc.
            response = requests.request(
                method=method,
                url=url,
                headers=default_headers,
                json=body # Auto-converts Python dictionaries to JSON strings
            )
            
            # 4. Log the results
            logger.info(f"Status Code: {response.status_code}")
            logger.info(f"Response Body: {response.text[:300]}...\n") 
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")

    logger.info("API Test Harness execution completed.")

if __name__ == "__main__":
    run_harness()