import sqlite3


def connect() -> (sqlite3.Connection, sqlite3.Cursor):
    connection = sqlite3.connect("model.db")
    cursor = connection.cursor()
    return connection, cursor


def complete(connection : sqlite3.Connection, cursor : sqlite3.Cursor):
    connection.commit() 
    connection.close()
    

def get_catalog() -> str:
    connection, cursor = connect()
    cursor.execute("""SELECT product.rowid, name, price, COUNT(*)
                    FROM product LEFT JOIN item
                    ON product.rowid = item.product_id
                    WHERE order_id IS NULL
                    GROUP BY name
                    ORDER BY product.rowid""")
    result = cursor.fetchall()
    result = [str(rowid) + " " + name + " " + str(price) + " руб. " +
              str(number) + " шт." for rowid, name, price, number in result]
    result = "\n".join(result)
    complete(connection, cursor)
    return result


def add_order(address : str) -> str:
    connection, cursor = connect()
    cursor.execute("""INSERT INTO 'order' VALUES
                   (?, ?)""", [address, "ФОРМИРУЕТСЯ"])
    cursor.execute("""SELECT MAX(rowid)
                   FROM 'order'""")  # how to get id from select
    result = str(cursor.fetchone()[0])
    complete(connection, cursor)
    return "Номер заказа: " + result


# order id check
def add_product(order_number : int, product_number : int, number : int) -> str:
    connection, cursor = connect()
    cursor.execute("""SELECT rowid
                   FROM item
                   WHERE product_id = ? AND order_id is NULL""", [product_number])
    result = [record[0] for record in cursor.fetchall()]
    cursor.execute("""SELECT status
                   FROM 'order'
                   WHERE rowid = ?""", [order_number])
    status = cursor.fetchone()[0]
    if len(result) >= number and status == "ФОРМИРУЕТСЯ" and number > 0:
        for item_id in result[:number]:
            cursor.execute("""UPDATE item
                           SET order_id = ?
                           WHERE rowid = ?""", [order_number, item_id])
        result = "Товары добавлены в заказ"
    else:
        result = "Ошибка"
    complete(connection, cursor)
    return result


# order id check
def remove_product(order_number : int, product_number : int, number : int) -> str:
    connection, cursor = connect()
    cursor.execute("""SELECT rowid
                   FROM item
                   WHERE product_id = ? AND order_id = ?""", [product_number, order_number])
    result = [record[0] for record in cursor.fetchall()]
    cursor.execute("""SELECT status
                   FROM 'order'
                   WHERE rowid = ?""", [order_number])
    status = cursor.fetchone()[0]
    if len(result) >= number and status == "ФОРМИРУЕТСЯ" and number > 0:
        for item_id in result[:number]:
            cursor.execute("""UPDATE item
                           SET order_id = NULL
                           WHERE rowid = ?""", [item_id])
        result = "Товары удалены из заказа"
    else:
        result = "Ошибка"
    complete(connection, cursor)
    return result


# order id check
def form_order(order_number : int) -> str:
    connection, cursor = connect()
    cursor.execute("""SELECT status
                   FROM 'order'
                   WHERE rowid = ?""", [order_number])
    result = cursor.fetchone()[0]
    if (result == "ФОРМИРУЕТСЯ"):
        cursor.execute("""UPDATE 'order'
                       SET status = ?
                       WHERE rowid = ?""", ["АКТИВЕН", order_number])
        result = "Заказ сформирован"
    else:
        result = "Ошибка"
    complete(connection, cursor)
    return result


# order id check
def cancel_order(order_number : int) -> str:
    connection, cursor = connect()
    cursor.execute("""SELECT status
                   FROM 'order'
                   WHERE rowid = ?""", [order_number])
    result = cursor.fetchone()[0]
    if (result != "ВЫПОЛНЕН"):
        cursor.execute("""UPDATE 'order'
                       SET status = ?
                       WHERE rowid = ?""", ["ОТМЕНЕН", order_number])
        result = "Заказ отменён"
    else:
        result = "Ошибка"
    complete(connection, cursor)
    return result


# order id check
def get_order(order_number : int) -> str:
    connection, cursor = connect()
    cursor.execute("""SELECT name, price, COUNT(*)
                    FROM product LEFT JOIN item
                    ON product.rowid = item.product_id
                    WHERE order_id = ?
                    GROUP BY name
                    ORDER BY product.rowid""", [order_number])
    result = cursor.fetchall()
    result = [name + " " + str(price) + " руб. " +
              str(number) + " шт." for name, price, number in result]
    cursor.execute("""SELECT SUM(price)
                    FROM item LEFT JOIN product
                    ON item.product_id = product.rowid
                    WHERE item.order_id = ?""", [order_number])
    cost = str(cursor.fetchone()[0])
    result.append(f"Итого: {cost} руб.")
    result.append("Доставка: 20 руб.")
    cursor.execute("""SELECT address, status
                   FROM 'order'
                   WHERE rowid = ?""", [order_number])
    address, status = cursor.fetchone()
    result.append(f"Адрес: {address}")
    result.append(f"Статус: {status}")
    result.append(f"Номер: {order_number}")
    result = "\n".join(result)
    complete(connection, cursor)
    return result
