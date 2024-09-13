import pycodestyle
import os


def check_dir(dir_name):
    wrong_codestyle_files = []

    for root, _, files in os.walk(dir_name):
        path = root.split(os.sep)
        for file in files:
            file_path = "/".join(path) + "/" + file

            if file_path.endswith(".py"):
                checker = pycodestyle.Checker(file_path, show_source=False, quiet=True)
                if checker.check_all() != 0:
                    wrong_codestyle_files.append(file_path)

    return wrong_codestyle_files


def test_codestyle():
    wrong_codestyle_files = check_dir("src")

    assert len(wrong_codestyle_files) == 0, "; ".join(wrong_codestyle_files)
