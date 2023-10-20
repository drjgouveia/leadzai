from paginator import generate_pagination, pagination_to_string


def test__001():
    # Case of page being in the beginning
    current_page = 1
    total_pages = 9
    boundaries = 1
    around = 1
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == "1 2 ... 9"
    )


def test__002():
    # Case of page being in the middle
    current_page = 4
    total_pages = 9
    boundaries = 1
    around = 1
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == "1 ... 3 4 5 ... 9"
    )


def test__003():
    # Case of page being in the end
    current_page = 9
    total_pages = 9
    boundaries = 2
    around = 1
    assert (
        pagination_to_string(
            generate_pagination(current_page, total_pages, boundaries, around),
            current_page,
            total_pages,
            boundaries,
        )
        == "1 2 ... 8 9"
    )
