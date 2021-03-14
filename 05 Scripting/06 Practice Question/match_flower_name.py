def create_dict(file_name):
    flower_dict = {}
    with open(file_name) as f:
        for line in f:
            char = line.split(":")[0]
            flower = line.split(":")[1].strip()
            flower_dict[char] = flower
    return flower_dict

def flower_name():
    flowers_dict = create_dict("flowers.txt")
    name = input("Enter your First [space] Last name only: ")
    first = name[0].upper()
    flower_name = flowers_dict[first]
    message = "Unique flower name with the first letter: {}".format(flower_name)
    print(message)
    
flower_name()
