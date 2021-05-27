import random
import sys

sys_arg = sys.argv[1:]

rearranged_lst = []
for word in sys_arg:
    rearranged_lst.insert(random.randint(0,len(sys_arg)-1), word)
print(' '.join(rearranged_lst))
