def main():
    print("Calculating the elf with the most calories...")
    # read in input.txt into a list of integers
    with open("input.txt") as f:
        lines = f.readlines()
    # while loop over lines
    elf_total = 0
    max_cals = 0
    for line in lines:
        # is the line a newline?
        if line == "\n":
            if elf_total > max_cals:
                max_cals = elf_total
            elf_total = 0
            continue # skip to next line
        # otherwise, we're still on the current elf 
        # strip whitespace over line
        line = line.strip()
        # convert to int 
        int_line = int(line)
        elf_total = elf_total + int_line 
    print(max_cals)

if __name__ == "__main__":
    main()