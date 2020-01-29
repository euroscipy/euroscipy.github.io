import os
import os.path

print(list(os.environ.keys()))

with open(os.path.expanduser('~/.ssh/id_rsa'), 'w') as f:
    print(os.environ['SSH_KEY'], file=f)

with open(os.path.expanduser('~/.ssh/known_hosts'), 'w') as f:
    print(os.environ['SSH_KNOWN_HOST'], file=f)

