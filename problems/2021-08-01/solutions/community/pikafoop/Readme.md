[https://youtu.be/AFSWukfYyZs](https://youtu.be/AFSWukfYyZs) || [GitHub](https://github.com/somacdivad/recreational-mathematics-problems/tree/main/problems/2021-08-01) || [Twitter](https://twitter.com/somacdivad/status/1422965666110492673)

# Blank Divisibility

This week's puzzle is about filling in blanks in a number so that it's divisible by another number.

How many ways are there to fill in the blanks for

5_3_1_672

with the digits 4, 9, and 8, in some order, so that the resulting number is divisible by 792?

_This problem is Problem 4.35 in Problem Solving Through Recreational Mathematics by Bonnie Averbach and Orin Chein._

Feel free to use your favorite programming language to solve the problem.

If you can immediately see a way to solve this problem with code, then I challenge you to come up with a solution that *doesn't* check all possible combinations of 4, 9, and 8. Can you find a way to limit the search space?

You can submit solutions via pull request or by emailing your code to recmath@davidamos.dev. If you submit a pull request, make sure your solution is added to the `solutions/community/` folder.

> **Note:** By submitting a solution you agree to make the code for your solution available under the MIT license.

I'll feature my solution and a couple of my favorite submitted solutions in a YouTube video!

<hr/>

_Some time later..._

And, as a bonus challenge, given a "number" with some blank digits, and some number N, can you find all the ways to fill in the blanks with digits so that the resulting number is divisible by N?

<hr/>

_NB: I'm going to do my best to make this explanation thorough and understandable to someone who only has junior-high math and programming training. I'm not an educator, though, so I might not get the audience level just right. I'll write my code in the way that I would normally write it to explore this problem (except maybe with longer variable names)._

_If you already know about modulo arithmetic, all of this may seem painfully obvious. Or maybe I'll get something wrong!_

_I will rely on "list comprehensions" and "dict comprehensions" in my Python code, in order to quickly build up data structures that might otherwise require `for` loops to create. If you're browsing this solution and see something you don't recognize, I suggest you start by looking up those search terms. (And try using them! They can make your code read more like the thoughts that you are trying to express, and even lead to more efficient code.)_

### Insight: Setting those three digits is creating and summing four numbers

In case it's not too obvious to state, each digit in a number is a number to be multiplied by a power of 10 in a sum. For instance: `1,234 = 1,000 + 200 + 30 + 4 = 1*10^3 + 2*10^2 + 3*10^1 + 4*10^0`

If we set the numbers in order {4,9,8}, we get `543,918,672 = 503,010,672 + 40,000,000 + 900,000 + 8,000`. (Since we are using addition, order does not matter, and partial additions are allowed. We just added up all the non-blank digits' values to make the first term.)

Looking at that formula, we can see that the "base number" is 503,010,672 when we set all the blanks to 0. Then for each permutation (ordering) a,b,c of {4,9,8}, we have a number `p = a*10,000,000 + b*100,000 + c*1,000`. There will be 6 of these, as there are 6 orderings possible of 3 unique digits: 4,9,8; 4,8,9; 9,4,8...


### Insight: A number _n_ is divisible by _m_ if _n_ mod _m_ equals 0

Modulo arithmetic (sometimes called "clock arithmetic") is arithmetic in which we only count remainders. The "clock arithmetic" moniker comes from the fact that this is how a 24-hour clock works (and a 12-hour clock, if you substitute "0" for "12" and ignore AM/PM). If it's 23:00 (11 PM) and you add 2 hours, it's not 25:00 (13 PM) but 1:00 (1 AM), because 25 mod 24 = 1 (13 mod 12 = 1).

Starting from the top of the clock and getting back there means going completely around, no matter how many times we go around. So any number _n_ we add to, say, our 24 hour clock that is divisible by 24 just gets us back to the top after going around _n_ / 24 times.

Once we understand that we're in a cyclic system, we realize that we are just walking around our limited circle of numbers and seeing where we stop. You could think of any number _n_ as `n = x*m + r`, with _x_ trips the whole way around the clock and a remainder _r_. We can throw away _x_ because each time we take _m_ steps we're back at 0, so `n mod m = r`. If _r_ = 0, we made a whole number of trips, and _n_ must have been divisible by _m_.

### Insight: A number _s_ mod _m_ is equal to the sum of _n1, n2, ..._ mod _m_ if the sum of _n1 + n2 + ..._ equals _s_

Now think of breaking our trip up into smaller segments _n_ = _a_,_b_,_c_... It doesn't matter what those segments are, since we'll end up at the same place as if we took the trip _n_ all at once.

### Synthesis

In this case, our modulus is 792 (so our "clock" has 792 hours on it).

We now use our program to find a solution using these tools:

- The value of the "blank" number with zeros in the blank spaces `n = 503,010,672`
- The value of _n_ modulo 792 `mn = 503,010,672 mod 792 = 384`
- The sum of the values of each permutation of digits in their tens places, for instance `p = 40,000,000 + 900,000 + 8,000 = 40,908,000` in the order given in the problem statement.
- The value of each _p_ modulo 792 `mp = p mod 792`

Now we determine which values of `mn + mp mod 792` are 0. `mn = 384`, so we can filter out only the _p_ for which `mp = 408`.

After this step is complete, we can use the results to develop a more complex filter.


```python
from itertools import permutations
from pprint import pprint

base_number = 503010672
modulus = 792
digit_permutations = permutations( (4, 9, 8) )

perm_numbers = { a*10**7 + b*10**5 + c*10**3: (a,b,c) for (a,b,c) in digit_permutations } # NB: dict comprehension
pprint(perm_numbers)

print('-' * 25)
    
base_modulo = base_number % modulus # we write "n mod m" in Python as "n % m"
print(f"{base_number:,} mod {modulus} = {base_modulo}")
perm_modulos = [(p % modulus, p) for p in perm_numbers ] # NB: list comprehension

pprint(perm_modulos)
```

### The Trick

We pause here, because we've stumbled upon a trick. Each permutation of {4,9,8} yields a number _n_ for which _n_ mod 792 = 408.

503,010,672 mod 792 = 384;

384 + 408 = 792;

792 mod 792 = 0.

Each of the 6 permutations yields a number divisible by 792, so:

# The Answer is 6 (or: all of them)

<hr/>

### Pulling apart the trick

Let's first explore the value of every component we can use in building up our final number, and see if there are any obvious patterns there.


```python
from itertools import product

sub_modulos = [ (a*p % modulus, a*p) for a, p in product( (4,9,8), (10**3,10**5,10**7) ) ]

pprint(sub_modulos)
```

Each position for the 4 yields a remainder of 40; 8, 80; 9, 288– it's a mechanism where the order we choose doesn't matter, as long as we pick one of each. Since `384 + 40 + 80 + 288 = 792 = 0 mod 792`, every order works.

In order for this to work, the _differences_ between each of the digits' positional values must be 0 mod 792. To make this work, somacdivad will have generated the following values, or chosen them very carefully:

```
m = 792

a = 4000
a * 99 mod 792 = 0
a * 9999 mod 792 = 0

b = 9000
b * 99 mod 792 = 0
b * 9999 mod 792 = 0
```

(Note that we get `c = 8000` for free, since `c*99 mod 792 = a*2*99 mod 792 = 0`, and the same for 9999.) 


```python
from itertools import product
# We already imported `product` above, but I want each code block to contain all
# its own references, and re-importing does not have any unwanted side-effects.

m = 792
a = 4000
b = 9000
c = 8000

[(a*x % 792, f"{a:,}*{x:,} = {a*x:,}") for (a, x) in product((4000, 8000, 9000), (99, 9999))]
```




    [(0, '4,000*99 = 396,000'),
     (0, '4,000*9,999 = 39,996,000'),
     (0, '8,000*99 = 792,000'),
     (0, '8,000*9,999 = 79,992,000'),
     (0, '9,000*99 = 891,000'),
     (0, '9,000*9,999 = 89,991,000')]



Having shown this, a remaining question is how exactly the authors came upon these values.

I suspect that they could have done the following:

- Found or generated `a = 4,000; b = 9,000; m = 792` (or the same for 400,000 and 900,000)
- Found or realized that `c = 8,000` has the same property as `a = 4,000`
- Calculated `a mod m + b mod m + c mod m = 408`
- Calculated `n = 503,010,672` based on the criteria `n mod m = 464` and `0 in 1,000 and 100,000 and 10,000,000 places`

However, it's not unlikely that they did these in a different order, such as calculating _a_, _b_, and _m_, finding suitable candidates for _n_, realizing that an 8 was in a fortuitous place in one candidate and assigning _c_ accordingly. The clue that 8 was chosen after 4 and 9 is in the language of the question: 4, 9, and 8 are always presented in that order.

The most interesting question to me is that of the origin of `m = 792`. If he has insights on the origin of the puzzle from the book, perhaps somacdivad will share them with us during the solution video!

<hr/>

### Bonus Question

"And, as a bonus challenge, given a "number" with some blank digits, and some number N, can you find all the ways to fill in the blanks with digits so that the resulting number is divisible by N?"

(I had already begun work on another section, "Building our own version", before this additional challenge was issued on Twitter. This bonus problem is basically the same, but seems to be easier to express, so we'll do this instead.)

_Warning, some variable names change in this section!_

When we are doing this work on a contemporary computer, it's tempting to use brute force to solve these problems. Even if we had 10 blank digits, there are only `10! = 3,628,800` permutations of the 10 digits (`9! = 362,880` if you don't use zeros), and asking a computer to do a few million divisibility checks won't take any time at all. (The environment I'm writing this in takes < 1 second to iterate through all possible permutations of 10 digits.) In fact, the algorithm we implement here will still technically be brute force, but it will be checking every combination of digits for divisibility instead of checking just the resultant value. It's slower than just checking that resultant value, but still pretty much instantaneous.

We'll generate a similar problem to the one above:

- A 9-digit number with 3 "blanks"
- A 3-digit number to use as a modulus/divisor
- Neither number ends in "0" (to keep things interesting)
- If the 9-digit number is odd, so is the 3-digit number (to keep things possible - an odd number cannot be evenly divided by an even number)

We'll also look for every possible solution, including ones that have repeated digits or use 0's. The output will be quite verbose, so we can see how the solution was found.


```python
from random import randrange
from itertools import permutations

# choose a number with 3 blanks "b" and a modulus "n" of the same order as the original problem
def choose_problem():
    b = 1
    while b%10 == 0 or str(b).count('0') != 3:
        b = randrange(10**8,10**9)
    
    n = 10
    while n%10 == 0 or (n%2 == 0 and b%2 == 1):
        n = randrange(100, 1000)
    
    return(b, n)

problem = choose_problem()
problem
```




    (651007082, 234)




```python
from itertools import combinations_with_replacement, permutations

digits = list(range(10)) # all digits from 0-9

# find the "blanks" in b, as epxressed by the 10's place of the missing digit (0) from left to right
find_blanks = lambda b: list(reversed([i for i, c in enumerate(reversed(str(b))) if c == '0']))

def find_solutions(b, n):
    print(f"Finding solutions for {str(b).replace('0', '_')} divisible by {n}...")
    
    bm = b % n
    print(f"~ {b:,} mod {n:,} = {bm:,}")
    
    cm = n - bm
    print(f"~ The compliment of {bm:,} is {cm:,}")
    print(f"~ Finding digits combinations that yield sub-numbers that sum to {cm} mod {n}...")
    
    solutions = []
    blanks = find_blanks(b)
    # ds will be every set of digits, with replacements, that can fit into the blanks
    for ds in combinations_with_replacement(digits, len(blanks)):
        # os will be every possible ORDERING of the digits in ds, since placement matters
        for os in sorted(set(permutations(ds))):
            subs = [d * 10**p for (d,p) in zip(os, blanks)]
            rems = [s % n for s in subs]
            subrem = sum(rems)
            if subrem % n == cm:
                fullnum = sum(subs) + b
                if fullnum % n != 0:
                    raise Exception(f"Something went wrong: {fullnum:,}%{n:,} != 0")
                print(f"~ Solution: {os} --> {fullnum:,} / {n:,} = {fullnum/n:,}")
                for s, r in zip(subs, rems):
                    print(f"~      {s:,} mod {n} = {r}")
                print(f"~      {' + '.join(str(r) for s in rems)} mod {n} = {subrem}")
                print(f"~      {bm} + {subrem} mod {n} = {bm + subrem} mod {n} = {(bm + subrem) % n}")
                solutions.append(os)
    
    print(f"~ {len(solutions):,} solution{'' if len(solutions) == 1 else 's'} found.")
    return solutions
    

b, n = problem
find_solutions(b, n)
```

    Finding solutions for 651__7_82 divisible by 234...
    ~ 651,007,082 mod 234 = 128
    ~ The compliment of 128 is 106
    ~ Finding digits combinations that yield sub-numbers that sum to 106 mod 234...
    ~ Solution: (7, 0, 0) --> 651,707,082 / 234 = 2,785,073.0
    ~      700,000 mod 234 = 106
    ~      0 mod 234 = 0
    ~      0 mod 234 = 0
    ~      0 + 0 + 0 mod 234 = 106
    ~      128 + 106 mod 234 = 234 mod 234 = 0
    ~ Solution: (1, 5, 1) --> 651,157,182 / 234 = 2,782,723.0
    ~      100,000 mod 234 = 82
    ~      50,000 mod 234 = 158
    ~      100 mod 234 = 100
    ~      100 + 100 + 100 mod 234 = 340
    ~      128 + 340 mod 234 = 468 mod 234 = 0
    ~ Solution: (9, 1, 6) --> 651,917,682 / 234 = 2,785,973.0
    ~      900,000 mod 234 = 36
    ~      10,000 mod 234 = 172
    ~      600 mod 234 = 132
    ~      132 + 132 + 132 mod 234 = 340
    ~      128 + 340 mod 234 = 468 mod 234 = 0
    ~ Solution: (2, 2, 3) --> 651,227,382 / 234 = 2,783,023.0
    ~      200,000 mod 234 = 164
    ~      20,000 mod 234 = 110
    ~      300 mod 234 = 66
    ~      66 + 66 + 66 mod 234 = 340
    ~      128 + 340 mod 234 = 468 mod 234 = 0
    ~ Solution: (2, 9, 5) --> 651,297,582 / 234 = 2,783,323.0
    ~      200,000 mod 234 = 164
    ~      90,000 mod 234 = 144
    ~      500 mod 234 = 32
    ~      32 + 32 + 32 mod 234 = 340
    ~      128 + 340 mod 234 = 468 mod 234 = 0
    ~ Solution: (7, 7, 2) --> 651,777,282 / 234 = 2,785,373.0
    ~      700,000 mod 234 = 106
    ~      70,000 mod 234 = 34
    ~      200 mod 234 = 200
    ~      200 + 200 + 200 mod 234 = 340
    ~      128 + 340 mod 234 = 468 mod 234 = 0
    ~ Solution: (4, 3, 9) --> 651,437,982 / 234 = 2,783,923.0
    ~      400,000 mod 234 = 94
    ~      30,000 mod 234 = 48
    ~      900 mod 234 = 198
    ~      198 + 198 + 198 mod 234 = 340
    ~      128 + 340 mod 234 = 468 mod 234 = 0
    ~ Solution: (3, 6, 7) --> 651,367,782 / 234 = 2,783,623.0
    ~      300,000 mod 234 = 12
    ~      60,000 mod 234 = 96
    ~      700 mod 234 = 232
    ~      232 + 232 + 232 mod 234 = 340
    ~      128 + 340 mod 234 = 468 mod 234 = 0
    ~ Solution: (8, 4, 4) --> 651,847,482 / 234 = 2,785,673.0
    ~      800,000 mod 234 = 188
    ~      40,000 mod 234 = 220
    ~      400 mod 234 = 166
    ~      166 + 166 + 166 mod 234 = 574
    ~      128 + 574 mod 234 = 702 mod 234 = 0
    ~ Solution: (9, 8, 8) --> 651,987,882 / 234 = 2,786,273.0
    ~      900,000 mod 234 = 36
    ~      80,000 mod 234 = 206
    ~      800 mod 234 = 98
    ~      98 + 98 + 98 mod 234 = 340
    ~      128 + 340 mod 234 = 468 mod 234 = 0
    ~ 10 solutions found.
    




    [(7, 0, 0),
     (1, 5, 1),
     (9, 1, 6),
     (2, 2, 3),
     (2, 9, 5),
     (7, 7, 2),
     (4, 3, 9),
     (3, 6, 7),
     (8, 4, 4),
     (9, 8, 8)]



We can now generate and solve problems to our hearts' content. Note that some problems have no solutions.


```python
for x in range(3):
    print('-'*25)
    b, n = choose_problem()
    find_solutions(b, n)
    print('-'*25)
```

    -------------------------
    Finding solutions for 24___8126 divisible by 991...
    ~ 240,008,126 mod 991 = 809
    ~ The compliment of 809 is 182
    ~ Finding digits combinations that yield sub-numbers that sum to 182 mod 991...
    ~ Solution: (9, 7, 1) --> 249,718,126 / 991 = 251,986.0
    ~      9,000,000 mod 991 = 729
    ~      700,000 mod 991 = 354
    ~      10,000 mod 991 = 90
    ~      90 + 90 + 90 mod 991 = 1173
    ~      809 + 1173 mod 991 = 1982 mod 991 = 0
    ~ 1 solution found.
    -------------------------
    -------------------------
    Finding solutions for 6894___59 divisible by 113...
    ~ 689,400,059 mod 113 = 54
    ~ The compliment of 54 is 59
    ~ Finding digits combinations that yield sub-numbers that sum to 59 mod 113...
    ~ Solution: (6, 3, 0) --> 689,463,059 / 113 = 6,101,443.0
    ~      60,000 mod 113 = 110
    ~      3,000 mod 113 = 62
    ~      0 mod 113 = 0
    ~      0 + 0 + 0 mod 113 = 172
    ~      54 + 172 mod 113 = 226 mod 113 = 0
    ~ Solution: (4, 0, 4) --> 689,440,459 / 113 = 6,101,243.0
    ~      40,000 mod 113 = 111
    ~      0 mod 113 = 0
    ~      400 mod 113 = 61
    ~      61 + 61 + 61 mod 113 = 172
    ~      54 + 172 mod 113 = 226 mod 113 = 0
    ~ Solution: (0, 6, 5) --> 689,406,559 / 113 = 6,100,943.0
    ~      0 mod 113 = 0
    ~      6,000 mod 113 = 11
    ~      500 mod 113 = 48
    ~      48 + 48 + 48 mod 113 = 59
    ~      54 + 59 mod 113 = 113 mod 113 = 0
    ~ Solution: (2, 9, 1) --> 689,429,159 / 113 = 6,101,143.0
    ~      20,000 mod 113 = 112
    ~      9,000 mod 113 = 73
    ~      100 mod 113 = 100
    ~      100 + 100 + 100 mod 113 = 285
    ~      54 + 285 mod 113 = 339 mod 113 = 0
    ~ Solution: (5, 1, 7) --> 689,451,759 / 113 = 6,101,343.0
    ~      50,000 mod 113 = 54
    ~      1,000 mod 113 = 96
    ~      700 mod 113 = 22
    ~      22 + 22 + 22 mod 113 = 172
    ~      54 + 172 mod 113 = 226 mod 113 = 0
    ~ Solution: (1, 7, 8) --> 689,417,859 / 113 = 6,101,043.0
    ~      10,000 mod 113 = 56
    ~      7,000 mod 113 = 107
    ~      800 mod 113 = 9
    ~      9 + 9 + 9 mod 113 = 172
    ~      54 + 172 mod 113 = 226 mod 113 = 0
    ~ Solution: (7, 4, 3) --> 689,474,359 / 113 = 6,101,543.0
    ~      70,000 mod 113 = 53
    ~      4,000 mod 113 = 45
    ~      300 mod 113 = 74
    ~      74 + 74 + 74 mod 113 = 172
    ~      54 + 172 mod 113 = 226 mod 113 = 0
    ~ Solution: (8, 5, 6) --> 689,485,659 / 113 = 6,101,643.0
    ~      80,000 mod 113 = 109
    ~      5,000 mod 113 = 28
    ~      600 mod 113 = 35
    ~      35 + 35 + 35 mod 113 = 172
    ~      54 + 172 mod 113 = 226 mod 113 = 0
    ~ Solution: (9, 6, 9) --> 689,496,959 / 113 = 6,101,743.0
    ~      90,000 mod 113 = 52
    ~      6,000 mod 113 = 11
    ~      900 mod 113 = 109
    ~      109 + 109 + 109 mod 113 = 172
    ~      54 + 172 mod 113 = 226 mod 113 = 0
    ~ 9 solutions found.
    -------------------------
    -------------------------
    Finding solutions for 8_86_9_81 divisible by 191...
    ~ 808,609,081 mod 191 = 76
    ~ The compliment of 76 is 115
    ~ Finding digits combinations that yield sub-numbers that sum to 115 mod 191...
    ~ Solution: (5, 1, 6) --> 858,619,681 / 191 = 4,495,391.0
    ~      50,000,000 mod 191 = 20
    ~      10,000 mod 191 = 68
    ~      600 mod 191 = 27
    ~      27 + 27 + 27 mod 191 = 115
    ~      76 + 115 mod 191 = 191 mod 191 = 0
    ~ Solution: (3, 7, 2) --> 838,679,281 / 191 = 4,390,991.0
    ~      30,000,000 mod 191 = 12
    ~      70,000 mod 191 = 94
    ~      200 mod 191 = 9
    ~      9 + 9 + 9 mod 191 = 115
    ~      76 + 115 mod 191 = 191 mod 191 = 0
    ~ Solution: (2, 8, 9) --> 828,689,981 / 191 = 4,338,691.0
    ~      20,000,000 mod 191 = 8
    ~      80,000 mod 191 = 162
    ~      900 mod 191 = 136
    ~      136 + 136 + 136 mod 191 = 306
    ~      76 + 306 mod 191 = 382 mod 191 = 0
    ~ Solution: (4, 4, 4) --> 848,649,481 / 191 = 4,443,191.0
    ~      40,000,000 mod 191 = 16
    ~      40,000 mod 191 = 81
    ~      400 mod 191 = 18
    ~      18 + 18 + 18 mod 191 = 115
    ~      76 + 115 mod 191 = 191 mod 191 = 0
    ~ 4 solutions found.
    -------------------------
    

With modifications to `choose_problem`, we could pick problems with variations of sizes and contstraints on _b_ and _N_, but this example suffices.

<hr/>

### Next Steps

We have used up all the time we had to devote to this problem. But, now that we can generate and solve random problems, it might be interesting to find problems that also contain the "trick" present in the original problem. That is to say:

- Blanks that can accept a set of digits in any order
- Sets of digits that do not contain 0 or 1
- Sets of digits with a greatest common divider of 1

We could just let the random generator run until it finds a problem with these characteristics, but it would be more fun to build a loop to generate such a problem. If we were to begin such a project, I recommend this algorithm as a starting point, and then seek optimizations. (Each starred point can represent the beginning of a nested search, so the order of this algorithm is likely to be exponential.)

- Set the desired number of "blanks" for the problem
- (*) Generate sets of 10's places _p1_, _p2_,.. for the blanks
- Set a desirable range for _N_, perhaps based on the _p_ values
- (*) Generate candidate values for _N_
- (*) Find digits _d1_, _d2_,.. for which each _d_ multiplied by 10 to the power of each _p_ modulo _N_ is the same

If there are suitable digits for a value of _N_, we have a solution in search of a problem.

- Set the desirable range for the "blanks" number _b_, again based on the _p_ values
- (*) Generate candidate values for _b_ with zeros in the _p_ places
- Once a _b_ is found where `b mod N = N - (d1*10^n + d2*10^n + ...) mod N`, we have found the problem!


```python

```
