from utils import calculate_discount, is_even, get_full_name

# 1
def test_calculate_discount_20():
    assert calculate_discount(100.0, 20.0) == 80.0


def test_calculate_discount_50():
    assert calculate_discount(200.0, 50.0) == 100.0


def test_calculate_discount_0():
    assert calculate_discount(150.0, 0.0) == 150.0


def test_calculate_discount_price_zero():
    assert calculate_discount(0.0, 15.0) == 0.0


def test_calculate_discount_other():
    assert calculate_discount(80.0, 25.0) == 60.0

# 2
def test_is_even_positive_even():
    assert is_even(4) is True


def test_is_even_positive_odd():
    assert is_even(7) is False


def test_is_even_negative_even():
    assert is_even(-2) is True


def test_is_even_negative_odd():
    assert is_even(-5) is False


def test_is_even_zero():
    assert is_even(0) is True

# 3
def test_get_full_name_standard():
    assert get_full_name("Даша", "Шевченко") == "Даша Шевченко"


def test_get_full_name_short():
    assert get_full_name("А", "Б") == "А Б"


def test_get_full_name_long():
    assert get_full_name("Олександра-Марія", "Константинопольська") == "Олександра-Марія Константинопольська"


def test_get_full_name_single_char():
    assert get_full_name("J", "D") == "J D"


def test_get_full_name_other():
    assert get_full_name("Іван", "Петров") == "Іван Петров"