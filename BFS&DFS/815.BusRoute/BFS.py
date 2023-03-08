from collections import defaultdict
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        station2route = defaultdict(set)
        for i, stations in enumerate(routes):
            for station in stations:
                station2route[station].add(i)
        cur_routes = station2route[S]
        tar_routes = station2route[T]
        count = 1
        used_route = set()
        for route in cur_routes:
            if route in tar_routes:
                return count
            used_route.add(route)

        used_stations = set()
        while cur_routes:
            count += 1
            next_routes = []

            for route in cur_routes:
                for station in routes[route]:
                    if station not in used_stations:
                        for next_route in station2route[station]:
                            if next_route not in used_route:
                                if next_route in tar_routes:
                                    return count
                                next_routes.append(next_route)
                                used_route.add(next_route)
                        used_stations.add(station)
            cur_routes = next_routes
        return -1

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source = 15
target = 12
a = Solution().numBusesToDestination(routes, source, target)
print(a)