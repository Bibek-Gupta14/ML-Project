import logging
import os
from datetime import datetime

# 1. Create a unique log file name based on current time
# Example: 12_14_2025_02_30_00.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create the path: current_directory/logs/12...log
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# 3. Create the folder if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 4. Set up the logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has been set up.")
