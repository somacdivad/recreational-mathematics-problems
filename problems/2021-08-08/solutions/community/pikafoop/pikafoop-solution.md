[YouTube](https://youtu.be/kQaTzqngI4M) || [GitHub](https://github.com/somacdivad/recreational-mathematics-problems/tree/main/problems/2021-08-08) || [Twitter](https://twitter.com/somacdivad/status/1425517816191586316)

pikafoop's solution to...

# Largest And Smallest Numbers

This week's puzzle continues the divisibility theme from last week.

There are two parts:

a) For each value of *n*, from 2 to 16, find the largest and smallest nine-digit numbers, containing each of the nine nonzero digits exactly once, that are exactly divisible by *n*.

b) Do the same for ten-digit numbers containing each of the ten digits (including 0) exactly once. (Note that 0 may not be the first digit of a number.)

_This problem is Problem 4.33 in Problem Solving Through Recreational Mathematics by Bonnie Averbach and Orin Chein._

Feel free to use your favorite programming language to solve the problem.

You can submit solutions via pull request or by emailing your code to recmath@davidamos.dev. If you submit a pull request, make sure your solution is added to the `solutions/community/` folder.

> **Note:** By submitting a solution you agree to make the code for your solution available under the MIT license.

I'll feature my solution and a couple of my favorite submitted solutions in a YouTube video!

<hr/>

## STEP 1: Brute Force

With a modern computer, we can brute-force the problem in a matter of seconds. We'll do that first so we have an answer table to check ourselves against, then be clever later.


```python
from itertools import permutations

digit_cs_1to9 = '123456789'
digit_cs_0to9 = '0123456789'

%time pandigs_1to9 = [int(''.join(cs)) for cs in permutations(digit_cs_1to9)]
%time pandigs_0to9 = [int(''.join(cs)) for cs in permutations(digit_cs_0to9) if cs[0] != '0']

print(f"{len(pandigs_1to9):,} pandigital 1-9 numbers")
print(f"{len(pandigs_0to9):,} pandigital 0-9 numbers")
```

    Wall time: 139 ms
    Wall time: 1.43 s
    362,880 pandigital 1-9 numbers
    3,265,920 pandigital 0-9 numbers
    


```python
from collections import namedtuple

sol = namedtuple('solution', ['smallest_1to9', 'largest_1to9', 'smallest_0to9', 'largest_0to9'])

solutions = {}
for n in range(2, 16+1):
    pd19 = [a for a in pandigs_1to9 if a % n == 0]
    pd09 = [a for a in pandigs_0to9 if a % n == 0]
    n19 = min(pd19) if pd19 else 0
    x19 = max(pd19) if pd19 else 0
    n09 = min(pd09) if pd09 else 0
    x09 = max(pd09) if pd09 else 0
    solutions[n] = sol(n19, x19, n09, x09)
    
    
def print_solution(d):
    print(f"""{d}-divisible:
    Largest  1-9:\t{solutions[d].largest_1to9:,}
    Largest  0-9:\t{solutions[d].largest_0to9:,}
    Smallest 1-9:\t{solutions[d].smallest_1to9:,}
    Smallest 1-9:\t{solutions[d].smallest_0to9:,}""")

    
for d in solutions:
    print_solution(d)
```

    2-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,456,798
        Smallest 1-9:	1,023,456,798
    3-divisible:
        Largest  1-9:	987,654,321
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,456,789
        Smallest 1-9:	1,023,456,789
    4-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,120
        Smallest 1-9:	123,457,896
        Smallest 1-9:	1,023,457,896
    5-divisible:
        Largest  1-9:	987,643,215
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,467,895
        Smallest 1-9:	1,023,467,895
    6-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,456,798
        Smallest 1-9:	1,023,456,798
    7-divisible:
        Largest  1-9:	987,654,213
        Largest  0-9:	9,876,543,201
        Smallest 1-9:	123,456,879
        Smallest 1-9:	1,023,456,798
    8-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,120
        Smallest 1-9:	123,457,896
        Smallest 1-9:	1,023,457,896
    9-divisible:
        Largest  1-9:	987,654,321
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,456,789
        Smallest 1-9:	1,023,456,789
    10-divisible:
        Largest  1-9:	0
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	0
        Smallest 1-9:	1,234,567,890
    11-divisible:
        Largest  1-9:	987,652,413
        Largest  0-9:	9,876,524,130
        Smallest 1-9:	123,475,869
        Smallest 1-9:	1,024,375,869
    12-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,120
        Smallest 1-9:	123,457,896
        Smallest 1-9:	1,023,457,896
    13-divisible:
        Largest  1-9:	987,654,213
        Largest  0-9:	9,876,542,130
        Smallest 1-9:	123,456,879
        Smallest 1-9:	1,023,456,798
    14-divisible:
        Largest  1-9:	987,653,142
        Largest  0-9:	9,876,543,012
        Smallest 1-9:	123,457,698
        Smallest 1-9:	1,023,456,798
    15-divisible:
        Largest  1-9:	987,643,215
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,467,895
        Smallest 1-9:	1,023,467,895
    16-divisible:
        Largest  1-9:	987,645,312
        Largest  0-9:	9,876,543,120
        Smallest 1-9:	123,457,968
        Smallest 1-9:	1,023,457,968
    

