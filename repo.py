from dagster import job, op, repository


@op
def foo_op(_):
    pass


@job
def foo_job():
    foo_op()


@repository
def foo_repo():
    return [foo_job]
