from invoke import task


@task()
def create(c):
    """
    Create test enviroenment
    """

    cmd = "virtualenv ./venv && source ./venv/bin/activate && pip install -r requirements.txt"
    c.run(cmd)


@task()
def remove(c):
    """
    Remove test enviroenment
    """

    cmd = "rm -rf ./venv"
    c.run(cmd)
