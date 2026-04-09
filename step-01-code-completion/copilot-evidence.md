# Copilot Evidence — Step 01

## Prompt 1

Finish the function to have normalized names in #sym:normalize_username
Use the rules described in comments for this func.

now gen a slugify helper for lowecase ascii and hyphens #sym:build_slug

## Why you accepted/rejected the suggestion

it generated a proper code for the task

## Final check

    name = name.lower()  # Convert to lowercase
    name = name.strip()  # Trim outer whitespace
    name = name.replace(' ', '_')  # Replace spaces with underscores
    name = re.sub(r'[^a-z0-9_]+', '', name)  # Remove any character that is not a-z, 0-9, or underscore
    name = re.sub(r'_+', '_', name)  # Collapse repeated underscores into one underscore
    name = name.strip('_')  # Strip leading/trailing underscores
    return name

    def build_slug(title: str) -> str:
    title = title.lower()  # Lowercase
    title = re.sub(r'[^a-z0-9]+', '-', title)  # Replace any sequence of non-alphanumeric characters with a single '-'
    title = title.strip('-')  # Strip leading/trailing '-'
    return title
