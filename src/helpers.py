def simplelist():
    words = open("testdata/makeplural_test.txt", "r").readlines()
    temp = []
    for w in words:
        temp.append(w.strip())
    return temp
