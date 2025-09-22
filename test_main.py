import pytest
from main import main


def test_main_output(capsys):
    """Проверка, что main печатает Hello, world!"""
    main()
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
