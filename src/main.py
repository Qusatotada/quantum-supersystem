import time
from src.git_engine import git_commit_and_push
from src.logger import logger

def main():
    logger.info("Quantum Supersystem started")
    print("Quantum Supersystem running...")
    while True:
        git_commit_and_push()
        time.sleep(30)

if __name__ == "__main__":
    main()
