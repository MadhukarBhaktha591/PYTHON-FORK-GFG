#06.GarbageCollection.py
import gc
b = 9
b = 4

def create_cycle():
    x = []
    x.append(x)
create_cycle

x = []
x.append(1)
x.append(2)

del x
# x = None


print('Garbage collection thresholds:',
      gc.get_threshold())

collected = gc.collect()
print("Garbage collector: collected",
      "%d objects." %collected)

i = 0
def create_cycle():
    x = {}
    x[i+1] = x
    print(x)

collected = gc.collect()
print("Garbage collector: collected %d objects." %(collected))
print("Creating cycles...")
for i in range(10):
    create_cycle()
collected = gc.collect()
print("Garbage collector: collected %d objects." %(collected))
