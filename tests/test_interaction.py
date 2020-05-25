import pytest

from src.interaction import send


@pytest.mark.parametrize(('return_value', 'text'), [
    (True, 'success'),
    (False, 'failure'),
])
def test_send(return_value, text, mocker):
    receive = mocker.patch('src.interaction.receive')
    receive.return_value = return_value
    assert send('Hello World!') == text
    receive.assert_called_once_with('Hello World!')
