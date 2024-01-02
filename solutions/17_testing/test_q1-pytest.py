import pytest
from shared_test_data import valid_ip_addresses, \
    invalid_ip_address_fields, invalid_ip_address_range, invalid_ip_address_values
from classify import classify_ip


@pytest.mark.parametrize("ip,name", valid_ip_addresses)
def test_valid_ip_returns_class_type(ip, name):
    assert classify_ip(ip) == name


@pytest.mark.parametrize("ip", invalid_ip_address_fields)
def test_invalid_ip_fields_raises_UserWarning(ip):
    with pytest.raises(UserWarning, match='four dot'):
        classify_ip(ip)


@pytest.mark.parametrize("ip", invalid_ip_address_range)
def test_invalid_ip_ranges_raises_UserWarning(ip):
    with pytest.raises(UserWarning, match='Invalid number'):
        classify_ip(ip)


@pytest.mark.parametrize("ip", invalid_ip_address_values)
def test_invalid_ip_ranges_raises_ValueError(ip):
    with pytest.raises(ValueError):
        classify_ip(ip)
                    