biggie_list= [-1,3,5,-5]
def biggie_size (biggi_list):
    for i in range (0,len(biggie_list),1):
        if biggie_list[i] > 0:
            biggie_list[i] = "big"
    return biggie_list
print (biggie_size(biggie_size))

####################################################################################

positive_list= [-1,1,1,1]
def count_positive (positive_list):
    count = 0
    for i in range (0,len(positive_list),1):
        if positive_list[i] > 0:
           count +=1
    positive_list[len(positive_list)-1] = count
    return positive_list
print (count_positive(positive_list))

####################################################################################

def sumlist (sum_list):
    sum = 0
    for i in range(len(sum_list)):
        sum += sum_list[i]
    return sum
print(sumlist([1,2,3,4]))

 ####################################################################################   

def average (sum_list):
    sum = 0
    for i in range(len(sum_list)):
        sum += sum_list[i]
    return sum / len(sum_list)
print(average([1,2,3,4]))

####################################################################################

def length(num_list):
    if len(num_list) == 0:
        return False
    else:
        return len(num_list)
    
print(length([37,2,1,-9]))
print(length([]))

####################################################################################

def min(num_list):
    if len(num_list) == 0:
        return False
    else:
        min = num_list[0]
        for i in range(len(num_list)):
            if num_list[i] < min:
                min = num_list[i]
        return min
print(min([37,2,1,-9]))
print(min([]))

####################################################################################        


def max(num_list):
    if len(num_list) == 0:
        return False
    else:
        max = num_list[0]
        for i in range(len(num_list)):
            if num_list[i] > max:
                min = num_list[i]
        return max
print(max([37,2,1,-9]))
print(max([]))

####################################################################################Dictionary

def ultimate_analysis(num_list):
    analysis = {'sumlist' : sumlist (num_list),'average' : average (num_list),'minimum' : min(num_list),'maximum' : max(num_list),'length' : length(num_list)
    }
    return analysis
print(ultimate_analysis([37,2,1,-9]))

####################################################################################

def reverse_list(num_list):
    for i in range(int(len(num_list)/2)):
        temp = num_list[len(num_list)-1-i]
        num_list[len(num_list)-1-i] = num_list[i]
        num_list[i] = temp
    return num_list
print (reverse_list([37,2,1,-9]))
