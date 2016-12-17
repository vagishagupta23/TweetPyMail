import os
choice=raw_input("Enter your choice: 1)Tweet \n 2)Email\n")
if choice == "1":
        from fir import func2
        func2()
elif choice == "2":
        from mail import func1
        func1()
else:
        print("Invalid")
