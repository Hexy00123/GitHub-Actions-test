import pycodestyle


def test_codestyle():
    fchecker = pycodestyle.Checker("src/main.py", show_source=False, quiet=True)
    codestyle_errors = fchecker.check_all()

    assert codestyle_errors == 0
