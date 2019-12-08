''' li=['h','i',' ','h','e','y']
print(''.join(li)) 

st=input().split()
#print(''.join(st))
for word in st:
    print(''.join(word)) ''' 


st='fruit'
''' for ch in st:
    print(st) 

my_iter=iter(st)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) 
print(next(my_iter)) 

# example with tuple/list

fruits=('apple','banana','pine apple','orange')

for fruit in fruits:
    print(fruits) 
fr_iter=iter(fruits)

print(next(fr_iter))
print(next(fr_iter)) # here I retrieved only 2 fruits 


class return_nums:
    def __iter__(self):
        # self.a=1
        self.a=int(input()) # we can give dynamical inputs also
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x

numbers=return_nums()
my_iter=iter(numbers)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# upto your limit '''

#StopIteration

class upto_num:
    def __iter__(self):
        self.a=int(input("first number:"))
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration


numbers=upto_num()
for num in numbers:
    print(num,end=" ")




