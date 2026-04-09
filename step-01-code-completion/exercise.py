import re


def normalize_username(name: str) -> str:
    """Normalize a username.

    Rules:
    - Trim outer whitespace.
    - Convert to lowercase.
    - Replace spaces with underscores.
    - Remove any character that is not a-z, 0-9, or underscore.
    - Collapse repeated underscores into one underscore.
    - Strip leading/trailing underscores.
    """
        # Complete the rules above using code completion.
    name = name.lower()  # Convert to lowercase
    name = name.strip()  # Trim outer whitespace
    name = name.replace(' ', '_')  # Replace spaces with underscores
    name = re.sub(r'[^a-z0-9_]+', '', name)  # Remove any character that is not a-z, 0-9, or underscore 
    name = re.sub(r'_+', '_', name)  # Collapse repeated underscores into one underscore
    name = name.strip('_')  # Strip leading/trailing underscores
    return name


def build_slug(title: str) -> str:
    """Convert a title into a URL-friendly slug.

    Rules:
    - Lowercase.
    - Keep letters and digits.
    - Replace any sequence of non-alphanumeric characters with a single '-'.
    - Strip leading/trailing '-'.
    """
    # implement it now
    title = title.lower()  # Lowercase
    title = re.sub(r'[^a-z0-9]+', '-', title)  # Replace any sequence of non-alphanumeric characters with a single '-'
    title = title.strip('-')  # Strip leading/trailing '-'
    return title    