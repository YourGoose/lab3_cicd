import pytest
from lesson_testing import (
    square_eq_solver,
    show_result,
    main_first_script,
    is_palindrome_iterative,
    main_second_script,
    compute_factorial,
    main_third_script,
    main,
)


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, -13, 12, [1.0, 12.0]),  
        (1, 2, 1, [-1.0]),     
        (4, 5, 6, []),          
    ]
)
def test_square_eq_solver(a, b, c, expected):
    assert sorted(square_eq_solver(a, b, c)) == sorted(expected)


@pytest.mark.parametrize("word,expected", [
    ("level", True),
    ("Mom", True),
    ("python", False),
    ("StTs", True),
    ("gJ", False),
])
def test_is_palindrome_iterative(word, expected):
    assert is_palindrome_iterative(word) == expected


@pytest.mark.parametrize("a,expected", [
    (5, 120),
    (0, 1),
    (10,3628800),
])
def test_compute_factorial(a, expected):
    assert compute_factorial(a) == expected

def test_compute_factorial_negative():
    with pytest.raises(ValueError) as excinfo:
        compute_factorial(-5)
    assert "Факториал отрицательного числа не определён" in str(excinfo.value)


@pytest.mark.parametrize(
    "data, expected",
    [
        ([1.2345, 2.3456], ["Корень номер 1 равен 1.23", "Корень номер 2 равен 2.35"]),
        ([12.0], ["Корень номер 1 равен 12.0"]),
        ([], ["Уравнение с заданными параметрами не имеет корней"]),
    ]
)
def test_show_result(capsys, data, expected):
    show_result(data)
    captured = capsys.readouterr()

    for phrase in expected:
        assert phrase in captured.out

    
@pytest.mark.parametrize(
    "user_input, expected_result, expected_output",
    [
        ("1 -13 12", [1.0, 12.0], ["Корень номер 1 равен", "Корень номер 2 равен"]),
        ("1 2 1", [-1.0], ["Корень номер 1 равен -1.0"]),
        ("4 5 6", [], ["не имеет корней"]),
    ],
)
def test_main_first_script(monkeypatch, capsys, user_input, expected_result, expected_output):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    result = main_first_script()
    assert sorted(result) == sorted(expected_result)
    captured = capsys.readouterr()

    for phrase in expected_output:
        assert phrase in captured.out

@pytest.mark.parametrize(
    "user_input, expected_result, expected_output",
    [
        ("level", True, "Строка является палиндромом"),           
        ("python", False, "Строка не является палиндромом"),      
        ("StTs", True, "Строка является палиндромом"),        
    ],
)
def test_main_second_script(monkeypatch, capsys, user_input, expected_result, expected_output):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    result = main_second_script()
    assert result == expected_result
    captured = capsys.readouterr()
    assert expected_output in captured.out


@pytest.mark.parametrize(
    "user_input, expected_result, expected_output",
    [
        ("5", 120, "Факториал числа 5 равен 120"),
        ("0", 1, "Факториал числа 0 равен 1"),
    ],
)
def test_main_third_script(monkeypatch, capsys, user_input, expected_result, expected_output):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    result = main_third_script()
    assert result == expected_result
    captured = capsys.readouterr()
    assert expected_output in captured.out

def test_main_third_script_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "-5")

    with pytest.raises(ValueError, match="Факториал отрицательного числа не определён"):
        main_third_script()


@pytest.mark.parametrize(
    "menu_inputs, expected_output",
    [
        (["1", "1 -13 12"], ["Корень номер 1 равен", "Корень номер 2 равен"]),
        (["2", "level"], ["Строка является палиндромом"]),
        (["3", "5"], ["Факториал числа 5 равен 120"]),
    ],
)
def test_main(monkeypatch, capsys, menu_inputs, expected_output):
    inputs = iter(menu_inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    for phrase in expected_output:
        assert phrase in captured.out

def test_main_exit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "999")
    with pytest.raises(SystemExit):
        main()