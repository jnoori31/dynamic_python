from climb_stairs import climbStairs

def test_climbStairs():
    # Passing cases
    assert climbStairs(1) == 1
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(4) == 5
    assert climbStairs(5) == 8
    assert climbStairs(6) == 13
    assert climbStairs(10) == 89
    assert climbStairs(0) == 1
    assert climbStairs(45) == 1836311903

    # Failing case
    assert climbStairs(5) != 10  # This assertion will fail
    
    print("All tests passed!")

# Run the unit tests
test_climbStairs()
