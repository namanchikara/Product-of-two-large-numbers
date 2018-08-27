def GetMeTheProduct(n,m):

    n = str(n)
    m = str(m)
    i = len(n)            # length of n and m
    j = len(m)
    l = m                 # l represents larger number, s represents smaller number
    s = n                 # assuming that 2nd number is larger i.e larger = m, and smaller = n
    
    if i>j:               # if our assumption of 2nd number being larger is wrong, i.e 1st number is larger
        l,s = n,m         # then we make l = n and s = m
    else:                 # if our assumption is right then, value of i and j should be interchanged because
         i,j = j,i        # value of i should always contain length of larger number, and value of j should contain value of smaller number
    
    ans = [0 for x in range(i+2+j)]      # product of any 2 number can contain at most sum of length of both the numbers
 
    
    del n,m               # n and m are no longer required as we have s and l now.
    
    i -=1                 # value of i and j is subtracted by 1 because of zero base index
    j -=1
    k = 0  
 
    ############################################################################################################               
    # k is a variable whose value will increase by 1 so that product will be shifted towards right in each step, 
    # for e.g 121 * 121 , 
    # we will have 121 for 121*1
    #             242X for 121*2 
    #            121XX for 121*1
    # sum =      14652, so we notice that x is going from left to right, k plays the role of x.
    ############################################################################################################
    
    while True:
        bk = i                                    # we take backup of i
        bjk = len(l) + len(s) + 1                 # bjk is index used to access our ans array(list)
        while True:
            prod = int(l[bk]) * int(s[j])
            if len(str(prod)) == 1:               #if no carry is generated then just add the current product to it's corresponding index
                ans[bjk-k] += prod 
            
            else:
                temp = str(prod)                  
                temp_int0 = int(temp[0])          # temp_int0 stores value of carry
                temp_int1 = int(temp[1])          # temp_int1 stores value of significant number
                
                ans[bjk-k-1] += temp_int0
                ans[bjk-k]   += temp_int1
                
            loop = bjk                            # if more than 9 i.e 10 and above value is stored at any index of ans, we move the tens digit number to left and one's digit number stays there.
                
            while loop != 0:
           
                if len(str(ans[loop])) == 2:
                    temp = str(ans[loop])
                    ans[loop-1] += int(temp[0])
                    ans[loop]    = int(temp[1])
                        
                loop -= 1
                    
                
            bk -= 1
            bjk -= 1
            
            if bk < 0:
                break
        
        
        k+=1
        j-=1
        if j < 0:
            break
    
    
    # in c or c++ we won't be able to do this next step because, our long long integer variable won't be able to hold such large values
    # so instead of doing this next step we'll just return the array, of pointer to the array (in case of large space.)
    
    num = 0                                      
    factor = 1
    for i in range(len(ans)-1,-1,-1):            # ans is in form of list, so we convert it into integer.
        num += (ans[i]*factor)
        factor *= 10
    
    return num
    
    
def main():
    first_number = int(input())
    second_number = int(input())
    
    ans = GetMeTheProduct(first_number, second_number)
    print(ans)
    
main()
