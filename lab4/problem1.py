import os

class InvalidLineError(Exception):
    def __init__(self, line: str) -> None:
        super().__init__(line)

class InvalidItemError(Exception):
    def __init__(self, item: str) -> None:
        super().__init__(item)

class InvalidQuantityError(Exception):
    def __init__(self, item: tuple[str, str]) -> None:
        super().__init__(*item)

class InvalidPriceError(Exception):
    def __init__(self, item: tuple[str, str]) -> None:
        super().__init__(*item)

class ListFileError(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(path)

def validate_list(path: str) -> float:
    if not os.path.isfile(path):
        raise ListFileError(path)

    sum: float = 0.0
    
    try:
        with open(path, encoding="utf-8") as file:
            lines: list[str] = file.readlines()

            for line in lines:
                item: list[str] = line[1:].strip().split(":")

                if line[0] != "-" or len(item) != 3:
                    raise InvalidLineError(line)

                name, quantity, price = item

                if name == "" or name.isdigit():
                    raise InvalidItemError(name)

                if not quantity.isdigit():
                    raise InvalidQuantityError((name, quantity))

                if not set(price) <= set("1234567890.") or price.endswith("."):
                    raise InvalidPriceError((name, price))
                
                sum += int(quantity) * float(price)
    except (IOError, UnicodeDecodeError):
        raise ListFileError(path)

    return sum

assert abs(validate_list(os.path.join("task_1", "list1.txt")) - 11.25) < 0.001

assert int(validate_list(os.path.join("task_1", "list2.txt"))) == 0, "Empty files should return 0"

try:
    validate_list(os.path.join("task_1", "list3.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("task_1", "list4.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("task_1", "list5.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidItemError:
    pass

try:
    validate_list(os.path.join("task_1", "list6.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list7.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list8.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list9.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("task_1", "list10.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("task_1", "list11.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

"✅ All OK! +1 point"