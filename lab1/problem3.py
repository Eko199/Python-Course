INVALID_FORMAT_MSG = "Невалиден формат"
INVALID_LETTERS_MSG = "Невалидни букви"
INVALID_CODE_MSG = "Невалиден регионален код"

ALLOWED_LETTERS = set("АВЕКМНОРСТУХ")

REGION_CODES = {
    "Е": "Благоевград",
    "А": "Бургас",
    "В": "Варна",
    "ВТ": "Велико Търново",
    "ВН": "Видин",
    "ВР": "Враца",
    "ЕВ": "Габрово",
    "ТХ": "Добрич",
    "К": "Кърджали",
    "КН": "Кюстендил",
    "ОВ": "Ловеч",
    "М": "Монтана",
    "РА": "Пазарджик",
    "РК": "Перник",
    "ЕН": "Плевен",
    "РВ": "Пловдив",
    "РР": "Разград",
    "Р ": "Русе",
    "СС": "Силистра",
    "СН": "Сливен",
    "СМ": "Смолян",
    "СО": "София (област)",
    "С": "София (столица)",
    "СА": "София (столица)",
    "СВ": "София (столица)",
    "СТ": "Стара Загора",
    "Т": "Търговище",
    "Х": "Хасково",
    "Н": "Шумен",
    "У": "Ямбол",
}

def is_valid(license_plate):
    license_plate = license_plate.upper()
    
    isSecondLetter = license_plate[1].isalpha()

    if (len(license_plate) != 7 + int(isSecondLetter) or not license_plate[0].isalpha() or not license_plate[-2:].isalpha() or not license_plate[-6:-2].isdigit()):
        return False, INVALID_FORMAT_MSG
    
    if (not { license_plate[0], *license_plate[-2:] } <= ALLOWED_LETTERS or (isSecondLetter and not license_plate[1] in ALLOWED_LETTERS)):
        return False, INVALID_LETTERS_MSG
    
    region = REGION_CODES.get(license_plate[0:2] if isSecondLetter else license_plate[0])
    
    return (True, region) if region is not None else (False, INVALID_CODE_MSG)

assert is_valid("СА1234АВ") == (True, "София (столица)")
assert is_valid("С1234АВ") == (True, "София (столица)")
assert is_valid("ТХ0000ТХ") == (True, "Добрич")
assert is_valid("ТХ000ТХ") == (False, INVALID_FORMAT_MSG)
assert is_valid("ТХ0000Т") == (False, INVALID_FORMAT_MSG)
assert is_valid("ТХ0000ТХХ") == (False, INVALID_FORMAT_MSG)
assert is_valid("У8888СТ") == (True, "Ямбол")
assert is_valid("Y8888CT") == (False, INVALID_LETTERS_MSG)
assert is_valid("ПЛ7777АА") == (False, INVALID_LETTERS_MSG)
assert is_valid("РВ7777БВ") == (False, INVALID_LETTERS_MSG)
assert is_valid("ВВ6666КН") == (False, INVALID_CODE_MSG)

"✅ All OK! +1.25 points"