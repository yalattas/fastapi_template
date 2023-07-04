import subprocess

def run_alembic_migrations():
    subprocess.run(["alembic", "upgrade", "head"], check=True)

if __name__ == "__main__":
    run_alembic_migrations()
