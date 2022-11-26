def parse_equation(equation):
    available_operations = ["+", "-", "*", "/"]
    operation = ""
    args = [""]
    index = 0

    for char in equation:
        if char in available_operations:
            operation = char
            index += 1
            args.append("")
        else:
            args[index] += char

    return operation, list(filter(bool, map(str.strip, args)))


def check_args(args):
    try:
        assert len(args) == 2
        return all(i.isnumeric() for i in args)
    except Exception:
        return False


def calculate(equation):
    operation, args = parse_equation(equation)
    if not check_args(args):
        raise Exception("Incorrect args")
    args = list(map(int, args))

    if operation == "+":
        return args[0] + args[1]

    if operation == "-":
        return args[0] - args[1]

    if operation == "*":
        return args[0] * args[1]

    if operation == "/":
        if args[1] == 0:
            raise Exception("Division by zero")
        return args[0] / args[1]

    raise Exception(f"Unknown operation '{operation}'")


def main():
    try:
        with open("input.txt", "r") as file:
            for equation in file.readlines():
                print(f"{equation.strip()} = {calculate(equation)}")
        print("Done")
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    main()
