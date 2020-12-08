import os
import time

if __name__ == '__main__':
    # os.system('pwd')
    while True:
        os.system("scrapy crawl Train")
        print("start")
        # 每1２个小时执行一次　６０＊６０＊２

        time.sleep(60*60*12)