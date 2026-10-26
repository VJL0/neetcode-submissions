class UndergroundSystem {
    record CheckIn(String start, int time) {}
    record Route(String start, String end) {}
    record Total(long total, int count) {}

    Map<Integer, CheckIn> idMap;
    Map<Route, Total> totalMap;

    public UndergroundSystem() {
        idMap = new HashMap<>();
        totalMap = new HashMap<>();
    }
    public void checkIn(int id, String stationName, int t) {
        idMap.put(id, new CheckIn(stationName, t));
    }
    public void checkOut(int id, String stationName, int t) {
        CheckIn checkIn = idMap.remove(id);
        Route route = new Route(checkIn.start(), stationName);

        Total totals = totalMap.getOrDefault(route, new Total(0, 0));
        
        Total total = new Total(
            totals.total() + (t - checkIn.time()),
            totals.count() + 1
        );
        totalMap.put(route, total);
    }
    public double getAverageTime(String startStation, String endStation) {
        Total ans = totalMap.get(new Route(startStation, endStation));
        return (double)ans.total()/ans.count();
    }
}
