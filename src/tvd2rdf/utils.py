def toLowerCamelCase(s):
    """Converts a string to lowerCamelCase."""
    # convert to a list
    l = s.strip().replace("_", " ").replace("-", " ").split(" ")
    # convert inital letter of first word to lc but leave anything that is already in CamelCase
    word1 = l[0]
    if word1 == word1.upper():
        r = word1.lower()  # don't camel case words that are all UC, e.g. URL
    else:
        r = word1[0].lower() + word1[1:]
    # convert inital letters of the rest to UC but leave anything that is alread in CamelCase
    for word in l[1:]:
        t = word[0].capitalize() + word[1:].lower()
        r = r + t
    return r
