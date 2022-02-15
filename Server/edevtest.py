import edev
while 1:
    sel = input("def: ")
    if sel == "bastfr":
        call1 = input("ba: ")
        call2 = input("st: ")
        call3 = input("fr: ")
        edev.bastfr(call1, call2, call3)
    if sel == "mosc":
        call1 = input("mo: ")
        call2 = input("sc: ")
        edev.mosc(call1, call2)