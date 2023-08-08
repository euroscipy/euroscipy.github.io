# This script is intended to parse the proposals exported from Pretalx in CSV
# format and generate a markdown output that cna be pasted in the `poster_session.md`.
# This is really manual and not very elegant, but it works.

# %%
import pandas as pd

proposals = pd.read_csv("euroscipy-2023_sessions.csv")

# %%
proposals.head()

# %%
import numpy as np

output_md = ""
for _, proposal in proposals.iterrows():
    if proposal["Session type"] == "Poster":
        output_md += f"\n## {proposal['Proposal title']}\n\n"
        name = proposal["Speaker names"]
        if not isinstance(name, str):
            name = "To Be Defined"
        output_md += f"*{name}*\n\n"
        output_md += f"**Abstract:** {proposal['Abstract']}\n\n"
        output_md += f'<a href="https://pretalx.com/euroscipy-2023/talk/{proposal["ID"]}/"><button type="button" class="btn btn-primary">All details</button></a>\n\n'
print(output_md)

# %%
