class function:

    def Subfields():
        lists = [
            "Sub-fields in AI are:",
            "Machine Learning",
            "Neural Networks",
            "Vision, Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]

        for ch in lists:
            print(ch)

    def oddeven():
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print(num, "is an even number")
        else:
            print(num, "is an odd number")

    def elegible():
        gender = input("Your Gender: ")
        age = int(input("Your age: "))

        if gender == "male" and age >= 21:
            print("Eligible")
        elif gender == "female" and age >= 18:
            print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        sub1 = int(input("Subject1 = "))
        sub2 = int(input("Subject2 = "))
        sub3 = int(input("Subject3 = "))
        sub4 = int(input("Subject4 = "))
        sub5 = int(input("Subject5 = "))

        total = sub1 + sub2 + sub3 + sub4 + sub5
        print("Total:", total)

        percent = total / 500 * 100
        print("Percentage:", percent)

    def triangle():
        tri1 = int(input("Height = "))
        tri2 = int(input("Breadth = "))

        area = (tri1 * tri2) / 2
        print("Area of Triangle:", area)

        tri3 = int(input("Height1 = "))
        tri4 = int(input("Height2 = "))
        tri5 = int(input("Breadth = "))

        perimeter = tri3 + tri4 + tri5
        print("Perimeter of Triangle:", perimeter)