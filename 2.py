def match(kom):
    count_match = 0
    match = None
    while match != 1:
        ex_kom = 0
        if kom % 2 != 0:
            ex_kom = 1
        match = kom // 2
        kom = (kom // 2) + ex_kom
        count_match += match
    return count_match

x  = int(input(" n = "))
print(match(x))
