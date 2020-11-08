from concurrent.futures import ThreadPoolExecutor

def say_hello():
    print("Hello")
    
executor = ThreadPoolExecutor(20)
for i in range(0,10):
    executor.submit(say_hello())