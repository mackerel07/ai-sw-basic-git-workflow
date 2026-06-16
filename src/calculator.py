from __future__ import annotations

import math
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Callable


Number = int | float
Operation = Callable[[Number, Number], Number]
EXIT_COMMANDS = {"q", "quit", "exit", "종료"}
MODULE_DIR = Path(__file__).with_name("calculator")


def _load_operation(module_name: str, function_name: str) -> Operation:
    module_path = MODULE_DIR / f"{module_name}.py"
    spec = spec_from_file_location(f"calculator_operations.{module_name}", module_path)

    if spec is None or spec.loader is None:
        raise ImportError(f"{module_path} 모듈을 불러올 수 없습니다.")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    operation = getattr(module, function_name, None)
    if not callable(operation):
        raise ImportError(f"{module_path}에 {function_name} 함수가 없습니다.")

    return operation


add = _load_operation("add", "add")
subtract = _load_operation("subtract", "substract")
multiply = _load_operation("multiply", "multiply")
divide = _load_operation("divide", "divide")

OPERATIONS: dict[str, Operation] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def parse_number(value: str) -> Number:
    try:
        number = float(value.strip())
    except ValueError as exc:
        raise ValueError("숫자를 입력해 주세요.") from exc

    if not math.isfinite(number):
        raise ValueError("유효한 숫자를 입력해 주세요.")

    if number.is_integer():
        return int(number)

    return number


def calculate(left: Number, operator: str, right: Number) -> Number:
    operation = OPERATIONS.get(operator.strip())
    if operation is None:
        raise ValueError("지원하지 않는 연산자입니다. +, -, *, / 중 하나를 입력해 주세요.")

    return operation(left, right)


def format_number(number: Number) -> str:
    if isinstance(number, float) and number.is_integer():
        return str(int(number))

    return str(number)


def is_exit_command(value: str) -> bool:
    return value.strip().lower() in EXIT_COMMANDS


def main() -> None:
    print("계산기 프로그램")
    print("종료하려면 q, quit, exit 또는 종료를 입력하세요.")

    while True:
        first_input = input("첫 번째 숫자: ")
        if is_exit_command(first_input):
            break

        operator = input("연산자(+, -, *, /): ")
        if is_exit_command(operator):
            break

        second_input = input("두 번째 숫자: ")
        if is_exit_command(second_input):
            break

        try:
            left = parse_number(first_input)
            right = parse_number(second_input)
            result = calculate(left, operator, right)
        except ValueError as exc:
            print(f"오류: {exc}")
            continue

        print(
            "결과: "
            f"{format_number(left)} {operator.strip()} "
            f"{format_number(right)} = {format_number(result)}"
        )

    print("계산기를 종료합니다.")


if __name__ == "__main__":
    main()
