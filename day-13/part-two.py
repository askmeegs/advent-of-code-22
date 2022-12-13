def main(): 
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]


# execute main
if __name__ == '__main__':
    main()