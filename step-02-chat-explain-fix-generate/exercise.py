def parse_scoreboard(raw: str) -> dict[str, int]:
    """Parse 'name:score' pairs separated by commas.

    Example: "alice:10,bob:9,alice:14" -> {"alice": 14, "bob": 9}

    Invalid segments should be skipped.
    """
    board: dict[str, int] = {}
    if raw == "":
        return board

    parts = raw.split(",")
    for part in parts:
        if ":" not in part:
            continue
        try:
            name, score_str = part.split(":", 1)
            name = name.lower().strip()
            score = int(score_str.strip())
            board[name] = score
        except ValueError:
            continue
    return board


def _max_score_player(board: dict[str, int]) -> tuple[str, int] | None:
    """Return the player with the highest score, else None.

    Deterministic ties are resolved by choosing the alphabetically first name.
    """
    if not board:
        return None

    max_score = max(board.values())
    top_name = min(name for name, score in board.items() if score == max_score)
    return (top_name, max_score)


def top_player(board: dict[str, int]) -> tuple[str, int] | None:
    """Return the player with the highest score, else None."""
    return _max_score_player(board)
