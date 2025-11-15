import requests, datetime
from mysqldb import insertMBTARecord

URL = "https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip"

def callMBTAApi():
    r = requests.get(URL, timeout=10)
    r.raise_for_status()
    data = r.json()

    out = []
    for v in data.get("data", []):
        attr = v.get("attributes", {})
        d = {
            "id": v.get("id"),
            "label": attr.get("label"),
            "latitude": attr.get("latitude"),
            "longitude": attr.get("longitude"),
            "updated_at": attr.get("updated_at"),
            "current_stop_sequence": attr.get("current_stop_sequence"),
            "speed": attr.get("speed"),
            "occupancy_status": attr.get("occupancy_status"),
            "direction_id": attr.get("direction_id"),
            "route_id": attr.get("route", "1"),
            "trip_id": (v.get("relationships", {})
                        .get("trip", {}).get("data", {}) or {}).get("id"),
            "bearing": attr.get("bearing"),
            "stop_id": attr.get("stop", None),
            "vehicle_status": attr.get("current_status")
        }
        out.append(d)

    # store in MySQL
    if out:
        insertMBTARecord(out)
    return out
