from paginator import generate_pagination, pagination_to_string

if __name__ == "__main__":
    datakeys = ["current_page", "total_pages", "boundaries", "around"]
    data = {}
    for k in datakeys:
        while True:
            try:
                data[k] = int(input(f"{k} = "))
                if data[k] < 0:
                    raise Exception
                break
            except Exception:
                print("Invalid input")

    print(
        pagination_to_string(
            generate_pagination(**data),
            int(data["boundaries"]),
        )
    )
