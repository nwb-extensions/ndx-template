import re
import sys
import json
import os
import os.path
from email.utils import parseaddr

import cookiecutter.config
import cookiecutter.replay

PREF_NAMESPACE_REGEX = r'^[\-a-z]+$'
REQ_NAMESPACE_REGEX = r'^[\-_a-zA-Z0-9]+$'
REQ_VERSION_REGEX = r'^[\-_a-zA-Z0-9.+]+$'
GITHUB_USERNAME_REGEX = r'^[a-zA-Z\d](?:[a-zA-Z\d]|-(?=[a-zA-Z\d])){0,38}$'

namespace = """{{ cookiecutter.namespace }}"""
email = map(str.strip, """{{ cookiecutter.email }}""".split(','))
github_username = map(str.strip, """{{ cookiecutter.github_username }}""".split(','))
version = """{{ cookiecutter.version }}"""


def _validate():
    """
    Validate the namespace, email address, and github username.
    Exits if namespace does not start with "ndx" or has invalid characters.
    """
    warnings = []
    errors = []

    if namespace[:4] != 'ndx-':
        errors.append('The name of your NDX extension must start with "ndx-".')
    if not re.match(PREF_NAMESPACE_REGEX, namespace):
        warnings.append('It is recommended to use only lower-case '
                        'ASCII letters and hyphens in your namespace.')
    if not re.match(REQ_NAMESPACE_REGEX, namespace):
        # these are the rules for naming GitHub repositories, and we want the
        # name of the GitHub repository to match the name of the extension
        errors.append('Namespace can only have lower-case and upper-case ASCII'
                      ' letters, hyphens (-), and underscores (_).')
    for e in email:
        if '@' not in parseaddr(e)[1]:
            warnings.append(
                'The email address you entered "{email}" does not '
                'appear to be a valid email address. Are you sure you'
                ' entered it correctly?'.format(email=e)
            )
    for u in github_username:
        if not re.match(GITHUB_USERNAME_REGEX, u):
            warnings.append(
                'The GitHub username you entered "{u}" does not '
                'appear to be a valid GitHub username. Are you sure you '
                'entered it correctly?'.format(u=u)
            )
    if not re.match(REQ_VERSION_REGEX, version):
        errors.append('Version can only have lower-case and upper-case ASCII'
                      ' letters, hyphens (-), underscores (_), plus signs (+),'
                      ' and periods (.).')

    print('------------------------------------------------------------------')
    for w in warnings:
        print('WARNING: ' + w)

    for e in errors:
        print('ERROR: ' + e)

    if warnings or errors:
        print('\nTo re-run cookiecutter with your entered values as the '
              'defaults, run:')
        print('cookiecutter gh:nwb-extensions/ndx-template')
        print('BUT 1) when prompted to delete and re-download ndx-template, '
              'enter "no"')
        print('and 2) when prompted to re-use the existing version, '
              'enter "yes".\n')

    if errors:
        sys.exit(1)


def _write_new_defaults():
    """
    Overwrite the default values of the cached template with the values entered
    by the user. Overwrites only if cookiecutter downloads and caches the
    template from GitHub.
    """

    # the template name used by cookiecutter.replay is the name of the repo dir
    # this code assumes that the template repo was checked out into a dir
    # called "ndx-template".
    template_name = 'ndx-template'

    user_config = cookiecutter.config.get_user_config()
    template_path = os.path.join(user_config['cookiecutters_dir'],
                                 template_name,
                                 'cookiecutter.json')

    # the below will only work if cookiecutter downloads and caches the
    # template from github or has previously downloaded and cached this
    # template. this will not work for the following command on a clean
    # system:
    # cookiecutter {ndx-template source dir}
    if not os.path.exists(template_path):
        return

    replay_dir = user_config['replay_dir']
    replay_context = cookiecutter.replay.load(replay_dir, template_name)
    new_default_context = replay_context['cookiecutter']

    with open(template_path, 'w') as outfile:
        json.dump(new_default_context, outfile)


def main():
    """
    Runs the pre gen project hook main entry point.
    """
    _write_new_defaults()
    _validate()


if __name__ == "__main__":
    main()
