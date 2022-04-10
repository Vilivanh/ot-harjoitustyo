from invoke import task

@task
def start(ctx):
    ctx.run("python src/budget.py", pty = True)

@task
def test(ctx):
    ctx.run("pytest src", pty = True)

@task
def coverage_report(ctx):
    ctx.run("coverage html", pty = True)