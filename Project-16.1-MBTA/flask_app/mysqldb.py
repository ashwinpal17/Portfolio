import mysql.connector
from datetime import datetime

def get_conn():
    return mysql.connector.connect(
        host="127.0.0.1", port=3307,
        user="user", password="user", database="MBTA"
    )

def _to_dt(x):
    if not x:
        return None
    # '2025-11-09T14:57:49-05:00' -> '2025-11-09 14:57:49'
    return x.split('.')[0].replace('T', ' ')[:19]

def insertMBTARecord(rows):
    sql = """
      INSERT INTO mbta_buses
      (id,label,latitude,longitude,updated_at,current_stop_sequence,
       speed,occupancy_status,direction_id,route_id,trip_id,bearing,stop_id,vehicle_status)
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
      ON DUPLICATE KEY UPDATE
        label=VALUES(label), latitude=VALUES(latitude), longitude=VALUES(longitude),
        updated_at=VALUES(updated_at), current_stop_sequence=VALUES(current_stop_sequence),
        speed=VALUES(speed), occupancy_status=VALUES(occupancy_status),
        direction_id=VALUES(direction_id), route_id=VALUES(route_id),
        trip_id=VALUES(trip_id), bearing=VALUES(bearing),
        stop_id=VALUES(stop_id), vehicle_status=VALUES(vehicle_status)
    """
    vals = [(
        r.get("id"), r.get("label"), r.get("latitude"), r.get("longitude"),
        _to_dt(r.get("updated_at")), r.get("current_stop_sequence"),
        r.get("speed"), r.get("occupancy_status"), r.get("direction_id"),
        r.get("route_id"), r.get("trip_id"), r.get("bearing"),
        r.get("stop_id"), r.get("vehicle_status")
    ) for r in rows]

    conn = get_conn()
    cur = conn.cursor()
    cur.executemany(sql, vals)
    conn.commit()
    cur.close(); conn.close()
