import pytest

from city import City, Street, House

TEST_CITY_NAME = 'г. Москва'
TEST_STREET_NAME = 'ул. Власова'
TEST_HOUSE_NAME = 'д. 1'
TEST_POPULATION = 100

@pytest.fixture
def city():
    return City(TEST_CITY_NAME)

@pytest.fixture
def street(city):
    return city.add_street(TEST_STREET_NAME)

@pytest.fixture
def house(street):
    return street.add_house(TEST_HOUSE_NAME, TEST_POPULATION)

def test_empty_city(city):
    assert str(city) == 'г. Москва'
    assert city.population == 0

def test_street(street):
    assert str(street) == 'ул. Власова, г. Москва'

def test_house(house):
    assert str(house) == 'д. 1, ул. Власова, г. Москва'

@pytest.mark.usefixtures('house')
def test_population(city, street):
    assert street.population == city.population == 100
    city.remove_street(TEST_STREET_NAME)
    assert city.population == 0