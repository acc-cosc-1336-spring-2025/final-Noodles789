def create_multiplication_table(rows: int = 5, cols: int = 10) -> list[list[int]]:
    return [
        [i * j for j in range(1, cols + 1)]
        for i in range(1, rows + 1)
    ]
def display_table(table: list[list[int]], col_width: int = 4) -> None:

    for row in table:
        print(' '.join(f"{num:{col_width}}" for num in row))


def test_config() -> bool:

    return True