import os

with open('id_ssh', 'w') as f:
    print(os.environ['SSH_KEY'], file=f)

