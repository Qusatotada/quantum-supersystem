import subprocess
from src.config.settings import AUTO_COMMIT_MESSAGE
from src.logger import logger

def has_changes():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip() != ""

def commit_and_push():
    if not has_changes():
        logger.info("No changes detected. Skipping commit.")
        return

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", AUTO_COMMIT_MESSAGE])
    subprocess.run(["git", "push"])

    logger.info("Changes committed and pushed.")
