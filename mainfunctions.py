import numpy as np
from copy import deepcopy
def two_dee(x):
    for i in range(len(x)):
        x[i]=list(x[i])
    return x
arr=tobe=["A'B'C'D'", "A'B'C'D", "AB'C'D", "AB'CD", "ABC'D", 'ABCD']

def join_with_apos(x):
    joined=[]
    for i in x:
        temp=[]
        for j in range(len(i)):
            if i[j]=="'":
                temp.append(i[j-1]+i[j])
            elif (j==len(i)-1) and (i[j]!="'"): temp.append(i[j])
            else:
                if j != len(i)-1:
                   if i[j + 1] != "'":temp.append(i[j])
        joined.append(temp)

    return joined

def difference(x,y):
        arr=[x,y]
        temp=join_with_apos(arr)
        diff=list(np.setdiff1d(temp[0],temp[1]))+list(np.setdiff1d(temp[1],temp[0]))
        if len(diff)!=1 and (diff[0][0] not in diff[1]) or (len(temp[0])!=len(temp[1])):
                return 0
        else:
            return 1

def truth_table(n):
    x=[[0],[1]]
    for i in range(n-1):
        for i in x:
            i.insert(0,0)
        table_of_zer0=deepcopy(x)
        for i in x:
            del i[0]
        for i in x:
            i.insert(0,1)
        table_of_ones=x
        table_of_zer0.extend(table_of_ones)
        x=table_of_zer0
    return x

def maxx(n):
    x=2**n-1
    return x

def equation(x):
    minterm=[]
    for l in x:
        lst=[]
        z=96
        for j in range(len(l)-1):
            z+=1
            if l[-1]==1:
                for k in range(z,123):
                    letter=chr(k).capitalize()
                    if l[j]==1:
                        lst.append(letter)
                    elif l[j]==0:
                        lst.append(letter+"'")
                    break
            elif l[-1]==0:
                break
        if l[-1]==1:
            string=''.join(lst)
            minterm.append((string))
        # result='+'.join(minterm)
    return(minterm)

def minterm(x,lst1):
    for i in range(len(x)):
        for j in lst1:
            if i==int(j):
                x[i].append(1)
                break
        if i!=int(j):
            x[i].append(0)
    return x

def get_common(arr,common):
    comm=[]
    for i in arr:
        temp=[]
        for j in range(len(i)):
            if i[j] not in common:
                temp.append(i[j])
        comm.append(temp)
    return comm

def dashed_simplification(arr):
    changed=False
    try:
        if len(arr[0])==1:
            if len(arr[0][0]) ==1:
                compare=arr[0][0]
            else:compare=arr[0][0][0]
            for i in arr[1]:
                if i[0]==compare:
                    arr[1].remove(i)
                    changed=True
        elif len(arr[1])==1:
            if len(arr[1][0]) ==1:
                compare=arr[1][0]
            else:compare=arr[1][0][0]
            for i in arr[0]:
                if i[0]==compare:
                    arr[0].remove(i)
                    changed=True
        else:
            arr=[]
            changed=False
        return arr,changed
    except: return [],False

def sort_it(arr):
    for i in range(len(arr)):
        if i != len(arr)-1:
            for j in range(i+1,len(arr)):
                if arr[i][0]>arr[j][0]:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
    return arr






