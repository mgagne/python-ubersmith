from mock import Mock
import pytest

from ubersmith.api import IntResponse


class DescribeIntResponse:
    @pytest.fixture
    def response(self):
        resp = Mock()
        resp.json.return_value = {'data': 12}
        return IntResponse(resp)

    def it_adds(self, response):
        assert response + 2 == 14
        assert 2 + response == 14

    def it_subtracts(self, response):
        assert response - 2 == 10
        assert 2 - response == 10

    def it_multiplies(self, response):
        assert response * 2 == 24
        assert 2 * response == 24

    def it_divides(self, response):
        assert response / 5 == 12 / 5
        assert 15 / response == 15 / 12

    def it_floor_divides(self, response):
        assert response // 5 == 2
        assert 15 // response == 1

    def it_mods(self, response):
        assert response % 5 == 2
        assert 15 % response == 3

    def it_pows(self, response):
        assert response ** 2 == 144
        assert 2 ** response == 4096

    def it_converts_to_int(self, response):
        result = int(response)
        assert type(result) is int
        assert result == 12

    def it_converts_to_float(self, response):
        result = float(response)
        assert type(result) is float
        assert result == 12.0

    def it_converts_to_octal(self, response):
        assert oct(response) in ['0o14', '014']

    def it_converts_to_hex(self, response):
        assert hex(response) == '0xc'

    def it_abs(self, response):
        resp = Mock()
        resp.json.return_value = {'data': -12}
        response2 = IntResponse(resp)
        assert abs(response) == 12
        assert abs(response2) == 12

    def it_negates(self, response):
        resp = Mock()
        resp.json.return_value = {'data': -12}
        response2 = IntResponse(resp)
        assert -response == -12
        assert -response2 == 12