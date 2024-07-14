''' You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed. '''

def removeStar(s):
    stack = []
    
    for char in s:
        if char == '*':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)    
        
print(removeStar(s='leet**cod*e'))