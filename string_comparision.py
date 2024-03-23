#Two strings comparision, if equal a=b        (10M)
#if a subset of b then output a<b,
#if b subset of a then output a>b
#else a!=b

def compare_string(a, b):
    if a == b:
        print("a=b")
    elif set(a) < set(b):
        print("a<b")
    elif set(b) < set(a):
        print("a>b")
    else:
        print("a!=b")
string1 = input("enter 1st sentence\n")
string2 = input("enter 2nd sentence\n")
compare_string(string1, string2)