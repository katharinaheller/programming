def weihnachtsbaum(a):
    for i in range(1, a+1):
        emptyspace = a-i
        stars = (i*2)-1

        space = emptyspace * " "
        star = stars * "*"
        print(space + star)
    print((a-2)*" "+"| |")
weihnachtsbaum(10)

