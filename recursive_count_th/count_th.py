'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#check the first 2 letters of word if they equal "th". If not, then count_th(word but minus its first character).
def count_th(word):
    print(word)
    print(word[:2] + " == th?" + str(word[:2] == "th"))
    if(len(word) < 2):#There's no way word can contain th if it's less that 2 characters long, we've reached our base case
        return 0
    if(word[:2] == "th"):#found one! Return 1 + whatever we find in the next substring 
        return 1 + count_th(word[1:])
    else:#Didn't find one, lets just keep searching
        return count_th(word[1:])
