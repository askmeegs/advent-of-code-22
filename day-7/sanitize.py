# convert all directory names to uuids 
import uuid
def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    parent = ""
    for i, line in enumerate(lines):
        # lcgv_cthtlwds 
        if line.startswith("$ cd") and line != "$ cd ..":
            spl = line.split("_")
            # get last item in spl
            parent = spl[len(spl) - 1]
        if line.startswith("dir"):
            oldName = line.split(" ")[1]
            lines[i] = "dir " + parent + "_" +  oldName

    with open('sanitized.txt', 'w') as f:
        for line in lines:
            f.write(line + "\n")

# execute main
if __name__ == '__main__':
    main()