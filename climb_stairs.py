"Dynamic programming 1: Easy"
link = "https://www.youtube.com/watch?v=Y0lT9Fck7qI"

def climbStairs(n):
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one

# Example usage
result = climbStairs(5)
print(result)
