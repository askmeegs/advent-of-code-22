"""

Now run 10000 rounds. 
The worry level / 3 is gone. 

Here's the problem. We still have to complete operations and run tests. 
But the numbers get too big. With this implementation, using python, after round 37, things get extremely slow. 

Operations are + or * by a number < 100. 
Tests are of divisibility. 

is there any way to COMPRESS the item value to a smaller number? 

let's say with no compression, the item val is 1056. 
Operation is *4. 

We then have to test divisibility by 8. 
Without compression, we'd do 1056*4 = 4224.
Then 4224 % 8 = 0. 

The problem -- at least part of it -- lies in monkey #2. 
Its operation has you run an exponential function, old^2. 

aka old * old. 
is there any way to somehow get rid of this operation and replace it 
so that it's valid for future operations?

I have to run old * old then test divisibility by 2. what would produce 
the same outcome? 

What is an equivalent operation to old * old / 2 ? 
We're checking odd vs. even. 

an odd * odd = odd
an even * even = even 

so the result of the test will be the same even if we didn't do the operation. 
so instead let's just change the operation from old * old to old * 1. 

the issue with that, though, is that the absolute value of item will be lower.
so subsequent operations like *11, will fundamentally be different once the item
is thrown. 

so that didn't work. 
🙉 TRY AGAIN. 

a common property of all tests is divisibility by a prime number. 
there must be some hint there.... math and I are not friends. ugh 🥹 

https://www.quora.com/Is-the-square-of-a-prime-number-divisible-by-the-same-number-only 
so we know this.. once we HAVE a prime number, and we square it, 
(aka monkey 2 has it) 
the next test -- no matter what -- will result in FALSE because a square
 of a prime is only divisible by itself and 1. 


ok ok ... what if we keep all ops the same, keep squaring things...
BUT. as a way of cutting numbers down, we divide or mod by ... SOME AMOUNT.
instead of dividing arbitrarily by 3, we could MOD by the COMMON DIVISOR of all the prime dividends in all operations? 

let's see if that works... 
"""

import json
def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        print(lines)
    # parse input
    """
    monkey[0] = {"looked_at": 0, "items": [79, 98], "operation": "+", "operand": 19, "test_divisible": 5, "true_throw_to": 3, "false_throw_to": 2}
    monkey[1] = {"looked_at": 0 "items": [], "operation": "*", "operand": "old", "test_divisible": 1, "true_throw_to": 0, "false_throw_to": 1}
    """
    monkeys = {}
    monkeyCount = 8
    parsedMonkeys = 0 
    i = 0 
    common_divisor = 1 
    while parsedMonkeys < monkeyCount:
        monkeyIndex = parsedMonkeys
        m = {"looked_at": 0} 
        # skip the first line  Monkey # 
        i += 1 

        # starting items 
        start = lines[i].split(": ")[1] 
        m["items"] = [int(x) for x in start.split(", ")]
        monkeys[monkeyIndex] = m 
        i += 1 
        # operation 
        raw_op = lines[i].split(" = ")[1] 
        op = raw_op.split(" ")
        m["operation"] = op[1]
        m["operand"] = op[2]
        i+= 1 
        # test_divisible
        raw_test = lines[i].split(" by ")[1]
        m["test_divisible"] = int(raw_test)
        common_divisor *= m["test_divisible"]
        i+= 1 
        # test true 
        # get the last char in line 
        raw_true = lines[i].split("monkey ")[-1]
        m["true_throw_to"] = int(raw_true)
        i+= 1 
        # test false
        raw_false = lines[i].split("monkey ")[-1]
        m["false_throw_to"] = int(raw_false)
        i+= 1 

        parsedMonkeys += 1 

        # advance a line 
        i += 1 
        
    print(json.dumps(monkeys, sort_keys=True, indent=4))

    # run 20 rounds 
    for round in range(10000):
        print("\n\n🙊 ROUND {}".format(round)) 
        # each monkey gets 1 turn, to look at all its items. 
        for mIndex in range(0, monkeyCount): 
            # print("Monkey {}".format(mIndex))
            """
            Monkey, go through all items: 
                1. Monkey inspects an item (executes operation)
                2. Relief -  worry / 3 (rounded down to nearest int) 
                3. Test worry level --> take action based on test T or F 
                When an item is thrown, it goes to the END of the recipient's list. 
            """
            m = monkeys[mIndex]
            # print(m["items"])
            # go through all my items. they should all get thrown. 
            for item in m["items"]: 
                # print("\tMonkey {} inspects an item with a worry level of {}".format(mIndex, item))
                m["looked_at"] += 1
                # 1. execute operation 
                # get the true operand
                if m["operand"] == "old":
                    operand = item
                else:
                    operand = int(m["operand"])
                if m["operation"] == "+":
                    item += operand
                elif m["operation"] == "*":
                    item *= operand
                # print("\t\tWorry level is is operanded-ed by {} to {}".format(operand, item))
                # 2. execute relief 
                # update item (worryVal) by dividing by 3, round down to nearest int 
                item %= common_divisor 
                # print("\t\t Monkey gets bored with item. Worry level is divided by 3 to {}".format(item))
                # what to do with this item? 
                # 3. execute test
                # if item % test_divisible == 0, throw to true_throw_to
                # else, throw to false_throw_to
                if item % m["test_divisible"] == 0:
                    # throw to true_throw_to
                    target = m["true_throw_to"]
                    # print("\t\t Current worry level is divisible by {}".format(m["test_divisible"]))
                else:
                    # throw to false_throw_to
                    # print("\t\t Current worry level is not divisible by {}".format(m["test_divisible"]))
                    target = m["false_throw_to"]
                # add item to the end of target's list
                monkeys[target]["items"].append(item)
                # print("\t\t Item with worry level {} is thrown to monkey {}".format(item, target))
            # update monkeys dict
            m["items"] = []
            monkeys[mIndex] = m 


    # get final score 
    print("🏁 DONE")
    print("common divisor is ", common_divisor)

    # get the top 2 values of looked at 
    top2 = sorted(monkeys.items(), key=lambda x: x[1]["looked_at"], reverse=True)[:2]
    # multiply them 
    print(top2[0][1]["looked_at"] * top2[1][1]["looked_at"])

# execute main
if __name__ == '__main__':
    main()