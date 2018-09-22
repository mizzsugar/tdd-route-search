import route


def test_able_to_access():
    yokohama = route.Station("横浜")
    ohmiya = route.Station("大宮")

    router = route.Router()
    router.cross_link(yokohama, ohmiya)
    assert router.is_linked(yokohama, ohmiya)
