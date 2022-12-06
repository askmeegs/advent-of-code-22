def main(): 
    with open('input.txt', 'r') as f:
        txt = f.read()
        txt = txt.strip()
        print(txt)
    # get all 14-character sequences in the file 
    # for each 14-character sequence, check if it has any duplicates
    # if it does, skip it
    # if it doesn't, print the index of the first character of the sequence
    sequences = {}
    for i in range(len(txt)-13):
        sequences[i+14] = txt[i:i+14]
    for k, v in sequences.items():
        if len(v) != len(set(v)):
            continue
        else:
            print(k)
            break

# execute main
if __name__ == '__main__':
    main()