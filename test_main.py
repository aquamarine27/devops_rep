import pytest
from main import main


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
