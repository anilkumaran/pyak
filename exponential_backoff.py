import time
from requests.exceptions import ConnectionError

# The below code will try to call the remote_api_call(). If we get ConnectionError, it'll wait for 3 seconds and tries again. 
# If it fails, it'll wait for 5 seconds this time and tries again, and so on... until it tried all the intervals. Fails on the 5th iteration.
retry_intervals = [3, 5, 15, 30, 0]
for interval in retry_intervals:
    try:
        response = remote_api_call()
        break
    except ConnectionError as e:
        if interval == 0:
            raise e
        else:
            print(f'Retrying in {interval} seconds')
    time.sleep(interval)
