# 1. Печать строки в обратном порядке
def print_reverse(s):
  if len(s) == 0:
    return
  print(s[-1], end="")
  print_reverse(s[:-1])


# 2. Обмен пар соседних узлов в связанном списке
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def swapPairs(head):
  if not head or not head.next:
    return head
  first = head
  second = head.next
  first.next = swapPairs(second.next)
  second.next = first
  return second


# 3. Числа Фибоначчі
def fib(n):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  return fib(n - 1) + fib(n - 2)


# 4. Подъем по лестнице (эквивалентно Фибоначчи)
def climbStairs(n, memo=None):
  if memo is None:
    memo = {}
  if n <= 2:
    return n
  if n in memo:
    return memo[n]
  memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
  return memo[n]


# 5. Возведение в степень pow(x, n) за O(log n)
def myPow(x, n):
  if n == 0:
    return 1.0
  if n < 0:
    return 1.0 / myPow(x, -n)
  if n % 2 == 0:
    half = myPow(x, n // 2)
    return half * half
  else:
    return x * myPow(x, n - 1)