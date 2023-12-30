a = float(input("nhập giá trị a"))
b = float(input("nhập giá trị b"))
c = float(input("nhập giá trị c"))
d = float(input("nhập giá trị d"))
if a>max:
    max=a
    if a<min:
        min=a
        if b>max:
            max=b
            if b<min:
             min=b
            if c>max:
                max=c
                if c<min:
                    min=c
                    if d>max:
                        max=d
                        if d<min:
                            min=d
                            print("giá trị lớn nhất:",max)
                            print("giá trị nhỏ nhất:",min)
