p = "hello.text"
with open(p, "r") as files:
    for line in files:
        a = line.rstrip()
        print(a)


with open("testing.text", "w") as f:
    f.write("hello there we are writing from another file \n")


# c = "this is a string"
# d = c.split(" ")
# result = "-".join(d)
# print(result)
