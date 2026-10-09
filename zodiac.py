T = int(input())
for _ in range (T):
    d, m = input().split()
    d = int(d)
    if m == "Jan":
        if d <= 19:
            print("Capricorn")
        else:
            print("Aquarius")
    elif m == "Feb":
        if d <= 19:
            print("Aquarius")
        else:
            print("Pisces")
    elif m == "Mar":
        if d <= 20:
            print("Pisces")
        else:
            print("Aries")
    elif m == "Apr":
        if d <= 20:
            print("Aries")
        else:
            print("Taurus")
    elif m == "May":
        if d <= 20:
            print("Taurus")
        else:
            print("Gemini")
    elif m == "Jun":
        if d <= 20:
            print("Gemini")
        else:
            print("Cancer")
    elif m == "Jul":
        if d <= 22:
            print("Cancer")
        else:
            print("Leo")
    elif m == "Aug":
        if d <= 22:
            print("Leo")
        else:
            print("Virgo")
    elif m == "Sep":
        if d <= 22:
            print("Virgo")
        else:
            print("Libra")
    elif m == "Oct":
        if d <= 22:
            print("Libra")
        else:
            print("Scorpio")
    elif m == "Nov":
        if d <= 22:
            print("Scorpio")
        else:
            print("Sagittarius")
    elif m == "Dec":
        if d <= 21:
            print("Sagittarius")
        else:
            print("Capricorn")
