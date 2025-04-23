def is_substring(sub, full):
    for i in range(len(full) - len(sub) + 1):
        if full[i:i+len(sub)] == sub:
            return True
    return False
