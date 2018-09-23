"""Route Searcher
"""
import collections
from typing import (
    Dict,
    NamedTuple,
    Set,
)

import route.exceptions


class Station(NamedTuple):
    name: str


class Router:
    def __init__(self) -> None:
        Routes = Dict[Station, Set[Station]]
        self._routes: Routes = collections.defaultdict(set)
        self._known_stations: Set[Station] = set()

    def cross_link(self, station_a: Station, station_b: Station) -> None:
        """Register given stations cross linked.
        """
        self._routes[station_a].add(station_b)
        self._routes[station_b].add(station_a)
        self._known_stations.add(station_a)
        self._known_stations.add(station_b)

    def is_linked(self, from_station: Station, to_station: Station) -> bool:
        """Return True if from_station connected to to_station.
        """
        def _is_linked(from_station: Station, scanned: Set[Station]) -> bool:
            if from_station in scanned:
                return False
            scanned.add(from_station)

            if to_station not in self._known_stations:
                raise route.exceptions.UnknownStationError()

            try:
                next_stations = self._routes[from_station]
            except KeyError:
                raise route.exceptions.UnknownStationError()

            return any(
                next_station == to_station or _is_linked(next_station, scanned)
                for next_station in next_stations
            )

        return _is_linked(from_station, set())
