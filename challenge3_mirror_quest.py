def find_longest_mirror_length(s, start, end):
    if start > end:        
        return 0
    
    if start == end:
        return 1
    
    if s[start] == s[end]:
        start = start + 1   # second character
        end = end - 1       # second last character
        return find_longest_mirror_length(s, start, end) + 2
    else:
        # throwing away the first character
        length1 = find_longest_mirror_length(s, start+1, end)

        # throwing away the last character
        length2 = find_longest_mirror_length(s, start, end - 1)

        if length1 > length2:
            return length1
        return length2


st = "bbabcbcab"
print(find_longest_mirror_length(st, 0, len(st) - 1))
    