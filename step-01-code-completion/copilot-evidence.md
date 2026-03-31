
# Copilot Evidence — Step 01

Replace all placeholders.

## Prompt 1

Finish the function to have normalized names in #sym:normalize_username
Use the rules described in comments for this func.

now gen a slugify helper for lowecase ascii and hyphens #sym:build_slug

## Why you accepted/rejected the suggestion

it generated the correct code for the task

## Final check
def normalize_username(name: str) -> str:

    name = name.strip()
    name = name.lower()
    name = name.replace(' ', '_')
    name = re.sub(r'[^a-z0-9_]', '', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    return name

def build_slug(title: str) -> str:

    title = title.lower()
    title = re.sub(r'[^a-z0-9]+', '-', title)
    title = title.strip('-')
    return title
