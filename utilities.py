from datetime import datetime


def timer(func):
    def inner():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        print(f"Total Time take: {end_time-start_time}")
        return 
    return inner