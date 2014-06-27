limit = 1000

set_ = set()

i = 0

while ((i*3)<limit):
    set_.add(i*3)
    i += 1

i= 0
while ((i*5)<limit):
    set_.add(i*5)
    i += 1

print (set_)

sum_ = 0
for i in set_:
    sum_ += i


print(sum_)
