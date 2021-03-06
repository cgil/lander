import os
import sys

from fabric.api import local
from fabric.api import task
from fabric.colors import green
from fabric.colors import red
from fabric.context_managers import settings

DEFAULT_ENV = 'development'


@task
def clean():
    """Remove all .pyc files."""
    print green('Clean up .pyc files')
    local("find . -name '*.py[co]' -exec rm -f '{}' ';'")


@task
def shell(env=DEFAULT_ENV):
    """Run the shell in the environment."""
    os.environ['CONFIG_ENV'] = './config/%s.yaml' % env
    local('python manage.py shell')


@task
def test(args='', env='test'):
    """Run tests."""
    os.environ['CONFIG_ENV'] = './config/%s.yaml' % env
    os.environ['ENV_NAME'] = env
    clean()
    print green('Running all tests')
    cmd = ('nosetests -d --verbosity 3 --with-id --nocapture %s' % args)

    with settings(warn_only=True, quiet=True):
        success = local(cmd).succeeded

    lint()

    if success:
        print(green('Tests finished running with success.'))
    else:
        print(red('Test finished running with errors.'))
        sys.exit(1)


@task
def lint():
    """Check for lints"""
    print green('Checking for lints')
    return local("flake8 `find . -name '*.py' -not -path '*env/*'` "
                 "--ignore=E711,E712 --max-line-length=100").succeeded


@task
def bootstrap(env=DEFAULT_ENV):
    """Bootstrap the environment."""
    os.environ['CONFIG_ENV'] = './config/%s.yaml' % env
    local('mkdir -p logs')
    print green('\nInstalling requirements')
    local('pip install -r requirements-test.txt')
    local('pip install -r requirements-development.txt')
    local('pip install -r requirements.txt')
    local('python setup.py develop')


@task
def serve(env=DEFAULT_ENV):
    """Start the server."""
    os.environ['ENV_NAME'] = env
    local('python app.py')
