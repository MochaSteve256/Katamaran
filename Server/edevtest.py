import edev
while 1:
    sel = input("def: ")
    if sel == "bastfr":
        call1 = input("ba: ")
        try: call1 = bool(call1)
        except:
            pass
        call2 = input("st: ")
        try: call2 = bool(call2)
        except:
            pass
        call3 = input("fr: ")
        try: call3 = bool(call3)
        except:
            pass
    edev.bastfr(call1, call2, call3)
    if sel == "mosc":
        call1 = input("mo: ")
        try: call1 = bool(call1)
        except:
            pass
        call2 = input("sc: ")
        try: call2 = bool(call2)
        except:
            pass
    edev.mosc(call1, call2)