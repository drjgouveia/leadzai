def generate_boundaries(total_pages: int, boundaries: int) -> list:
    """
    Generate a list of numbers that will be used as boundaries
    :param total_pages: total number of pages
    :param boundaries: size of the boundaries
    :return: list of number boundaries
    """
    numbers = []
    for i in range(boundaries):
        if i + 1 <= total_pages:
            numbers.append(i + 1)

        if total_pages - i > 0:
            numbers.append(total_pages - i)

    return sorted(set(numbers))


def generate_around(current_page: int, around: int, total_pages: int) -> list:
    """
    Generate a list of numbers that will be used as around
    :param current_page: current page
    :param around: size of the around
    :param total_pages: total number of pages
    """
    numbers = []
    if current_page > 0:
        numbers = [current_page]

    for i in range(around):
        if current_page - (i + 1) > 0:
            numbers.append(current_page - (i + 1))

        if current_page + (i + 1) <= total_pages:
            numbers.append(current_page + (i + 1))

    return sorted(set(numbers))


def generate_pagination(
    current_page: int, total_pages: int, boundaries: int, around: int
) -> list:
    """
    Generate a list of numbers that will be used as pagination
    """
    numbers = generate_boundaries(total_pages, boundaries)
    numbers += generate_around(current_page, around, total_pages)
    numbers = sorted(set(numbers))

    return numbers


def pagination_to_string(pagination: int, boundaries: int) -> str:
    string = ""
    prev = 0
    for i, p in enumerate(pagination):
        if (p - prev) > 1 and i < len(pagination):
            string += "... "
        prev = p
        string += str(p) + " "
        if boundaries == 0 and i == len(pagination) - 1:
            string += "..."

    return string.strip()
