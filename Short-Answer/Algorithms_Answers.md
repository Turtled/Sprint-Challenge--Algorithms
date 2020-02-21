#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

Justification: 
    a = 0
    while (a < n * n * n):
        a = a + n * n

If `a` were only increasing by 1 each time through the loop, O() would be a lot worse (O(n^3)). However, `a` is increasing by n^2. n^3 / n^2 = n, therefore this function is O(n)

b) O(n * log(n))

Justification:
    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

The first loop just loops from 0 to n, which is O(n). The loop inside (and since it's inside, it's going to be n * whatever is inside. This is because whatever is inside has to run n times) is going to be log(n), since it multiplies j by 2 each time through. I'm not sure if that's correct but it reminds me of a binary search, and a binary search's complexity is log(n).

c) O(n)

Justification:
    def bunnyEars(bunnies):
        if bunnies == 0:
            return 0

        return 2 + bunnyEars(bunnies-1)

This function will continue calling itself until it reaches 0, by subtracting 1 each time. That sounds a lot like a simple for loop looping from 0 to n to me, and that's O(n). 

## Exercise II
"Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized."

I would use a binary search, which would have a time complexity of O(log(floors)). First, I would go to the middle of the building and drop an egg. If the egg broke, I would know that the same thing will happen for all the floors that are above me, so I can completely disregard them all. Similarly, if the egg didn't break, I would know that the same thing will happen on all the floors that are below me, so I can completely disregard them all. I would continue this process, going to the middle of all the floors that I have currently not disregarded until I narrowed it down to the exact floor that the egg will break at but not on the floor below.

