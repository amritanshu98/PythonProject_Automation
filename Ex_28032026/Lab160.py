class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number: "))
            print("You have entered:",a)
        except Exception as e:
            print("Enter int only value of a")
        finally:
            print("FINALLY : Anyhow I will be printed")


x = XYZ()
x.f1()