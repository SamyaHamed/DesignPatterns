import time
from ftplib import print_line
def dec_time(base_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        base_func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(run_time)
        return run_time
    return wrapper

@dec_time
def make_tea(tea_type, prepare_time):
    print(f"Making {tea_type} tea ...")
    time.sleep(prepare_time)
    print ("Tea is redy ")

@dec_time
def make_matcha():
    print("Making matcha ...")
    time.sleep(1)
    print("Matcha is redy ")

make_tea(tea_type= "green", prepare_time= 1)
print("\n\n")
make_matcha()