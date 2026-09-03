import pytest

from src.prestandatest.insertion_sort.insertion_sort import insertion_sort
from src.prestandatest.merge_sort.merge_sort import merge_sort


@pytest.mark.unit
def test_insertion_sort():
    list1 = []
    list2 = [10]
    list3 = [10, 8, 6, 4, 2, 0]

    insertion_sort(list1)
    insertion_sort(list2)
    insertion_sort(list3)

    assert list1 == []
    assert list2 == [10]
    assert list3 == [10, 8, 6, 4, 2, 0]






