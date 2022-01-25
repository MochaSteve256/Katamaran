import edev
while 1:
    sel = input("def: ")
    if sel == "b":
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