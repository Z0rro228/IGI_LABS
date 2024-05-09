def removeStartWithA(text: str):
    """Remove all words in the text that starts with A."""
    words = text.split(' ')
    print(words)
    ans = ""
    for w in words:
        if not(w.startswith('a') or w.startswith('A')):
            ans = ans + " " + w
    return ans