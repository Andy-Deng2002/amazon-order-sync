import csv

def export_orders_to_csv(orders):
    fieldnames = [
        "order_id",
        "status",
        "order_time",
        "purchase_time",
        "ship_time",
        "arrival_time",
        "amazon_estimated_arrival_time"
    ]
    path = "orders_export.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for order in orders:
            writer.writerow({
                "order_id": order.order_id,
                "status": order.status,
                "order_time": order.order_time,
                "purchase_time": order.purchase_time,
                "ship_time": order.ship_time,
                "arrival_time": order.arrival_time,
                "amazon_estimated_arrival_time": order.amazon_estimated_arrival_time
            })
    return path 