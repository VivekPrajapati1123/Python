def Greet(**names):
    for i in names.values():
        print(f"Good Afternoon {i}")
Greet(name1="Rahul",name2="Vivek")