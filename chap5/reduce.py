from functools import reduce


def low_med_high(d, k, breaks):
    if float(d[k]) < breaks[0]:
        return "low"
    elif float(d[k]) < breaks[1]:
        return "medium"
    else:
        return "high"


def clean_entry(d):
    r = {"profit": None, "mpg": None, "odo": None}
    r["profit"] = float(d.get("price-sell", 0)) - float(d.get("price-buy", 0))
    r["mpg"] = low_med_high(d, "mpg", (18, 35))
    r["odo"] = low_med_high(d, "odo", (60000, 100000))
    return r


def acc_average(acc, profit):
    acc["total"] = acc.get("total", 0) + profit
    acc["count"] = acc.get("count", 0) + 1
    acc["average"] = acc.get("total", 0) / acc.get("count", 1)
    return acc


def sort_and_add(acc, nxt):
    p = nxt.get("profit", 0)

    acc["mpg"][nxt["mpg"]] = acc_average(acc["mpg"].get(nxt["mpg"], {}), p)
    acc["odo"][nxt["odo"]] = acc_average(acc["odo"].get(nxt["odo"], {}), p)
    return acc


if __name__ == "__main__":
    import json

    with open("cars.json") as f:
        cars = json.load(f)

    results = reduce(sort_and_add, map(clean_entry, cars), {"mpg": {}, "odo": {}})
    print(json.dumps(results, indent=4))
