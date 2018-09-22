from typing import NamedTuple


class Station(NamedTuple):
    name: str


class Router:
    def cross_link(self, station_a: Station, station_b: Station) -> None:
        pass

    def is_linked(self, station_a: Station, station_b: Station) -> bool:
        return True
