import time

def start_worker():
    while True:
        print("Processing shipment events")
        time.sleep(5)

if __name__ == "__main__":
    start_worker()