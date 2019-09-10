#!/usr/bin/python3
for i in range(1, 101):
    print("{}".format("FIzzBuzz" if not i % 3 and not i % 5 else "Fizz" if not
                      i % 3 else "Buzz" if not i % 5 else i), end=" ")
print()