Done! Now let's use divisibility rules. We'll use our results above to verify our work.

<hr/>

## STEP 2: Divisibility Rules

We can get a chart of divisibility rules from [Wikipedia](https://en.wikipedia.org/wiki/Divisibility_rule).

### 1: First, making largest and smallest numbers out of collections of digits

To make the largest number possible, order the digits from largest to smallest, only making exceptions to fit the number to the divisibility rules. No restrictions (divisible by 1):

- 987,654,321
- 9,876,543,210

To make the smallest number possible, order the digits from smallest to largest, only making exceptions to fit the number to the divisiblity rules, and to keep the first digit from being 0. No restrictions (divisible by 1):

- 123,456,789
- 1,023,456,789

### 2: The last digit (in the ones place) must be even (divisible by 2)

We only need to, at most, swap the last two digits in order to get an even digit in the ones place.

Largest:

- 987,654,3**12**
- 9,876,543,210

Smallest:

- 123,456,7**98**
- 1,023,456,7**98**



```python
print_solution(2)
```

    2-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,456,798
        Smallest 1-9:	1,023,456,798
    

### 3: The sum of all digits must be divisible by 3

`1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45` and `45 mod 3 = 0`, and `45 + 0 = 45`. Therefore, all our pandigital candidates are divisible by 3, and we can just use the largest and smallest numbers by digit ordering.

Largest:

- 987,654,321
- 9,876,543,210

Smallest:

- 123,456,789
- 1,023,456,789


```python
print_solution(3)
```

    3-divisible:
        Largest  1-9:	987,654,321
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,456,789
        Smallest 1-9:	1,023,456,789
    

### 4: The last two digits must form a number divisible by 4


We'll create a function to help with the "sub-number divisibility"-type rules. For some number of digits _d_ and divisor _n_, we want to find some number _a_ divisible by _n_, such that:

- For the "largest" values, we want the collection of smallest digits possible, making the largest number possible
- For the "smallest" values, we want the collection of largest digits possible, making the smallest number possible

We'll find these by making comparable tuples containing:

- Each sorting of digits, so we can determine collections of largest and smallest digits
- The values of any number those digits can make in any order, negated to make our "backwards" comparisons work

Then we'll return the un-negated numbers to use in construction our largest and smallest numbers.


```python
from itertools import combinations


def subdivs(d, n):
    sets_1to9 = set()
    for digit_set in combinations(digit_cs_1to9, d):
        digit_strs = [''.join(sorted(digit_set)), ''.join(sorted(digit_set, reverse=True))]
        for value_str in permutations(digit_set):
            i = int(''.join(value_str))
            sets_1to9.add( (digit_strs[0], -i) )
            sets_1to9.add( (digit_strs[1], -i) )
    
    sets_0to9 = set()
    for digit_set in combinations(digit_cs_0to9, d):
        digit_strs = [''.join(sorted(digit_set)), ''.join(sorted(digit_set, reverse=True))]
        for value_str in permutations(digit_set):
            i = int(''.join(value_str))
            sets_0to9.add( (digit_strs[0], -i) )
            sets_0to9.add( (digit_strs[1], -i) )
    
    smallest_1to9 = -min(p for p in sets_1to9 if p[1] % n == 0)[1]
    smallest_0to9 = -min(p for p in sets_0to9 if p[1] % n == 0)[1]
    largest_1to9 = -max(p for p in sets_1to9 if p[1] % n == 0)[1]
    largest_0to9 = -max(p for p in sets_0to9 if p[1] % n == 0)[1]
    
    return [str(a).zfill(d) for a in [smallest_1to9, smallest_0to9, largest_1to9, largest_0to9]]

            
subdivs(2, 4)
```




    ['12', '20', '96', '96']



12 and 20 are easily available for decreasing-digit order, but we have to reach for 96 in increasing order.

Largest:

- 987,654,3**12**
- 9,876,543,**12**0

Smallest:

- 123,45**7,896**
- 1,023,45**7,896**


```python
print_solution(4)
```

    4-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,120
        Smallest 1-9:	123,457,896
        Smallest 1-9:	1,023,457,896
    

### 5: The last digit must be 5 or 0

This merely requires that we shift one digit to the ones place.

Largest:

- 987,6**43,215**
- 9,876,543,210

Smallest:

- 123,4**67,895**
- 1,023,4**67,895**


```python
print_solution(5)
```

    5-divisible:
        Largest  1-9:	987,643,215
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,467,895
        Smallest 1-9:	1,023,467,895
    

### 6: Must be divisible by 2 and 3

Since all candidates are divisible by 3, these are the same answers as for 2.

Largest:

- 987,654,3**12**
- 9,876,543,210

Smallest:

- 123,456,7**98**
- 1,023,456,7**98**


```python
print_solution(6)
```

    6-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,456,798
        Smallest 1-9:	1,023,456,798
    

### 7: Alternating sums of 3-digit blocks (from right to left) must yield a multiple of 7

Divisibility by 7 is more complicated than any of the previous numbers, and there are several tricks to choose from. This one might be fun to write a search function for.

Let's try some examples, keeping in mind that `(a + b) mod n = a mod n + b mod n` to keep the arithmetic simpler:

- `9,876,543,210 mod 7 = (210 - 543 + 876 - 9) mod 7 = (0 - 4 + 1 - 9) mod 7 = -12 mod 7 = 2`, so _not divisble_ by 7
- `9,876,543,201 mod 7 = (201 - 543 + 876 - 9) mod 7 = (5 - 4 + 1 - 9) mod 7 = -7 mod 7 = 0`, so _divisible_ by 7.

We'll recursively test 3-digit blocks in order of favorability until we are able to build the best possible number divisible by 7. We'll have to build our number from left to right, since the most influential blocks are furthest left.

_NB: This code could be generalized to work for multiple divisibility rules, but we're not doing that yet._


```python
from functools import lru_cache
from itertools import islice

digit_set_1to9 = frozenset(c for c in '123456789')
digit_set_0to9 = frozenset(c for c in '0123456789')


@lru_cache() # since we will call this multiple times with the same arguments, reuse results
def digit_subsets(digit_set, subset_size):
    subset = set()
    for digits in permutations(digit_set, subset_size):
        value_str = ''.join(digits)
        subset.add(value_str)
    return frozenset(subset)


def largest_7(digit_set):
    return list(islice(_search_7(True, digit_set), 1))[0] # just return the first valid value


def smallest_7(digit_set):
    return list(islice(_search_7(False, digit_set), 1))[0]


def _search_7(largest, digit_set, incoming_remainder=0, incoming_number = ""):
    
    # how big is this block?
    if len(digit_set) % 3 == 0:
        block_size = 3
    else:
        block_size = len(digit_set) % 3
          
    # is this a negative term? even-numbered terms, counted right to left, are.
    block_number = (len(digit_set) - block_size) / 3 + 1
    negative_term = block_number % 2 == 0
    
    for value_str in sorted(digit_subsets(digit_set, block_size), reverse=largest):
        if incoming_number == "" and value_str[0] == '0': # leading 0s are not allowed
            continue
        
        if incoming_number == "":
            new_number = value_str
        else:
            new_number = incoming_number + ',' + value_str
        value = int(value_str)
        remainder = value % 7
        
        if negative_term:
            new_remainder = (incoming_remainder - remainder) % 7
        else:
            new_remainder = (incoming_remainder + remainder) % 7
        
        rem_digits = digit_set - set(c for c in value_str)
        
        if len(rem_digits) == 0: # this is the final term
            if new_remainder == 0: # qualifying number
                yield new_number
        else: # move on to next block
            for result in _search_7(largest, rem_digits, new_remainder, new_number):
                yield result
                
        
largest_7(digit_set_1to9), largest_7(digit_set_0to9), smallest_7(digit_set_1to9), smallest_7(digit_set_0to9)
```




    ('987,654,213', '9,876,543,201', '123,456,879', '1,023,456,798')



Largest:
- 987,654,**213**
- 9,876,543,2**01**

Smallest:
- 123,456,**879**
- 1,023,456,7**98**


```python
print_solution(7)
```

    7-divisible:
        Largest  1-9:	987,654,213
        Largest  0-9:	9,876,543,201
        Smallest 1-9:	123,456,879
        Smallest 1-9:	1,023,456,798
    

### 8: The last 3 digits must form a number divisible by 8

This works because `1,000 mod 8 = 0`, so we only care about the places under the 1,000's place. 


```python
subdivs(3, 8)
```




    ['312', '120', '896', '896']



The smallest 8-divisible 3-digit numbers available are 312 and 120; the largest available is 896.

Largest:
- 987,654,3**12**
- 9,876,543,**120**

Smallest:
- 123,45**7,896**
- 1,023,45**7,896**


```python
print_solution(8)
```

    8-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,120
        Smallest 1-9:	123,457,896
        Smallest 1-9:	1,023,457,896
    

### 9: The sum of the digits must be divisible by 9

`1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45` and `45 mod 9 = 0`, and `45 + 0 = 45`. Therefore, all our pandigital candidates are divisible by 9, and we can just use the largest and smallest numbers by digit ordering, as we did for 3.

Largest:

- 987,654,321
- 9,876,543,210

Smallest:

- 123,456,789
- 1,023,456,789


```python
print_solution(9)
```

    9-divisible:
        Largest  1-9:	987,654,321
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,456,789
        Smallest 1-9:	1,023,456,789
    

### 10: The last digit must be 0

There are no 1-9 pandigital numbers that end in 0, since they don't contain 0.

Largest:
- _none exists_
- 9,876,543,210

Smallest:
- _none exists_
- 1,**234,567,890**


```python
print_solution(10) # our program indicates "no answer exists" as "0"
```

    10-divisible:
        Largest  1-9:	0
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	0
        Smallest 1-9:	1,234,567,890
    

### 11: Sums of 2-digit blocks must yield a multiple of 11

Just as with 7, there are multiple rules for 11. This one looks like another fun recursive search opportunity.

- `9,876,543,210 mod 11 = (98 + 76 + 54 + 32 + 10) mod 11 = (10 + 10 + 10 + 10 + 10) mod 11 = 50 mod 7 = 6`, so _not divisble_ by 11
- `9,876,524,130 mod 11 = (98 + 76 + 52 + 41 + 30) mod 11 = (10 + 10 + 8 + 8 + 8) mod 11 = 44 mod 11 = 0`, so _divisible_ by 11.

We'll modify our code from 7 to add up blocks of 2 numbers and test for 11-divisibility.

_NB: This is one rule we could use a generalized form of the solution from 7 to solve, instead of copy-pasted and modified code._


```python
def largest_11(digit_set):
    for result in _search_11(True, digit_set):
        return f"{int(result):,}"


def smallest_11(digit_set):
    for result in _search_11(False, digit_set):
        return f"{int(result):,}"


def _search_11(largest, digit_set, incoming_remainder=0, incoming_number = ""):
    
    # how big is this block?
    if len(digit_set) % 2 == 0:
        block_size = 2
    else:
        block_size = len(digit_set) % 2
    
    for value_str in sorted(digit_subsets(digit_set, block_size), reverse=largest):
        if incoming_number == "" and value_str[0] == '0': # leading 0s are not allowed
            continue
        
        if incoming_number == "":
            new_number = value_str
        else:
            new_number = incoming_number + value_str
        value = int(value_str)
        remainder = value % 11
        
        new_remainder = (incoming_remainder + remainder) % 11
        
        rem_digits = digit_set - set(c for c in value_str)
        
        if len(rem_digits) == 0: # this is the final term
            if new_remainder == 0: # qualifying number
                yield new_number
        else: # move on to next block
            for result in _search_11(largest, rem_digits, new_remainder, new_number):
                yield result
                
        
largest_11(digit_set_1to9), largest_11(digit_set_0to9), smallest_11(digit_set_1to9), smallest_11(digit_set_0to9)
```




    ('987,652,413', '9,876,524,130', '123,475,869', '1,024,375,869')



Largest:
- 987,65**2,413**
- 9,876,5**24,13**0

Smallest:
- 123,4**75,86**9
- 1,02**4,375,86**9


```python
print_solution(11)
```

    11-divisible:
        Largest  1-9:	987,652,413
        Largest  0-9:	9,876,524,130
        Smallest 1-9:	123,475,869
        Smallest 1-9:	1,024,375,869
    

### 12: Must be divisible by 3 and 4

Since all candidates are divisible by 3, we use the same answers as for 4.

Largest:

- 987,654,3**12**
- 9,876,543,**12**0

Smallest:

- 123,45**7,896**
- 1,023,45**7,896**


```python
print_solution(12)
```

    12-divisible:
        Largest  1-9:	987,654,312
        Largest  0-9:	9,876,543,120
        Smallest 1-9:	123,457,896
        Smallest 1-9:	1,023,457,896
    

### 13: Alternating sums of 3-digit blocks (from right to left) must yield a multiple of 13

Just as with 7 and 11, there are multiple rules to choose from. This rule is almost identical to the rule we chose for 7.

- `9,876,543,210 mod 13 = (210 - 543 + 876 - 9) mod 13 = (2 - 10 + 5 - 9) mod 13 = -12 mod 13 = 2`, so _not divisble_ by 13
- `9,876,542,130 mod 13 = (130 - 542 + 876 - 9) mod 13 = (0 - 9 + 5 - 9) mod 13 = -13 mod 13 = 0`, so _divisible_ by `13`.


We'll adapt our 7 code accordingly.

_NB: This is another rule we could use a generalized form of the solution from 7 to solve, instead of copy-pasted and modified code._


```python
def largest_13(digit_set):
    return list(islice(_search_13(True, digit_set), 1))[0] # just return the first valid value


def smallest_13(digit_set):
    return list(islice(_search_13(False, digit_set), 1))[0]


def _search_13(largest, digit_set, incoming_remainder=0, incoming_number = ""):
    
    # how big is this block?
    if len(digit_set) % 3 == 0:
        block_size = 3
    else:
        block_size = len(digit_set) % 3
          
    # is this a negative term? even-numbered terms, counted right to left, are.
    block_number = (len(digit_set) - block_size) / 3 + 1
    negative_term = block_number % 2 == 0
    
    for value_str in sorted(digit_subsets(digit_set, block_size), reverse=largest):
        if incoming_number == "" and value_str[0] == '0': # leading 0s are not allowed
            continue
        
        if incoming_number == "":
            new_number = value_str
        else:
            new_number = incoming_number + ',' + value_str
        value = int(value_str)
        remainder = value % 13
        
        if negative_term:
            new_remainder = (incoming_remainder - remainder) % 13
        else:
            new_remainder = (incoming_remainder + remainder) % 13
        
        rem_digits = digit_set - set(c for c in value_str)
        
        if len(rem_digits) == 0: # this is the final term
            if new_remainder == 0: # qualifying number
                yield new_number
        else: # move on to next block
            for result in _search_13(largest, rem_digits, new_remainder, new_number):
                yield result
                
        
largest_13(digit_set_1to9), largest_13(digit_set_0to9), smallest_13(digit_set_1to9), smallest_13(digit_set_0to9)
```




    ('987,654,213', '9,876,542,130', '123,456,879', '1,023,456,798')



Largest:
- 987,654,**213**
- 9,876,54**2,13**0

Smallest:
- 123,456,**87**9
- 1,023,456,7**98**


```python
print_solution(13)
```

    13-divisible:
        Largest  1-9:	987,654,213
        Largest  0-9:	9,876,542,130
        Smallest 1-9:	123,456,879
        Smallest 1-9:	1,023,456,798
    

### 14: Must be divisible by 2 and 7

We will use our code for finding numbers divisible by 7 and filter for even results.


```python
def largest_14(digit_set):
    for v in _search_7(True, digit_set):
        if int(v.replace(',', '')) % 2 == 0:
            return v

def smallest_14(digit_set):
    for v in _search_7(False, digit_set):
        if int(v.replace(',', '')) % 2 == 0:
            return v

largest_14(digit_set_1to9), largest_14(digit_set_0to9), smallest_14(digit_set_1to9), smallest_14(digit_set_0to9)
```




    ('987,653,142', '9,876,543,012', '123,457,698', '1,023,456,798')



Largest:
- 987,65**3,142**
- 9,876,543,**012**

Smallest:
- 123,45**7,698**
- 1,023,456,7**98**


```python
print_solution(14)
```

    14-divisible:
        Largest  1-9:	987,653,142
        Largest  0-9:	9,876,543,012
        Smallest 1-9:	123,457,698
        Smallest 1-9:	1,023,456,798
    

### 15: Must be divisible by 3 and 5

Since all candidates are divisible by 3, the last digit must be 5 or 0.

Largest:

- 987,6**43,215**
- 9,876,543,210

Smallest:

- 123,4**67,895**
- 1,023,4**67,895**


```python
print_solution(15)
```

    15-divisible:
        Largest  1-9:	987,643,215
        Largest  0-9:	9,876,543,210
        Smallest 1-9:	123,467,895
        Smallest 1-9:	1,023,467,895
    

### 16: The last 4 digits must be divisible by 16



```python
subdivs(4, 16)
```




    ['5312', '3120', '7968', '7968']



The smallest 4-digit numbers divisible by 16 are 5,312 and 3,120. The largest is 7,968.

Largest:
- 987,6**45,312**
- 9,876,543,**12**0

Smallest:
- 123,45**7,968**
- 1,023,45**7,968**


```python
print_solution(16)
```

    16-divisible:
        Largest  1-9:	987,645,312
        Largest  0-9:	9,876,543,120
        Smallest 1-9:	123,457,968
        Smallest 1-9:	1,023,457,968
    

<hr/>

## STEP 3: Analysis

Since we showed in STEP 1 that our computer is perfectly capable of doing divisibilty calculations on large numbers, using a very small amount of code, we might wonder if there's a benefit to the more complicated methods.

As an example, let's look at finding the solutions for divisibility by 13, and determine how many candidates we have to evaluate using an addition-by-blocks method and a "let the computer do the work" method. We'll modify code from above.

### A. Brute Force

Above, we used very naive code to create all the pandigital numbers and sieve them through divisibility tests. As a result, it took over 1.6 seconds to generate all of the numbers, and several seconds to sieve all of them.

We're going to be _slightly_ smarter here. We will take advantage of the ordering of results delivered by `permutations`. If we deliver our digits in increasing order, the results will count up from that smallest number. If we deliver them in decreasing order, then they will count down from the largest number. In this way, the first 13-divisible number is the largest (or smallest) number in the set. (We're also going not going to count any numbers that start with a 0 as candidates.)


