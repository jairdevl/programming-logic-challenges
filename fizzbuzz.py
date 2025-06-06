def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
            print("fizzbuzzboom")
        elif i % 3 == 0 and i == 5:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 7 == 0:
            print("boom")
        else:
            print(i)

fizzbuzz()