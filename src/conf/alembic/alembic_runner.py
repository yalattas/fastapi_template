# import subprocess
# from fastapi import BackgroundTasks

# # job
# def run_alembic_migrations():
#     subprocess.run(["alembic", "upgrade", "head"], check=True)

# # run background job
# def run_migrations(background_tasks: BackgroundTasks):
#     background_tasks.add_task(run_alembic_migrations)

# if __name__ == "__main__":
#     run_alembic_migrations()
