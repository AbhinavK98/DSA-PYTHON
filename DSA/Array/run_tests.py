from pathlib import Path
import sys

base = Path(__file__).resolve().parent
sys.path.insert(0, str(base))

from two_sum import solution3_optimal as two_sum
from best_time_to_buy_and_sell_stock import solution3_optimal as max_profit
from maximum_subarray import solution3_optimal as max_subarray
from move_zeroes import solution3_optimal as move_zeroes
from product_except_self import solution3_optimal as product_except_self
from majority_element import solution3_optimal as majority_element
from missing_number import solution3_optimal as missing_number
from search_in_rotated_sorted_array import solution3_optimal as search
from container_with_most_water import solution3_optimal as max_area
from subarray_sum_equals_k import solution3_optimal as subarray_sum


def test_move_zeroes():
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    return arr


def main():
    tests = [
        (lambda: two_sum([2, 7, 11, 15], 9), (0, 1)),
        (lambda: two_sum([3, 2, 4], 6), (1, 2)),
        (lambda: max_profit([7, 1, 5, 3, 6, 4]), 5),
        (lambda: max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6),
        (test_move_zeroes, [1, 3, 12, 0, 0]),
        (lambda: product_except_self([1, 2, 3, 4]), [24, 12, 8, 6]),
        (lambda: majority_element([3, 2, 3]), 3),
        (lambda: missing_number([3, 0, 1]), 2),
        (lambda: search([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (lambda: max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49),
        (lambda: subarray_sum([1, 1, 1], 2), 2),
    ]

    for fn, expected in tests:
        result = fn()
        assert result == expected, f"expected {expected}, got {result}"

    print("run_tests: all tests passed")


if __name__ == "__main__":
    main()
