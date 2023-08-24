from coin_change import Solution

def test_coinChange():
    sol = Solution()

    # Test cases with a passing result
    coins = [1, 2, 5]
    amount = 11
    assert sol.coinChange(coins, amount) == 3  # 11 = 5 + 5 + 1

    coins = [2]
    amount = 3
    assert sol.coinChange(coins, amount) == -1  # Not possible to make 3 with only a coin of 2

    coins = [1, 3, 4]
    amount = 6
    assert sol.coinChange(coins, amount) == 2  # 6 = 3 + 3

    # Test cases with a failing result
    coins = [2, 5, 10]
    amount = 3
    assert sol.coinChange(coins, amount) == -1  # Not possible to make 3 with these coins

    coins = []
    amount = 5
    assert sol.coinChange(coins, amount) == -1  # No coins available

    coins = [1, 3, 4]
    amount = 7
    assert sol.coinChange(coins, amount) == 2  # Fails, correct answer is 2 (4 + 3), not 3 (4 + 3 + 1)

    print("All test cases passed!")

test_coinChange()
