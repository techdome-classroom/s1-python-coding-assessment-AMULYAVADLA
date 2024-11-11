def decode_message( s: str, p: str) -> bool:

    # Memoization dictionary to store results of subproblems
    memo = {}

    def match(i: int, j: int) -> bool:
        # Check if the result is already calculated
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Base cases
        if j == len(p):
            # True if both strings are fully matched
            return i == len(s)
        
        if i == len(s):
            # Only matches if the remaining pattern is all '*'
            return p[j:] == '*' * (len(p) - j)
        
        # Matching logic
        if p[j] == '*':
            # '*' can match zero or more characters in `s`
            memo[(i, j)] = match(i + 1, j) or match(i, j + 1)
        elif p[j] == '?' or p[j] == s[i]:
            # '?' can match a single character, or exact character match
            memo[(i, j)] = match(i + 1, j + 1)
        else:
            # No match if characters differ and no wildcard applies
            memo[(i, j)] = False

        return memo[(i, j)]
    
    return match(0, 0)

        return False
