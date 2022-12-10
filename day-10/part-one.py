def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    instr = [line.split() for line in lines]

    """
    addx V takes two cycles to complete. 
    noop takes 1 cycle to complete 

    SIGNAL STRENGTH = the cyclenumber * the current value of the X register 
    during the 20th .. 40th... 60th.. cycle 
    """
    xreg = 1
    strength_sum = 0 
    cyclenum = 1

    signals = {} 

    for i, item in enumerate(instr):
        print("\n\n processing insruction #{}: {}. xreg={}, cyclenum={}, strength_sum is {}".format(i, item, xreg, cyclenum, strength_sum))
        if len(item) == 1: # noop 
            print("🤫 it's a noop")
            signals[cyclenum] = cyclenum * xreg
            cyclenum += 1
        else: # addx 
            addVal = int(item[1])
            print("🧮 addx {}".format(addVal))
            signals[cyclenum] = cyclenum * xreg
            cyclenum += 1 
            print("addval waiting done, ready to add {} to {}".format(addVal, xreg))
            signals[cyclenum] = cyclenum * xreg
            xreg += addVal 
            cyclenum += 1 
    print("🏁 DONE")
    result = signals[20] + signals[60] + signals[100] + signals[140] + signals[180] + signals[220]
    print(result)
# execute main
if __name__ == '__main__':
    main()