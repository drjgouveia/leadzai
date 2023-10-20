from paginator import (
    generate_around,
    generate_boundaries,
    generate_pagination,
    pagination_to_string,
)


def test_generate_boundaries__001():
    # Case where n of boundaries is 0
    total_pages = 5
    boundaries = 0
    assert generate_boundaries(total_pages, boundaries) == []


def test_generate_boundaries__002():
    # Case where n of boundaries is less than total pages
    total_pages = 5
    boundaries = 1
    assert generate_boundaries(total_pages, boundaries) == [1, 5]


def test_generate_boundaries__003():
    # Case where n of boundaries is equal to total pages
    total_pages = 5
    boundaries = 5
    assert generate_boundaries(total_pages, boundaries) == [1, 2, 3, 4, 5]


def test_generate_boundaries__004():
    # Case wheere n of boundaries is greater than total pages
    total_pages = 5
    boundaries = 20
    assert generate_boundaries(total_pages, boundaries) == [1, 2, 3, 4, 5]


def test_generate_around__001():
    # Case where around is 0
    current_page = 1
    around = 0
    total_pages = 5
    assert generate_around(current_page, around, total_pages) == [1]


def test_generate_around__002():
    # Case where around is less than total pages
    current_page = 1
    around = 1
    total_pages = 5
    assert generate_around(current_page, around, total_pages) == [1, 2]


def test_generate_around__003():
    # Case where around is less than total pages
    current_page = 1
    around = 3
    total_pages = 5
    assert generate_around(current_page, around, total_pages) == [1, 2, 3, 4]


def test_generate_around__004():
    # Case where around is equal to total pages
    current_page = 1
    around = 5
    total_pages = 5
    assert generate_around(current_page, around, total_pages) == [1, 2, 3, 4, 5]


def test_generate_around__005():
    # Case where around is greater than total pages
    current_page = 1
    around = 20
    total_pages = 5
    assert generate_around(current_page, around, total_pages) == [1, 2, 3, 4, 5]


def test_generate_around__006():
    # Case where around is lower than 0
    current_page = 1
    around = -2
    total_pages = 5
    assert generate_around(current_page, around, total_pages) == [1]


def test_generate_pagination__001():
    # Case where everything is 0
    assert generate_pagination(0, 0, 0, 0) == []


def test_generate_pagination__002():
    # Case where everything is 1
    assert generate_pagination(1, 1, 1, 1) == [1]


def test_generate_pagination__003():
    # Case where where there is no boundaries and no around
    current_page = 1
    total_pages = 5
    boundaries = 0
    around = 0
    assert generate_pagination(current_page, total_pages, boundaries, around) == [1]


def test_generate_pagination__004():
    # Case where where there is 1 boundary and 2 arounds
    current_page = 1
    total_pages = 5
    boundaries = 1
    around = 2
    assert generate_pagination(current_page, total_pages, boundaries, around) == [
        1,
        2,
        3,
        5,
    ]


def test_generate_pagination__005():
    # Case where where arounds and boundaries are bigger than total_pages
    current_page = 1
    total_pages = 5
    boundaries = 10
    around = 10
    assert generate_pagination(current_page, total_pages, boundaries, around) == [
        1,
        2,
        3,
        4,
        5,
    ]


def test_pagination_to_string__001():
    # Case there is boundaries
    current_page = 4
    total_pages = 5
    boundaries = 1
    around = 0
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == "1 ... 4 5"
    )


def test_pagination_to_string__002():
    # Case the current_page is bigger than the total_pages
    current_page = 7
    total_pages = 5
    boundaries = 0
    around = 0
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == f"... {total_pages}"
    )


def test_pagination_to_string__003():
    # Case the current_page is negative
    current_page = -3
    total_pages = 5
    boundaries = 1
    around = 1
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == f"1 2 ... {total_pages}"
    )


def test_pagination_to_string__004():
    # Case the around is negative
    current_page = 2
    total_pages = 5
    boundaries = 1
    around = -1
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == f"1 {current_page} ... {total_pages}"
    )


def test_pagination_to_string__005():
    # Case the boundaries is negative
    current_page = 4
    total_pages = 10
    boundaries = -1
    around = 1
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == f"... {current_page - 1} {current_page} {current_page + 1} ..."
    )


def test_pagination_to_string__006():
    # Case everything is 0
    current_page = 0
    total_pages = 0
    boundaries = 0
    around = 0
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == ""
    )


def test_pagination_to_string__007():
    # Case everything is 1
    current_page = 1
    total_pages = 1
    boundaries = 1
    around = 1
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == "1"
    )
