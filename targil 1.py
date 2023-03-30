##שאלה 1 ##

def my_func (x1 , x2 , x3):
    if type(x1) == int or type(x2) == int or type(x3) == int :
        value = print('Error: parameters should be float')
    
    try:    
        if type(x1) != float or type(x2) != float or type(x3) != float : 
            value = None
            return value
        else:
            num = x1 + x2 + x3
    except:
        value = None 
        return value    
        
    if num == 0:       
        value = print('Not a number – denominator equals zero')
    else:        
        sum1 = num*(x2+x3)*x3
        value = sum1/num
        return value
      
## שאלה 2##

def revword (word:str) ->str:
    return word[::-1]    
    
def countword () -> int:
    file = open("C:\\Users\\User\\Desktop\\שנה ג - סמסטר ב\\כרייה וניתוח\\data\\text.txt")
    lis_rows = list()
    for row in file:
        row = row.lower().split()
        for word in row:
            lis_rows.append(word)
    word = lis_rows[0]
    text = []
    text.append(word)
    lis_rows=lis_rows[1:]
    count = 1
    for i in lis_rows:
        rev = revword(i)
        text.append(rev)
        if rev == word:
            count = count+1
    return count
print (countword())
