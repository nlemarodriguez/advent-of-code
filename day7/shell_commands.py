from typing import Union, List

total = 0

directories_dict = {}

class Directory:
    
    def __init__(self, path: str, parent) -> None:
        self.path = path
        self.items: List[Union[Directory, File]] = []
        self.parent: Union[Directory, None] = parent
        
    @property
    def size(self) -> int:
        return sum(item.size for item in self.items)
    
    def tree(self, prefix: str = "") -> str:
        
        for item in self.items:
            if isinstance(item, Directory):
                print(prefix+(item.__str__()))
                prefix += "\t"
                item.tree(prefix)
                prefix = prefix.replace("\t", "", 1)
            else:
                print(prefix+(item.__str__()))
        
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Directory):
            return self.path == other.path
        return False
    
    def __str__(self) -> str:
        return f"{self.path.split('/')[-2]} (dir, size={self.size} bytes)"
    
    @staticmethod
    def part_one(items) -> int:
        
        for item in items:
            if isinstance(item, Directory):
                if item.size <= 100_000:
                    global total 
                    total += item.size
                item.part_one(item.items)
                
    @staticmethod
    def part_one_pro(items) -> int:
        
        for item in items:
            if isinstance(item, Directory):
                
                global directories_dict 
                directories_dict[item.path] = item.size
                item.part_one_pro(item.items)

class File:
    
    def __init__(self, path: str, size: int) -> None:
        self.path = path
        self.size = size
        self.parent: Union[Directory, None] = None
        
    def __str__(self) -> str:
        return f"{self.path.split('/')[-1]} (file, size={self.size} bytes)"
    
    
with open("day7/data_1.txt") as f:
    
    current_path = "/"
    inside_ls = False
    root = Directory(current_path, None)
    current_directory = root
    
    lines = f.readlines()

    for line in lines[1:]:
        line = line.strip()
        
        if line.startswith("$ cd"):
            if line == "$ cd ..":
                current_path = current_path.split("/")[:-2]
                current_path = "/".join(current_path)+"/"
                current_directory = current_directory.parent
            else:
                new = line.split(" ")[-1]
                current_path += f"{new}/"
                directory = Directory(current_path, current_directory)
                current_directory.items.append(directory)
                current_directory = directory
            
        
        else:
            new = line.split(" ")[0]
            if new.isdigit():
                file = File(current_path+line.split(" ")[1], int(new))
                file.parent = current_directory
                file.parent.items.append(file)
            
    print()
    print("Arbol")
    root.tree()
    print(f"Total size: {root.size} bytes")
    #print("Part one size:", part_one_size)
    Directory.part_one(root.items)
    Directory.part_one_pro(root.items)
    print("Part one:", total)
    print("Part one_pro:", sum([v for v in directories_dict.values() if v <= 100_000]))
    
    filesystem_sapce = 70_000_000
    at_least_space = 30_000_000
    current_unused_space = filesystem_sapce - root.size
    
    order_dict = dict(sorted(directories_dict.items(), key=lambda x: x[1]))
    for value in order_dict.values():
        if value + current_unused_space >= at_least_space:
            print("Part two:", value)
            break