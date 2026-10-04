def print_reverse(s):
    if len(s) == 0:
        return
    print(s[-1], end="")
    print_reverse(s[:-1])

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

def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

def climbStairs(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
    return memo[n]

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

if __name__ == "__main__":
    print("Task 1:")
    print_reverse("tiger")
    print("\n")

    print("Task 2:")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    new_head = swapPairs(head)
    res = []
    curr = new_head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print(res)

    print("Task 3:")
    print("F(4) =", fib(4))

    print("Task 4:")
    print("Climb 3 =", climbStairs(3))

    print("Task 5:")
    print("2^10 =", myPow(2.0, 10))
    print("2^-2 =", myPow(2.0, -2))
