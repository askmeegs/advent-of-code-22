"""
🐵 Keep-away 

predict where monkeys will throw items. 
monkeys operate based on "worry level." 
the input is your notes of which items the monkey has, and how the monkey makes decisions

For instance:
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Starting items is the WORRY LEVEL for each item. eg. 
2 items, worry level 79 and 98.

The monkey then inspects an item. 
The operation is how my worry level changes AFTER inspection. 

Test is how the monkey uses worry level to decide where to throw next.

Procedure goes:
1. Monkey inspects an item
2. Relief -  worry / 3 (rounded down to nearest int) 
3. Test worry level --> take action based on test T or F 

When an item is thrown, it goes to the END of the recipient's list. 

On 1 monkey's turn, it inspects ALL ITS ITEMS in the order listed. 
When all monkeys take 1 turn, that = 1 ROUND. 
A monkey could start a round with 0 items, but by its turn, have 3 items. 

If a monkey isn't holding any items, its turn ends immediately. 


TASK - count the total number of items each monkey inspected over
20 ROUNDS. 
Find the two most active monkeys and multiply their item count together. 
This is the "monkey business score." 

Again, return the monkey business score after 20 rounds.  
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
    for round in range(20):
        print("\n\n🙊 ROUND {}".format(round)) 
        # each monkey gets 1 turn, to look at all its items. 
        for mIndex in range(0, monkeyCount): 
            print("Monkey {}".format(mIndex))
            """
            Monkey, go through all items: 
                1. Monkey inspects an item (executes operation)
                2. Relief -  worry / 3 (rounded down to nearest int) 
                3. Test worry level --> take action based on test T or F 
                When an item is thrown, it goes to the END of the recipient's list. 
            """
            m = monkeys[mIndex]
            print(m["items"])
            # go through all my items. they should all get thrown. 
            for item in m["items"]: 
                print("\tMonkey {} inspects an item with a worry level of {}".format(mIndex, item))
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
                print("\t\tWorry level is is operanded-ed by {} to {}".format(operand, item))
                # 2. execute relief 
                # update item (worryVal) by dividing by 3, round down to nearest int 
                item = item // 3 
                print("\t\t Monkey gets bored with item. Worry level is divided by 3 to {}".format(item))
                # what to do with this item? 
                # 3. execute test
                # if item % test_divisible == 0, throw to true_throw_to
                # else, throw to false_throw_to
                if item % m["test_divisible"] == 0:
                    # throw to true_throw_to
                    target = m["true_throw_to"]
                    print("\t\t Current worry level is divisible by {}".format(m["test_divisible"]))
                else:
                    # throw to false_throw_to
                    print("\t\t Current worry level is not divisible by {}".format(m["test_divisible"]))
                    target = m["false_throw_to"]
                # add item to the end of target's list
                monkeys[target]["items"].append(item)
                print("\t\t Item with worry level {} is thrown to monkey {}".format(item, target))
            # update monkeys dict
            m["items"] = []
            monkeys[mIndex] = m 


    # get final score 
    print("🏁 DONE")
    print(json.dumps(monkeys, sort_keys=True, indent=4))
    # get the top 2 values of looked_at
    top2 = sorted(monkeys.values(), key=lambda x: x["looked_at"], reverse=True)[:2]
    # multiply them 
    score = top2[0]["looked_at"] * top2[1]["looked_at"]
    print(score)


# execute main
if __name__ == '__main__':
    main()