```python
from itertools import permutations

def bf_first_divisible_by(n, digit_chars):
    for i, digit_order in enumerate(o for o in permutations(digit_chars) if o[0] != '0'):
        a = int(''.join(digit_order))
        if a % n == 0:
            print(f"{a:,} is divisible by {n:,}. (Candidate # {i+1:,})")
            return a
        
        
%time bf_first_divisible_by(13, '987654321')
%time bf_first_divisible_by(13, '9876543210')
%time bf_first_divisible_by(13, '123456789')
%time bf_first_divisible_by(13, '0123456789')
print('-'*25)
print_solution(13)
```

    987,654,213 is divisible by 13. (Candidate # 4)
    Wall time: 0 ns
    9,876,542,130 is divisible by 13. (Candidate # 9)
    Wall time: 0 ns
    123,456,879 is divisible by 13. (Candidate # 3)
    Wall time: 0 ns
    1,023,456,798 is divisible by 13. (Candidate # 2)
    Wall time: 42.9 ms
    -------------------------
    13-divisible:
        Largest  1-9:	987,654,213
        Largest  0-9:	9,876,542,130
        Smallest 1-9:	123,456,879
        Smallest 1-9:	1,023,456,798
    

That went incredibly quickly. The largest number of candidates checked was 9, and the only part of the process that took over 1 ms was skipping all the candidates with a '0' in the leftmost place. We could eliminate that delay by sending in our digits in a more intelligent ordering so the permutations start with the smallest actually viable number.


```python
%time bf_first_divisible_by(13, '1023456789')
```

    1,023,456,798 is divisible by 13. (Candidate # 2)
    Wall time: 0 ns
    




    1023456798



It seems unlikely that we'll be technically faster using the block addition method.

### B. Block Method

We're going to modify our code from above to (1) be reusable for different divisors, block sizes, and alternating vs non-alternating block addition, and (2) keep track of the number of candidates evaluated.


```python
from functools import lru_cache
from itertools import islice

digit_set_1to9 = frozenset(c for c in '123456789')
digit_set_0to9 = frozenset(c for c in '0123456789')


@lru_cache() # since we will call this multiple times with the same arguments, reuse results
def digit_subsets(digit_set, subset_size):
    subset = set()
    for digits in permutations(digit_set, subset_size):
        value_str = ''.join(digits)
        subset.add(value_str)
    return frozenset(subset)

def largest_13(digit_set):
    return list(islice(_search_13(True, digit_set), 1))[0] # just return the first valid value


def smallest_13(digit_set):
    return list(islice(_search_13(False, digit_set), 1))[0]


def _search_13(largest, digit_set, incoming_remainder=0, incoming_number = ""):
    
    # how big is this block?
    if len(digit_set) % 3 == 0:
        block_size = 3
    else:
        block_size = len(digit_set) % 3
          
    # is this a negative term? even-numbered terms, counted right to left, are.
    block_number = (len(digit_set) - block_size) / 3 + 1
    negative_term = block_number % 2 == 0
    
    for value_str in sorted(digit_subsets(digit_set, block_size), reverse=largest):
        if incoming_number == "" and value_str[0] == '0': # leading 0s are not allowed
            continue
        
        if incoming_number == "":
            new_number = value_str
        else:
            new_number = incoming_number + ',' + value_str
        value = int(value_str)
        remainder = value % 13
        
        if negative_term:
            new_remainder = (incoming_remainder - remainder) % 13
        else:
            new_remainder = (incoming_remainder + remainder) % 13
        
        rem_digits = digit_set - set(c for c in value_str)
        
        if len(rem_digits) == 0: # this is the final term
            if new_remainder == 0: # qualifying number
                yield new_number
        else: # move on to next block
            for result in _search_13(largest, rem_digits, new_remainder, new_number):
                yield result
                
        
largest_13(digit_set_1to9), largest_13(digit_set_0to9), smallest_13(digit_set_1to9), smallest_13(digit_set_0to9)
```




    ('987,654,213', '9,876,542,130', '123,456,879', '1,023,456,798')




```python
from functools import lru_cache
from itertools import islice


@lru_cache() # since we will call this multiple times with the same arguments, reuse results
def digit_subsets(digit_set, subset_size):
    subset = set()
    for digits in permutations(digit_set, subset_size):
        value_str = ''.join(digits)
        subset.add(value_str)
    return frozenset(subset)


def ba_first_divisible_by(n, digit_chars, largest, rule_block_size, alternating_addition):
    global candidate_count
    candidate_count = 0
    
    digit_set = frozenset(c for c in digit_chars)
    
    return candidate_count, list(
        islice(
            ba_search_divisible_by(n, digit_set, largest, rule_block_size, alternating_addition), 1))[0]


def ba_search_divisible_by(n, digit_set, largest,
                           rule_block_size, alternating_addition,
                           incoming_remainder = 0, incoming_number = ""):
    global candidate_count
    
    # how big is this block?
    if len(digit_set) % rule_block_size == 0:
        block_size = rule_block_size
    else:
        block_size = len(digit_set) % rule_block_size
        
    # determine if this is a negative term, if alternating addition is specified
    if alternating_addition:
        block_number = (len(digit_set) - block_size) / rule_block_size + 1
        negative_term = block_number % 2 == 0
    else:
        negative_term = False
        
    for value_str in sorted(digit_subsets(digit_set, block_size), reverse=largest):
        if incoming_number == "" and value_str[0] == '0': # leading 0s are not allowed
            continue
        
        new_number = incoming_number + value_str
        value = int(value_str)
        remainder = value % n
        
        if negative_term:
            new_remainder = (incoming_remainder - remainder) % n
        else:
            new_remainder = (incoming_remainder + remainder) % n
        
        rem_digits = digit_set - set(c for c in value_str)
        
        if len(rem_digits) == 0: # this is the final term
            candidate_count += 1
            if new_remainder == 0: #qualifying number
                number_string = f"{int(new_number):,}"
                print(f"{number_string} is divisible by {n:,}. (Candidate # {candidate_count:,})")
                yield new_number
        else: # move on to next block
            for result in ba_search_divisible_by(n, rem_digits, largest,
                                                rule_block_size, alternating_addition,
                                                new_remainder, new_number):
                yield result


%time ba_first_divisible_by(13, '987654321', True, 3, True)
%time ba_first_divisible_by(13, '9876543210', True, 3, True)
%time ba_first_divisible_by(13, '123456789', False, 3, True)
%time ba_first_divisible_by(13, '1023456789', False, 3, True)
print('-'*25)
print_solution(13)
```

    987,654,213 is divisible by 13. (Candidate # 4)
    Wall time: 998 µs
    9,876,542,130 is divisible by 13. (Candidate # 9)
    Wall time: 999 µs
    123,456,879 is divisible by 13. (Candidate # 3)
    Wall time: 0 ns
    1,023,456,798 is divisible by 13. (Candidate # 2)
    Wall time: 0 ns
    -------------------------
    13-divisible:
        Largest  1-9:	987,654,213
        Largest  0-9:	9,876,542,130
        Smallest 1-9:	123,456,879
        Smallest 1-9:	1,023,456,798
    

A tie, in both timing and number of candidates!

So, it might seem useless to use all these divisibilty rules-- and perhaps while using a modern computer, with all the libraries included with a language like Python, it might be.

But let's consider the calculations involved a little more carefully, and think about what these divisibility rules allow a human to do. In the case of finding the largest 0-9 pandigital number divisible by 13, either approach requires the evaluation of 9 candidates. The naive approach requires long division of 9 10-digit numbers by 13. Let's adapt our block-addition code to keep track of how many long divisions of blocks are required.


```python
from collections import defaultdict

division_count = defaultdict(lambda: 0)


def ba_search_divisible_by(n, digit_set, largest,
                           rule_block_size, alternating_addition,
                           incoming_remainder = 0, incoming_number = ""):
    global candidate_count
    
    # how big is this block?
    if len(digit_set) % rule_block_size == 0:
        block_size = rule_block_size
    else:
        block_size = len(digit_set) % rule_block_size
        
    # determine if this is a negative term, if alternating addition is specified
    if alternating_addition:
        block_number = (len(digit_set) - block_size) // rule_block_size + 1
        negative_term = block_number % 2 == 0
    else:
        negative_term = False
        
    for value_str in sorted(digit_subsets(digit_set, block_size), reverse=largest):
        if incoming_number == "" and value_str[0] == '0': # leading 0s are not allowed
            continue
        
        new_number = incoming_number + value_str
        value = int(value_str)
        remainder = value % n
        division_count[block_number] += 1
        
        if negative_term:
            new_remainder = (incoming_remainder - remainder) % n
        else:
            new_remainder = (incoming_remainder + remainder) % n
        
        rem_digits = digit_set - set(c for c in value_str)
        
        if len(rem_digits) == 0: # this is the final term
            candidate_count += 1
            if new_remainder == 0: #qualifying number
                number_string = f"{int(new_number):,}"
                print(f"{number_string} is divisible by {n:,}. (Candidate # {candidate_count:,})")
                print(f"  Block division counts: {sorted(division_count.items(), reverse=True)}")
                yield new_number
        else: # move on to next block
            for result in ba_search_divisible_by(n, rem_digits, largest,
                                                rule_block_size, alternating_addition,
                                                new_remainder, new_number):
                yield result


%time ba_first_divisible_by(13, '9876543210', True, 3, True)
```

    9,876,542,130 is divisible by 13. (Candidate # 9)
      Block division counts: [(4, 1), (3, 1), (2, 2), (1, 9)]
    Wall time: 0 ns
    




    (0, '9876542130')



Our method required 1 division of the first block (which was a 1-digit number, so barely counts), and then 12 divisions of the other blocks combined, each of which was a 2- or 3-digit number. 12 long-divisions of 3-digit numbers is far easier for a human (or slow computer) than 9 long-divisions of 10-digit numbers.

So let's not throw out the divisibility rules just yet!
