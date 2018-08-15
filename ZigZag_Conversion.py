
# coding: utf-8

# In[2]:


def convert(s,numRows):
    if (numRows==1):return s
    a=[[]for i in range(numRows)]#产生一个有numRows单元的list，每个list可以往后面添加元素
    r=0
    direct=1
    for i in s:
        a[r].append(i)
        if r>=numRows-1:
            direct=-1
        elif r==0:
            direct=1
        r+=direct
    answer=''
    for row in a:
        for col in row:
            answer+=col
    return answer
if __name__=='__main__':
    print(convert('PAYPALISHIRING',4))

