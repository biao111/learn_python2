from  multiprocessing import  Queue

q =  Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.qsize())