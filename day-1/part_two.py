def main():
    print("Calculating the top 3 elves with the most calories...")
    # read in input.txt into a list of integers
    with open("input.txt") as f:
        lines = f.readlines()
    elves = []
    elf_total = 0
    for line in lines:
        # is the line a newline?
        if line == "\n":
            elves = elves + [elf_total]
            elf_total = 0
            continue # skip to next line
        # otherwise, we're still on the current elf 
        # strip whitespace over line
        line = line.strip()
        # convert to int 
        int_line = int(line)
        elf_total = elf_total + int_line 
    # sort elves in descending order
    elves.sort(reverse=True)
    # get the sum of the top 3 
    top_3 = elves[0] + elves[1] + elves[2]
    print(top_3)


if __name__ == "__main__":
    main()