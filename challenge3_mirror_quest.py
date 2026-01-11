def find_longest_mirror_length(s):
    def mirror_length(start, end, d):
        if (start, end) in d: #already found the length for (start, end) pair so returning it instead of finding again
            return d[(start, end)]
        
        if start > end:        
            return 0
        
        if start == end: # only one character left (middle character incase of odd length substring)
            return 1
        
        if s[start] == s[end]: # first and last character matches    
            length = mirror_length(start+1, end-1, d) + 2
        else:
            length = max( mirror_length(start+1, end, d), # thrwoing away the first character
                         mirror_length(start, end - 1, d)) # throwing away the last character
            
        d[(start, end)] = length
        return length


    return mirror_length(0, len(s)-1, {})

if __name__ == "__main__":
    st = "bbabcbcab"
    print(find_longest_mirror_length(st))

    st = "GEEKS"
    print(find_longest_mirror_length(st))

    st = "MAPAM"
    print(find_longest_mirror_length(st))

    st = "ABCD"
    print(find_longest_mirror_length(st))
    