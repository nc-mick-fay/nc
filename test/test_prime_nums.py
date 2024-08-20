from src.prime_nums import prime_nums

def test_returns_empty_list_if_num_lower_than_2():
    assert prime_nums(0) == []
    assert prime_nums(1) == []

def test_returns_2_when_num_2():
    assert prime_nums(2) == [2]


def test_returns_list_of_primes_for_nums_greater_than_2():
    assert prime_nums(3) == [2, 3]
    assert prime_nums(4) == [2, 3]
    assert prime_nums(5) == [2, 3, 5]
    assert prime_nums(10) == [2, 3, 5, 7]
    assert prime_nums(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                               31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
