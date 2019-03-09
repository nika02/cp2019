def find_num_uppercase(str):
    count = 0
    for i in str:
        if(i.isupper()):
            count = count + 1
    print(count)
find_num_uppercase("GooD mOrning")
