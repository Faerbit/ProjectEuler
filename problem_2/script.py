limit = 4 * pow(10, 6)

last = 1
before = 0

list_ = []

while (last+before < limit):
    current = last + before
    if (current % 2 == 0):
        print (current)
        list_.append(current)
    before = last
    last = current

print("Summe: " + str(sum(list_)))
