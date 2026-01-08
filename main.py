```python
def factorial(n):
      if n == 0:
                return 1
else:
        return n * factorial(n-1)

# 列表生成式创建斐波那契数列
fibonacci = [0, 1]
for i in range(2, 10):
      fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

# 使用zip函数组合姓名和年龄
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))

# 使用字典推导式计算数字的平方
squares = {x: x**2 for x in range(1, 6)}

# 使用生成器表达式计算100以内的素数
primes = (x for x in range(2, 100) if all(x % y != 0 for y in range(2, int(x**0.5) + 1)))

# 使用filter函数过滤出大于10的偶数
numbers = range(1, 20)
filtered = filter(lambda x: x > 10 and x % 2 == 0, numbers)

# 使用map函数将字符串转换为小写
strings = ["HELLO", "WORLD", "PYTHON"]
lowercase = map(str.lower, strings)

# 使用reduce函数计算列表中所有数字的和
from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

# 使用lambda函数定义一个简单的计算器
calculator = lambda x, y: x + y if y == 1 else x * y

# 使用递归函数计算阶乘
def recursive_factorial(n):
      return 1 if n == 0 else n * recursive_factorial(n-1)

# 使用装饰器打印函数执行时间
import time
def timer(func):
      def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
                return result
            return wrapper

@timer
def example_function():
      pass

# 使用多线程计算斐波那契数列
import threading

def fibonacci_thread(n):
      if n == 0:
                return 0
elif n == 1:
        return 1
else:
        return fibonacci_thread(n-1) + fibonacci_thread(n-2)

# 创建线程
thread = threading.Thread(target=fibonacci_thread, args=(10,))
thread.start()
thread.join()
```
