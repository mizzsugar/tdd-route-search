import pytest

import route
import route.exceptions


def test_able_to_access():
    yokohama = route.Station("横浜")
    ohmiya = route.Station("大宮")
    ohshima = route.Station("大島")

    router = route.Router()
    router.cross_link(yokohama, ohmiya)
    assert router.is_linked(yokohama, ohmiya)
    assert not router.is_linked(yokohama, ohshima)


def test_unknown_staiton():
    yokohama = route.Station("横浜")
    ohmiya = route.Station("大宮")
    ohshima = route.Station("大島")

    router = route.Router()

    with pytest.raises(route.exceptions.UnknownStationError):
        router.is_linked(yokohama, ohmiya)

    router.cross_link(yokohama, ohmiya)

    assert router.is_linked(yokohama, ohmiya)

    with pytest.raises(route.exceptions.UnknownStationError):
        router.is_linked(yokohama, ohshima)
