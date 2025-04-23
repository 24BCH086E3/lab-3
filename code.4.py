def remove_substring(original, remove):
    result = ''
    i = 0
    while i < len(original):
        if original[i:i+len(remove)] == remove:
            i += len(remove)
        else:
            result += original[i]
            i += 1
    return result
