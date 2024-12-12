from django.db import connection

class Queries:
    @staticmethod
    def get_orders_by_server_id(server_id):
        query = """
            SELECT * FROM ticket_app_order WHERE server_id = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [server_id])
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results

    @staticmethod
    def get_tables_by_server_id(server_id):
        query = """
            SELECT * FROM ticket_app_table WHERE server_id = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [server_id])
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results

    @staticmethod
    def get_items_by_station_id(station_id):
        query = """
            SELECT * FROM ticket_app_item WHERE station_id = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [station_id])
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
