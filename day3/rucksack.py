import string

with open("day3/data_1.txt") as f:
    
    lines = f.readlines()
    
    # Part one
    sumatory = 0
    alphabet = string.ascii_letters
    
    for line in lines:
        
        first_part = set(line[:len(line)//2])
        second_part = set(line[len(line)//2:])
        common = str(list(first_part & second_part)[0])
        #print(common)
        sumatory += (alphabet.index((common))+1)
    
    print("1:", sumatory)
    
    # Part one (one line)
    total = sum([alphabet.index(list(set(line[:len(line)//2]) & set(line[len(line)//2:]))[0])+1  for line in lines])
    
    # Part two
    sumatory = 0
    for i in range(0, len(lines), 3):
        
        first_part = set(lines[i].strip())
        second_part = set(lines[i+1].strip())
        third_part = set(lines[i+2].strip())
        common = str(list(first_part & second_part & third_part)[0])
        sumatory += (alphabet.index((common))+1)
    
    print("2:", sumatory)
        
        