import fire

from jcci.analyze import JCCI


def compare_branch(git_url, username, first_branch, second_branch):
    branch_analyze = JCCI(git_url, username)
    branch_analyze.analyze_two_branch(first_branch, second_branch)


def cli():
    return fire.Fire({
        'compare': compare_branch
    })

cli()