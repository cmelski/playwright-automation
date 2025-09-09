import pytest


@pytest.fixture(scope='module')
def pre_work():
    print('This is pre-work setup')
    return 'pass'


@pytest.fixture(scope='function')
def second_work():
    print('This is secondary work')
    yield 'pass'
    print('tear down validation')



@pytest.mark.tcid1
def test_initial_check(pre_work, second_work):
    print('first test')
    assert pre_work == 'pass', f'pre-work did not return {pre_work}'
    assert second_work == 'pass'


@pytest.mark.smoke
def test_second_check(second_work):
    print('second test')
