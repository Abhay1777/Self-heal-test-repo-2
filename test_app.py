from app import multiply

def test_multiply():
     # Expected: multiply(6, 7) should return 42.
    # This test will fail because the current implementation uses '+'.
    assert multiply(6, 7) == 42
