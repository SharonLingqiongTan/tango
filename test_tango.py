from tango import TangoTree

def test(sequence):
    for v in sequence:
        tango.access(v)

print "== First test tango, 1000 nodes =="
# initialization
nodes = []
for i in range(1, 1001):
    nodes += i,
tango = TangoTree(nodes)
#test access sequence
sequence1 = [1]
print ("> First test sequence " + str(sequence1))
test(sequence1)

sequence2 = [3,2,4,5,7,8,10,12,13,999]
print ("> Second test sequence " + str(sequence2))
test(sequence2)



# sequence3 = [50, 120, 3, 78, 66, 8]
# print ("> First test sequence " + str(sequence3))
# test(sequence3)



sequence4 = [999, 998, 997]
print ("> Forth test sequence " + str(sequence4))
test(sequence4)



print "== Second test tango, 10 nodes =="
# initialization
nodes = []
for i in range(10):
    nodes += i,
tango = TangoTree(nodes)
#test access sequence
sequence1 = [0]
print ("> First test sequence " + str(sequence1))
test(sequence1)

sequence2 = [1,2,3]
print ("> Second test sequence " + str(sequence2))
test(sequence2)

sequence3 = [3,2,1]
print ("> Third test sequence " + str(sequence3))
test(sequence3)

# sequence4 = [9, 8, 7]
# print ("> First test sequence " + str(sequence4))
# test(sequence4)









