"""
Fuel heating problem 

What is the total amount of fuel = sum of fuel requirements of all balloons

The fuel requirements are written on the side of a balloon in an unclear format, SNAFU. 

Which is sort of like base-5? 

... 625s place      125s place      25s place   5s place     1s place


1=-0-2
12111
2=0=
21

In regular base-5, you use digits 0, 1, 2, 3, and 4. 
In SNAFU, they're 2, 1, 0, - (equal to -1), and = (equal to -2) 

10 in base-10 is 20 (two fives, no ones) 
8 in base-10 is 2= (two fives, minus 2 ones)

2=-01 in SNAFU is 2 625s, -2 125s, -1 25s, 0 5s, and 1 1s = 

625*2 - 2*125 - 1*25 + 1*1 = 1250 - 250 - 25 + 1 = 976 


A confounding factor is the cold temperatures which the fuel was 
not designed to work in. 

You need to convert the SNAFU numbers to decimal, sum the DECIMAL numbers, 
then convert the sum to SNAFU. That's your output. 
"""

def main(): 
    with open('input.txt', 'r') as f:
        snafus = f.readlines()
        snafus = [line.strip() for line in snafus]
    # place 0, place 1, etc. 
    places = [] 
    for i in range(22):
        # append 5 to the power of i 
        places.append(5**i)
    print(places) 

    # read in the SNAFU numbers
    print(snafus)
    decimals = [] 
    for s in snafus:
        decimals.append(snafu_to_dec(s, places))
    
    print(decimals)

    # print the results 
    for i in range(0, len(snafus)):
        print("SNAFU: {}\t\tDECIMAL: {}".format(snafus[i], decimals[i]))

    # sum the values of decimals
    sum = 0
    for d in decimals:
        sum += d
    print("Sum of decimals: {}".format(sum))

    # convert sum to base 5 
    print("Sum in base 5: {}".format(dec_to_snafu(sum)))

    # convert sum to snafu
    # print("Sum in SNAFU: {}".format(dec_to_snafu(sum, places)))

# given a string snafu, convert to decimal integer 
"""
 SNAFU  Decimal
1=-0-2     1747
 12111      906
  2=0=      198
    21       11
  2=01      201
   111       31
 20012     1257
   112       32
 1=-1=      353
  1-12      107
    12        7
    1=        3
   122       37
"""

"""
1==12200-0=211---21=

Need 22 places for max len. 

"""
def snafu_to_dec(snafu, places): 
    sum = 0 
    # break snafu into list of characters
    snafu = list(snafu)
    for i, s in enumerate(snafu):
        e = len(snafu) - i - 1
        if s == '1':
            sum += places[e]
        elif s == '2':
            sum += 2*places[e]
        elif s == '0':
            sum += 0
        elif s == '-':
            sum -= places[e]
        elif s == '=':
            sum -= 2*places[e]
    return sum






"""
    Valid snafu characters: 1, 2, 0, -, =
    0, 1, 2 behave normally in base-5 
    - is -1 in base-5
    = is -2 in base-5

    Places is: 1, 5, 25, 125, 625, 3125... 

    4890 in snafu is: 2=-1=0
    or: 2*3125 - 2*625 - 1*125 + 1*25 - 2*5 + 0*1 = 4890 

    it's easy to calculate a decimal FROM a snafu... 
    getting from decimal TO snafu is hard because it's a balancing game. 

    4890 in snafu is: 2=-1=0
    it almost feels recursive ... 

    if I have the number 7, I know I can make it with two places, because 7 = 5 + 2.

    The key is that even though it's "sort of base 5," it's really not because you go 
    from 1="1", 2="2", 3="1=", 4="1-", 5="10" 

    3 is the first number that requires two places. 

  Decimal value          equals SNAFU value 
        1              1
        2              2
        3             1=
        4             1-
        5             10
        6             11
        7             12
        8             2=
        9             2-
       10             20
       15            1=0
       16            1=1
       20            1-0
     2022         1=11-2
    12345        1-0---0
314159265  1121-1110-1=0
"""

"""
How to convert decimal to regular base 5? 
http://mathcentral.uregina.ca/QQ/database/QQ.09.07/s/angela1.html 
http://www.unitconversion.org/numbers/base-10-to-base-5-conversion.html

419 in base 10 is ____ in base 5? 

Start with the whole number. Divide by 5. 
419/5 = 83 remainder 4. 

________4

83/5 = 16 remainder 3.


_______34


16 / 5 = 3 remainder 1.


______134

3 / 5 = 0 remainder 3.


419 base 10 = 3134 base 5 ✅
~~~~~~~~~~~~~`

Let's convert 16 to regular base 5 ...

16 / 5 = 3 remainder 1.

___1

3 / 5 = 0 remainder 3.

= 31 ✅
~~~~~~

Let's convert 16 into snafu...  (correct answer is 1=1)
In snafu, only remainders of 0, 1, and 2 are allowed. 
Remainders 3 and 4 must be "carried" into minus, and set to 3 --> =, 4 --> - 

16 / 5 = 3 remainder 1.
___1 

3 / 5 = 0 remainder 3.
A remainder of 3 is not allowed. so instead we have to carry 1 then double-minus.
_1=1 

~~~~~~~~~

20 to snafu
20 / 5 = 4 remainder 0.
____0

4 / 5 = 0 remainder 4.
A remainder of 4 is not allowed. so instead we have to carry 1 then minus - 
__1-0

~~~~~~~~~

2022 to snafu  (correct answer: 1=11-2)

2022 / 5 = 404 remainder 2.
______2

404 / 5 = 80 remainder 4.

_____42 
* A remainder of 4 is not allowed. so instead we have to carry 1 then minus -
____1-2 

80 / 5 = 16 remainder 0.
___01-2 

16 / 5 = 3 remainder 1.
__11-2

3 / 5 = 0 remainder 3.
__311-2 
* A remainder of 3 is not allowed. so instead we have to carry 1 then double-minus.
_1=11-2 

~~~~~~~~~

12345 to snafu (correct answer: 1-0---0)

12345 / 5 = 2469 remainder 0.
_______0

2469 / 5 = 493 remainder 4.
______40
* A remainder of 4 is not allowed. so instead we have to carry 1 then minus -
_____1-0

493 / 5 = 98 remainder 3.
____4-0 
* remainder 4 not allowed so carry 1 then - 
___1--0 

98 / 5 = 19 remainder 3.
___4--0 
* remainder 4 not allowed so carry 1 then -
__1---0

19 / 5 = 3 remainder 4.
__5---0
* a 5 is carred and becomes 0 
_10---0 

3 / 5 = 0 remainder 3.
_40---0
1-0---0 

"""

"""
9 in dec is 2- in snafu
"""
def dec_to_snafu(d):
    s = []
    while d > 0:
        q = d // 5
        r = d % 5
        if r == 0:
            s.insert(0, '0')
        elif r == 1:
            s.insert(0, '1')
        elif r == 2:
            s.insert(0, '2')
        elif r == 3:
            s.insert(0, '=')
            q += 1
        elif r == 4:
            s.insert(0, '-')
            q += 1
        d = q
    return ''.join(s)



# execute main
if __name__ == '__main__':
    main()