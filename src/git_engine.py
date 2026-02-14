import subprocess
from src.logger import logger

def git_commit_and_push():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto update"], check=False)
        subprocess.run(["git", "push"], check=True)
        logger.info("Changes pushed successfully")
    except Exception as e:
        logger.error(f"Git error: {e}")
