import csv
import os
from datetime import datetime

LOG_FILE = "logs/alerts.csv"

def log_event(ip, prediction, action):

    file_exists = os.path.exists(LOG_FILE)

    with open(
        LOG_FILE,
        "a",
        newline=""
    ) as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
                "time",
                "ip",
                "prediction",
                "action"
            ])

        writer.writerow([
            datetime.now(),
            ip,
            prediction,
            action
        ])