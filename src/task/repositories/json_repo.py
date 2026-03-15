import json
import logging

def load_tasks(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.info("File not found")
        return []
    except FileExistsError:
        logging.error("File not Exists")

def save_tasks(filename, tasks):
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)
            logging.info(f"{f} -- Saved")
    except FileExistsError:
        logging.error("Error save task File not Exists")
    except FileNotFoundError:
        logging.error("Error save task File not Found")