while True:
    try:
        c, h, w, capacity = map(int, input().split(" "))

        if capacity > h:
            print("YES")
        elif capacity > w + c:
            print("YES")
        elif capacity == h:
            if capacity >= c and capacity >= w:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    except:
        break