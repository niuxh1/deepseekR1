import time
import random


def api_call(question):
    n= random.randint(10, 20)
    for i in range(n):
        j = i % 4
        print("\r思考中"+j*".", end='', flush=True)
        time.sleep(1)
    print("\n服务器繁忙，请稍后再试")

if __name__ == "__main__":
    while(true){
    question = input("请输入问题：")
    api_call(question)
    }
