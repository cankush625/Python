print("Most frequent occuring element in the array")
def most_frequent(given_array=[1,3,2,1,3,1]) :
    max_count = -1
    max_item = 0
    count = {}
    for item in given_array :
        if item not in count :
            count[item] = 1
        else :
            count[item] += 1
        if count[item] > max_count :
            max_count = count[item]
            max_item = item
    print("Max value is ",max_item)
    return max_item

'''By Ankush Chavan'''