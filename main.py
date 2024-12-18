"""
TODO:
"""
import os
import shutil
import time
from datetime import datetime


def display_message(message, lck_filename="process.lck"):
    """Updates a log file with a message. Also adds to log file time that message was added.

    Args:
        message (str): Message being logged.
    """
    with open(lck_filename, "a+") as lock_file:
        print(message)
        lock_file.write(datetime.now().strftime("%Y:%m:%d - %H:%M:%S -- ") + message + "\n")


def main():
    log_filename = os.path.join("ARCHIVE", "LOG", datetime.now().strftime("%Y%m%d%H%M%S") + ".log")
    if os.path.exists("process.lck"):
        return

    with open("process.lck", "w+") as lock_file:
        lock_file.write("Process Running\n")

    display_message("Running download program.")
    os.system("py ascend.py")
    display_message("Running upload program.")
    os.system("py ascend_post.py")

    shutil.move("process.lck", log_filename)

    for log_file in os.listdir("LOG"):
        log_file = os.path.join("LOG", log_file)
        if time.time() - os.path.getmtime(log_file) > 3 * 30 * 24 * 60 * 60:
            os.remove(log_file)


if __name__ == "__main__":
    main()
