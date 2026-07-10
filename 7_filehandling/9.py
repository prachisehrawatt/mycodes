from contextlib import contextmanager
import time

@contextmanager
def prog_timer():
    start_time = time.time() 
    
    try:
        yield     
                  
    finally:
        process_time = time.time() - start_time
        start_time = process_time
        print(f"Time taken to execute : {process_time} seconds.")

#main()

with prog_timer():
    obj = sum(range(5000000))