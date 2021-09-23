# ThreadPoolExecutor
import time
from concurrent.futures.thread import ThreadPoolExecutor


def hoge(i):
    time.sleep(1)
    return i


start = time.time()

# 普通の処理
# for i in range(5):
#     hoge(i)

# 並列処理
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(hoge, i) for i in range(5)]

print(futures)

for v in futures:
    print(v.result())

elapsed_time = time.time() - start

print(elapsed_time)
