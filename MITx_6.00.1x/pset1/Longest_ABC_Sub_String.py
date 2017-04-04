
s = 'fuezhzgvoo'
longest, current = s[0], s[0]
for i in range(1, len(s)):
    if s[i-1] <= s[i]:
        current += s[i]
        longest = current if len(current) > len(longest) else longest
    else :
        current = s[i]

print( 'Longest substring in alphabetical order is: {}'.format(longest) )
