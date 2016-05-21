

def copy(lst):
    other = []
    for x in lst:
        other.append(x)
    return other

def dropWhile(predicate, lst):
    for i in range(len(lst)):
        if not predicate(lst[i]):
            return lst[i+1:]
    return []

def takeWhile(predicate, lst):
    for i in range(len(lst)):
        if not predicate(lst[i]):
            return lst[:i]
    return lst
