import edev
while 1:
    sel = input("def: ")
    if sel == "stuff":
        call1 = input("ba: ")
        call2 = input("st: ")
        call3 = input("fr: ")
        call4 = input("re: ")
        call5 = input("co: ")
        edev.bastfrreco(call1, call2, call3, call4, call5)
    if sel == "motor":
        call1 = input("mo: ")
        call2 = input("sc: ")
        edev.mosc(call1, call2)