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
GITHUB_USERNAME_REGEX = r'^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$'

namespace = '{{ cookiecutter.namespace }}'
email = map(str.strip, '{{ cookiecutter.email }}'.split(','))
github_username = '{{ cookiecutter.github_username }}'


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
    if not re.match(GITHUB_USERNAME_REGEX, github_username):
        warnings.append(
            'The GitHub username you entered "{github_username}" does not '
            'appear to be a valid GitHub username. Are you sure you entered it'
            ' correctly?'.format(github_username=github_username)
        )

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
    by the user.
    """
    user_config = cookiecutter.config.get_user_config()
    replay_dir = user_config['replay_dir']
    if not os.path.exists(replay_dir):
        os.makedirs(replay_dir)
    replay_context = cookiecutter.replay.load(replay_dir, 'ndx-template')
    new_default_context = replay_context['cookiecutter']
    # user_config['cookiecutters_dir'] probably only works with repo arg
    template_path = os.path.join(user_config['cookiecutters_dir'],
                                 'ndx-template',
                                 'cookiecutter.json')
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
