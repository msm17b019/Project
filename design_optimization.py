import numpy as np      #import numpy to generate a numpy array

def gen_matrix(var,cons):    
    '''
    This function create a table.
    '''
    tab = np.zeros((cons+1, var+cons+2))    
    return tab

def next_round_r(table):   
    '''
    This function checks whether minimum element in the last column is +ve or -ve.
    ''' 
    m = min(table[:-1,-1])
    if m>= 0:        
        return False    
    else:        
        return True

def next_round(table):   
    '''
    This function checks whether minimum element in the last row is +ve or -ve.
    ''' 
    l_row = len(table[:,0])   
    m = min(table[l_row-1,:-1]) 

    if m>=0:
        return False
    else:
        return True

def find_neg_r(table):
    '''
    This function find the index of negative element in the last column.
    '''
    l_col = len(table[0,:])
    m = min(table[:-1,l_col-1]) 
    if m<=0:        
        n = np.where(table[:-1,l_col-1] == m)[0][0] # returns the index of element
    else:
        n = None
    return n

def find_neg(table):
    '''
    This function find the index of negative element in the last row.
    '''
    l_row = len(table[:,0])
    m = min(table[l_row-1,:-1])
    if m<=0:
        n = np.where(table[l_row-1,:-1] == m)[0][0]
    else:
        n = None
    return n

def loc_piv_r(table):
    '''
    This function find the pivot element corresponding to a negative element in the last column.
    '''
    total = []        
    r = find_neg_r(table)
    row = table[r,:-1]
    m = min(row)
    c = np.where(row == m)[0][0]  # returns the index of element
    col = table[:-1,c]
    for i, b in zip(col,table[:-1,-1]):
        if i**2>0 and b/i>0:
            total.append(b/i)
        else:                
            total.append(10000)
    index = total.index(min(total))        
    return [index,c]

def loc_piv(table):
    '''
    This function find the pivot element corresponding to a negative element in the last row.
    '''
    if next_round(table):
        total = []
        n = find_neg(table)
        for i,b in zip(table[:-1,n],table[:-1,-1]):
            if b/i >0 and i**2>0:
                total.append(b/i)
            else:
                total.append(10000)
        index = total.index(min(total))
        return [index,n]

def pivot(row,col,table):
    '''
    This function remove the negative element in the final row or column.

    And return the updated table.
    '''
    l_row = len(table[:,0])
    l_col = len(table[0,:])
    t = np.zeros((l_row,l_col))     # creating new table of same dimension
    pr = table[row,:]               # row that contain pivot element
    if table[row,col]**2>0:
        e = 1/table[row,col]
        r = pr*e                    # pivot row elements * inverse of pivot element 
        for i in range(len(table[:,col])):  
            k = table[i,:]
            c = table[i,col]
            if list(k) == list(pr):
                continue
            else:
                t[i,:] = list(k-r*c)     # updating the row
        t[row,:] = list(r)
        return t
    else:
        print('Cannot pivot on this element.')

def convert(eq):
    '''
    This function takes the value from equation and put it in a list.
    '''
    eq = eq.split(',')
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i)*-1 for i in eq]  # multiply by -1 to change >= to <=
        return eq
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq

def convert_min(table):
    '''
    This function converts the minimization problem to maximization problem.

    '''
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]    
    return table

def gen_var(table):
    '''
    This function generate the required number of variables.
    '''
    l_col = len(table[0,:])
    l_row = len(table[:,0])
    var = l_col - l_row -1
    v = []
    for i in range(var):
        v.append('x'+str(i+1))
    return v

def add_cons(table):
    '''
    This function checks whether row is empty or not for adding constraint.
    '''
    l_row = len(table[:,0])    # number of rows in table
    empty = []
    for i in range(l_row):     # check whether row is empty or not
        total = 0
        for j in table[i,:]:                       
            total += j**2
        if total == 0: 
            empty.append(total)
    if len(empty)>1:
        return True
    else:
        return False

def constrain(table,eq):
    '''
    This function add constraint equation in table.
    '''
    if add_cons(table) == True:
        l_row = len(table[:,0])   # no of rows in table
        l_col = len(table[0,:])   # no of columns in table
    
        var = l_col - l_row -1      
        j = 0
        while j < l_row:      # for getting the value of j      
            row_check = table[j,:]
            total = 0
            for i in row_check:
                total += float(i**2)
            if total == 0:                
                row = row_check
                break
            j +=1
        eq = convert(eq)
        i = 0
        while i<len(eq)-1:
            row[i] = eq[i]  #add variable coefficient in row
            i +=1        
        row[-1] = eq[-1]   #add RHS of equation in last column of the row
        row[var+j] = 1   #add 1 in table for slack variable 
    else:
        print('Can\'t add another constraint.')

def add_obj(table):
    '''
    This function will check whether all constraints are added or not.

    If all constraints are added, then only it will allow
    objective equation to be added in table.
    '''
    l_row = len(table[:,0])
    empty = []
    for i in range(l_row):
        total = 0        
        for j in table[i,:]:
            total += j**2
        if total == 0:
            empty.append(total)    
    if len(empty)==1:
        return True
    else:
        return False

def obj(table,eq):
    '''
    This function add objective equation values in table.
    '''
    if add_obj(table)==True:
        eq = [float(i) for i in eq.split(',')]
        l_row = len(table[:,0])
        row = table[l_row-1,:]  # last row 
        i = 0        
        while i<len(eq)-1:
            row[i] = eq[i]*(-1)  # p=x1 + x2 to -x1-x2+p=0
            i +=1
        row[-2] = 1 
        row[-1] = eq[-1] # RHS of objective equation

    else:
        print('First add all the constraints.')

def maxz(table):
    '''
    This function returns the variable values the maximum of objective equation.
    '''
    while next_round_r(table)==True:  # it will run till next_round_r function return True
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)  # row, column and table --> arguments of pivot
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)        
    l_col = len(table[0,:])
    l_row = len(table[:,0])
    var = l_col - l_row -1            # number of variables
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]        
            val[gen_var(table)[i]] = table[loc,-1]    # final value of variable
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = "{:.2f}".format(table[-1,-1])   # max value of objective equation
    return val

def minz(table):
    '''
    This function returns the variable values the minimum of objective equation.
    '''
    table = convert_min(table)
    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)    
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)       
    l_col = len(table[0,:])
    l_row = len(table[:,0])
    var = l_col - l_row -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]             
            val[gen_var(table)[i]] = table[loc,-1]

        else:
            val[gen_var(table)[i]] = 0 
    val['min'] = "{:.2f}".format(table[-1,-1]*-1)

            
    return val

if __name__ == "__main__":
    m = gen_matrix(2,2)
    constrain(m,'2,-1,G,10')   #arguments are table and equation
    constrain(m,'1,1,L,20')
    obj(m,'5,10,0')     
    print(maxz(m))     
    m = gen_matrix(2,4)
    constrain(m,'2,5,G,30')
    constrain(m,'-3,5,G,5')
    constrain(m,'8,3,L,85')
    constrain(m,'-9,7,L,42')
    obj(m,'2,7,0')
    print(minz(m))