import pytest
from src.sorting import sort_by

# mockar resultados

criteria_min_salary = "min_salary"  # crescente
criteria_max_salary = "max_salary"  # decrescente
criteria_date_posted = "date_posted"  # decrescente
invalid_criteria = "invalid"

jobs = [
    {"min_salary": "1000", "max_salary": "2000", "date_posted": "2020-05-29"},
    {"min_salary": "500", "max_salary": "4000", "date_posted": "2018-05-29"},
    {"min_salary": "3000", "max_salary": "3500", "date_posted": "2022-05-29"},
    {
        "min_salary": "900",
        "max_salary": "1500",
    },
]

expected_result_max_salary = [
    {"min_salary": "500", "max_salary": "4000", "date_posted": "2018-05-29"},
    {"min_salary": "3000", "max_salary": "3500", "date_posted": "2022-05-29"},
    {"min_salary": "1000", "max_salary": "2000", "date_posted": "2020-05-29"},
    {
        "min_salary": "900",
        "max_salary": "1500",
    },
]

expected_result_min_salary = [
    {"min_salary": "500", "max_salary": "4000", "date_posted": "2018-05-29"},
    {
        "min_salary": "900",
        "max_salary": "1500",
    },
    {"min_salary": "1000", "max_salary": "2000", "date_posted": "2020-05-29"},
    {"min_salary": "3000", "max_salary": "3500", "date_posted": "2022-05-29"},
]

expected_result_date_posted = [
    {"min_salary": "3000", "max_salary": "3500", "date_posted": "2022-05-29"},
    {"min_salary": "1000", "max_salary": "2000", "date_posted": "2020-05-29"},
    {"min_salary": "500", "max_salary": "4000", "date_posted": "2018-05-29"},
    {
        "min_salary": "900",
        "max_salary": "1500",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, criteria_max_salary)
    assert jobs == expected_result_max_salary

    sort_by(jobs, criteria_min_salary)
    assert jobs == expected_result_min_salary

    sort_by(jobs, criteria_date_posted)
    assert jobs == expected_result_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs, invalid_criteria)
