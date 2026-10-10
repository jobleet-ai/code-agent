def find_duplicate_titles(tasks):
    """Return pairs of task ids whose titles match (case-insensitive)."""
    duplicates = []
    for i in range(len(tasks)):
        for j in range(i + 1, len(tasks)):
            if tasks[i]["title"].lower() == tasks[j]["title"].lower():
                duplicates.append((tasks[i]["id"], tasks[j]["id"]))
    return duplicates
