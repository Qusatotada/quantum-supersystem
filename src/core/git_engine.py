import subprocess
from src.logger import logger
from src.config.settings import AUTO_COMMIT_MESSAGE

def has_changes():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )
    return bool(result.stdout.strip())

def commit_and_push():
    try:
        if has_changes():
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", AUTO_COMMIT_MESSAGE], check=True)
            subprocess.run(["git", "push"], check=True)
            logger.info("Changes pushed successfully")
        else:
            logger.info("No changes detected")
    except Exception as e:
        logger.error(f"Git error: {e}")
