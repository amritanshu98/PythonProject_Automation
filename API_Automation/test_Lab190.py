import pytest

@pytest.fixture()
def sample_data():
    data = [1,2,3,4,5]
    return data

@pytest.fixture()
def sample_data2():
    return True

def test_verify_sample_data(sample_data,sample_data2):
    print("Sample Data: ", sample_data)
    print("Sample Data2: ", sample_data2)