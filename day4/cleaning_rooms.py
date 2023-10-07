
with open("day4/data_1.txt") as f:
    
    lines = f.readlines()
    
    sum = 0
    sum2 = 0
    
    for line in lines:
        line = line.strip()
        
        rooms_1, rooms_2 = line.split(",")[0], line.split(",")[1]
        r1_1, r1_2 = int(rooms_1.split("-")[0]), int(rooms_1.split("-")[1])
        r2_1, r2_2 = int(rooms_2.split("-")[0]), int(rooms_2.split("-")[1])
        
        if r1_1 <= r2_1 and r1_2 >= r2_2:
            sum += 1
            continue
        if r2_1 <= r1_1 and r2_2 >= r1_2:
            sum += 1
    
    for line in lines:
        rooms_1, rooms_2 = line.split(",")[0], line.split(",")[1]
        r1_1, r1_2 = int(rooms_1.split("-")[0]), int(rooms_1.split("-")[1])
        r2_1, r2_2 = int(rooms_2.split("-")[0]), int(rooms_2.split("-")[1])
        
        set1= set((range(r1_1, r1_2+1)))
        set2 = set((range(r2_1, r2_2+1)))
        intersec = set1 & set2
        if intersec:
            sum2 += 1
    
# Part one
print("1:", sum)

print("2:", sum2)
    
    