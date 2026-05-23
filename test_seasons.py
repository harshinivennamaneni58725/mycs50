from datetime import date
from seasons import calculate_minutes, minutes_to_words


def test_calculate_minutes():
    assert calculate_minutes(date(2021, 1, 1), date(2022, 1, 1)) == 525600
    assert calculate_minutes(date(2021, 1, 1), date(2023, 1, 1)) == 1051200


def test_minutes_to_words():
    assert (
        minutes_to_words(525600)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        minutes_to_words(1051200)
        == "One million, fifty-one thousand, two hundred minutes"
    )
