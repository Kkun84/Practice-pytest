import os
import pytest

from src.file import load_numbers_sorted


@pytest.fixture
def txt(tmpdir) -> str:
    tmpfile = tmpdir.join('numbers.txt')
    with tmpfile.open('w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))
    yield str(tmpfile)
    tmpfile.remove()


def test_load_numbers_sorted(txt):
    assert load_numbers_sorted(txt) == [1, 2, 3, 4, 5]
