# This script is intended to parse the proposals exported from Pretalx in CSV
# format and generate a markdown output that cna be pasted in the `poster_session.md`.
# This is really manual and not very elegant, but it works.

# %%
import pandas as pd

proposals = pd.read_csv("euroscipy-2024_confirmed.csv")

# %%
proposals.head()

# %%
import numpy as np

output_md = ""
for _, proposal in proposals.iterrows():
    session_type = proposal['Session type']
    if session_type != 'Poster':
        output_md += f"\n## {proposal['Proposal title']}\n\n"

        track = proposal['Track']
        name = proposal["Speaker names"]
        if not isinstance(name, str):
            name = "To Be Defined"
        output_md += f"*{name}*,  *{session_type}*, *{track}*\n\n"
        output_md += f"**Abstract:** {proposal['Abstract']}\n\n"
        output_md += f'<a href="https://pretalx.com/euroscipy-2024/talk/{proposal["ID"]}/"><button type="button" class="btn btn-primary">All details</button></a>\n\n'

with open('confirmed_talks.md', 'w') as file:
    file.write(output_md)

# %%
