import pytest
from main import kth_missing_positive_number


def test_kmpn_returns_missing_number():
    arr = [2, 3, 4, 7, 11]
    k = 5
    arr2 = [1, 2, 3, 4]
    k2 = 2

    assert kth_missing_positive_number(arr, k) == 9
    assert kth_missing_positive_number(arr2, k2) == 6


def test_kmpn_missing_at_start():
    arr = [5, 6, 7]
    k = 1

    assert kth_missing_positive_number(arr, k) == 1


def test_kmpn_k_out_of_list_range():
    arr = [2, 3, 4, 7, 11]
    k = 10
    arr2 = [2, 3, 4, 7, 11]
    k2 = 30

    assert kth_missing_positive_number(arr, k) == 15
    assert kth_missing_positive_number(arr2, k2) == 35


def test_kmpn_empty_array_returns_k():
    arr = []
    k = 3

    assert kth_missing_positive_number(arr, k) == k


def test_kmpn_single_element_arr_returns_missing_number():
    arr = [2]
    k = 1
    arr2 = [6]
    k2 = 3

    assert kth_missing_positive_number(arr, k) == 1
    assert kth_missing_positive_number(arr2, k2) == 3


def test_kmpn_first_elem_zero_returns_missing_number():
    arr = [0]
    k = 3
    arr2 = [2, 3, 4, 7, 11]
    k2 = 30
    # arr2 = [0, 1, 4]
    # k2 = 2

    assert kth_missing_positive_number(arr, k) == 3
    assert kth_missing_positive_number(arr2, k2) == 35
