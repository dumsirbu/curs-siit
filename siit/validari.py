class InvalidName(ValueError):
    pass

class NameTooLong(InvalidName):
    pass

def validate_name(name):
    if len(name) > 25:
        raise NameTooLong("Name too long")
    return name

validate_name("Georgel")
validate_name("asdasdasdasdasdasdasdasdasd")