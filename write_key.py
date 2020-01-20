import os

with open('id_ssh', 'w') as f:
    print(os.environ['SSH_KEY'], file=f)

with open('.ssh/known_hosts', 'w') as f:
    print(os.environ['SSH_KNOWN_HOST'], file=f)

