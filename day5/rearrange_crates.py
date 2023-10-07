from queue import LifoQueue

with open("day5/data_1.txt") as f:
    
    lines = f.readlines()
    
    # Find the index where the line is: 1 2 3 etc
    index = -1
    for i, line in enumerate(lines):
        if line.startswith(" 1"):
            index = i
            break
    
    # Get the number of columns
    columns_number = len(lines[index].strip().split("   "))

    # Create a stack for each column
    columns = [LifoQueue() for _ in range(columns_number)]
    
    # Create a list for part_two
    columns_part_two = [list() for _ in range(columns_number)]
    
    # Populate the lifos
    index_temp = index - 1
    while index_temp >= 0:
        
        line = lines[index_temp]
        
        for column in range(columns_number):
            init_pos = 4*column + 1
            final_pos = init_pos + 1
            char = line[init_pos:final_pos]
            
            if char != " ":
                columns[column].put(char)
                columns_part_two[column].append(char)

        index_temp -= 1
        
    # Move the crates
    for moving_line in list(map(str.strip, lines[index+2:])):
        indications = moving_line.split(" ")
        quantity = int(indications[1])
        from_column = int(indications[3])
        to_column = int(indications[5])
        
        for _ in range(quantity):
            columns[to_column-1].put(columns[from_column-1].get())
            
        columns_part_two[to_column-1].extend(columns_part_two[from_column-1][-quantity:])
        del columns_part_two[from_column-1][-quantity:]
            
    # Part 1
    # Print the result
    for column in columns:
        print(column.get(), end="")
    
    
    print()
    # Part 2
    for column in columns_part_two:
        print(column[-1], end="")