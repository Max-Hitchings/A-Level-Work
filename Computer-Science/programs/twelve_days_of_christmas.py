giftList = ["partridge in a pear tree", "turtle doves", "french hens", "calling birds", "gold rings", "geese a laying",
            "swans a swimming", "maids a milking", "ladies dancing", "lords of leaping", "pipers piping",
            "drummers drumming"]
giftList.reverse()

for i in range(12):
    if i ==0:
        suffix = 'st'
    elif i == 1:
        suffix = 'nd'
    elif i == 2:
        suffix = 'rd'
    else:
        suffix = 'th'


    currGifts = giftList[12-(i+1):]
    if i == 1:
        giftList[-1] = 'and '+currGifts[-1]
    print(f"on the {i+1}{suffix} day of christmas my true love gave to me {i+1 if i != 0 else 'a'} {f', {i} '.join(currGifts)}")