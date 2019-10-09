import re
import sys

from email.utils import parseaddr

PREF_NAMESPACE_REGEX = r'^[\-a-z]+$'
REQ_NAMESPACE_REGEX = r'^[\-_a-zA-Z0-9]+$'
GITHUB_USERNAME_REGEX = r'^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$'

namespace = '{{ cookiecutter.namespace }}'
email = '{{ cookiecutter.email }}'
github_username = '{{ cookiecutter.github_username }}'

RESTART_MSG = ('\nYou can restart cookiecutter with: cookiecutter --replay'
               ' gh:nwb-extensions/ndx-template')


def _validate():
    if not re.match(PREF_NAMESPACE_REGEX, namespace):
        print('WARNING: It is recommended to use only lower-case ASCII letters'
              ' and hyphens in your namespace.' + RESTART_MSG)
    if '@' not in parseaddr(email)[1]:
        print(('WARNING: The email address you entered "{email}" does not '
               'appear to be a valid email address. Are you sure you entered'
               ' it correctly?' + RESTART_MSG).format(email=email))
    if not re.match(GITHUB_USERNAME_REGEX, github_username):
        print(('WARNING: The GitHub username you entered "{github_username}" '
               'does not appear to be a valid GitHub username. Are you sure '
               'you entered it correctly?' + RESTART_MSG)
              .format(github_username=github_username))
    if namespace[:4] != 'ndx-':
        print('ERROR: The name of your NDX extension must start with "ndx-".' +
              RESTART_MSG)
        sys.exit(1)
    if not re.match(REQ_NAMESPACE_REGEX, namespace):
        # these are the rules for naming GitHub repositories, and we want the
        # name of the GitHub repository to match the name of the extension
        print('ERROR: Namespace can only have lower-case and upper-case ASCII '
              'letters, hyphens (-), and underscores (_).' + RESTART_MSG)
        sys.exit(1)


def main():
    """
    Runs the pre gen project hook main entry point.
    """
    _validate()


if __name__ == "__main__":
    main()
