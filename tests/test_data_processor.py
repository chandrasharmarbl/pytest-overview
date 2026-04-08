import pytest
from src.data_processor import (
    clean_data,
    normalize_numbers,
    process_user_data,
    async_fetch,
    get_cleaned_data,
)


@pytest.fixture
def sample_data():
    return [" hello ", None, "world"]


@pytest.fixture
def user_data():
    return [{"name": "Alice"}, {"name": "Bob"}]


def test_clean_data_basic(sample_data):
    assert clean_data(sample_data) == ["hello", "world"]


def test_clean_data_empty():
    assert clean_data([]) == []


def test_clean_data_mixed_types():
    data = [" a ", 1, None, "b "]
    assert clean_data(data) == ["a", 1, "b"]


def test_clean_data_invalid_input():
    with pytest.raises(TypeError):
        clean_data("not a list")


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1, 2, 3], [0.0, 0.5, 1.0]),
        ([5, 5, 5], [0.0, 0.0, 0.0]),
        ([], []),
        ([10], [0.0]),
    ],
)
def test_normalize_numbers(numbers, expected):
    assert normalize_numbers(numbers) == expected


def test_process_user_data_basic(user_data):
    assert process_user_data(user_data) == ["alice", "bob"]


def test_process_user_data_empty():
    assert process_user_data([]) == []


def test_process_user_data_missing_name():
    with pytest.raises(KeyError):
        process_user_data([{"age": 20}])


def test_get_cleaned_data(mocker):
    mocker.patch("src.data_processor.fetch_data", return_value=[" test "])
    assert get_cleaned_data() == ["test"]


@pytest.mark.asyncio
async def test_async_fetch():
    result = await async_fetch()
    assert result == [1, 2, 3]