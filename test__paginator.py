from paginator import (
    generate_around,
    generate_boundaries,
    generate_pagination,
    pagination_to_string,
)


def test_generate_pagination():
    # Case there is boundaries
    assert pagination_to_string([1, 4, 5], 1) == "1 ... 4 5"
    # Case where all numbers follow each other
    assert pagination_to_string([1, 2, 3, 4, 5], 1) == "1 2 3 4 5"
    # Case where there are 2 breaks in number sequence
    assert pagination_to_string([1, 5, 8, 9, 10], 1) == "1 ... 5 ... 8 9 10"
    # Case where there is no boundaries and one break in number sequence
    assert pagination_to_string([5, 8, 9], 0) == "... 5 ... 8 9 ..."
    # Case where there is no boundaries and one break in number sequence
    assert pagination_to_string([5, 6, 7, 8, 9], 0) == "... 5 6 7 8 9 ..."


def test_generate_boundaries():
    # Case where n of boundaries is 0
    assert generate_boundaries(5, 0) == []
    # Case where n of boundaries is less than total pages
    assert generate_boundaries(5, 1) == [1, 5]
    # Case where n of boundaries is equal to total pages
    assert generate_boundaries(5, 5) == [1, 2, 3, 4, 5]
    # Case wheere n of boundaries is greater than total pages
    assert generate_boundaries(5, 20) == [1, 2, 3, 4, 5]


def test_generate_around():
    # Case where around is 0
    assert generate_around(1, 0, 5) == [1]
    # Case where around is less than total pages
    assert generate_around(1, 1, 5) == [1, 2]
    # Case where around is less than total pages
    assert generate_around(1, 3, 5) == [1, 2, 3, 4]
    # Case where around is equal to total pages
    assert generate_around(3, 2, 5) == [1, 2, 3, 4, 5]
    # Case where around is greater than total pages
    assert generate_around(5, 10, 5) == [1, 2, 3, 4, 5]


def test_generate_pagination():
    # Case where everything is 0
    assert generate_pagination(0, 0, 0, 0) == []
    # Case where everything is 1
    assert generate_pagination(1, 1, 1, 1) == [1]
    # Case where where there is no boundaries and no around
    assert generate_pagination(1, 5, 0, 0) == [1]
    # Case where where there is 1 boundary and 2 arounds
    assert generate_pagination(1, 5, 1, 2) == [1, 2, 3, 5]
    # Case where where arounds and boundaries are bigger than total_pages
    assert generate_pagination(1, 5, 10, 10) == [1, 2, 3, 4, 5]
