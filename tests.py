import pytest

from main import DataCapture


@pytest.fixture
def sample_data():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    return capture.build_stats()


def test_less(sample_data):
    assert sample_data.less(4) == 2
    assert sample_data.less(3) == 0
    with pytest.raises(ValueError):
        sample_data.less(10)
    with pytest.raises(ValueError):
        sample_data.less(0)


def test_greater(sample_data):
    assert sample_data.greater(4) == 2
    assert sample_data.greater(3) == 3
    with pytest.raises(ValueError):
        sample_data.greater(10)
    with pytest.raises(ValueError):
        sample_data.greater(0)


def test_between(sample_data):
    assert sample_data.between(3, 6) == 4
    assert sample_data.between(4, 9) == 3
    assert sample_data.between(3, 9) == 5
    with pytest.raises(ValueError):
        sample_data.between(1, 2)
    with pytest.raises(ValueError):
        sample_data.between(9, 10)


def test_build_stats():
    capture = DataCapture()
    capture.add(4)
    capture.add(5)
    capture.add(6)
    stats = capture.build_stats()
    assert stats.less(6) == 2
    assert stats.less(4) == 0
    assert stats.greater(4) == 2
    assert stats.greater(6) == 0
    assert stats.between(4, 6) == 3
