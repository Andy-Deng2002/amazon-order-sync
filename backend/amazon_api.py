from models import Order

def fetch_orders():
    # 假设从 Amazon API 获取订单
    # 返回 Order 对象列表
    return [
        Order(
            order_id="123",
            status="Pending",
            order_time="2024-06-01T10:00:00",
            purchase_time="2024-06-01T12:00:00",
            ship_time=None,
            arrival_time=None,
            amazon_estimated_arrival_time="2024-06-10T18:00:00"
        ),
        Order(
            order_id="124",
            status="Shipped",
            order_time="2024-06-02T09:30:00",
            purchase_time="2024-06-02T10:00:00",
            ship_time="2024-06-03T08:00:00",
            arrival_time=None,
            amazon_estimated_arrival_time="2024-06-12T18:00:00"
        ),
        Order(
            order_id="125",
            status="Delivered",
            order_time="2024-05-28T15:20:00",
            purchase_time="2024-05-28T16:00:00",
            ship_time="2024-05-29T09:00:00",
            arrival_time="2024-06-05T14:00:00",
            amazon_estimated_arrival_time="2024-06-06T18:00:00"
        ),
    ]

def update_order_status(order_id, status):
    # 调用 Amazon SP-API 更新订单状态
    pass 