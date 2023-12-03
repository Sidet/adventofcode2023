from typing import Callable

from . import load


def check(directory: str, solve: Callable[[list[str]], str]) -> bool:
    example_2 = load.example_inputs_2(directory)
    answer_2 = load.example_answer_2(directory)

    if example_2:
        result = solve(example_2)
        if answer_2 == result:
            print("Example 2 passed.")
            return True
        else:
            print(f"Example 2 returned {result}. Expected {answer_2}.")
            return False

    example_1 = load.example_inputs_1(directory)
    answer_1 = load.example_answer_1(directory)

    if example_1:
        result = solve(example_1)
        if answer_1 == result:
            print("Example 1 passed.")
            return True
        else:
            print(f"Example 1 returned {result}. Expected {answer_1}.")
            return False

    print("Examples not found.")
    return False
