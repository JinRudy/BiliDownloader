import sqlite3

class SQLiteDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        # columns format: [(column_name, data_type), ...]
        columns_str = ', '.join([f'{col[0]} {col[1]}' for col in columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_data(self, table_name, data):
        # data format: {column_name: value, ...}
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data.keys()])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_query, list(data.values()))
        self.connection.commit()

    def update_data(self, table_name, data, condition):
        # data format: {column_name: value, ...}
        # condition format: "column_name = value"
        set_values = ', '.join([f"{col} = ?" for col in data.keys()])
        update_query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
        self.cursor.execute(update_query, list(data.values()))
        self.connection.commit()

    def delete_data(self, table_name, condition):
        # condition format: "column_name = value"
        delete_query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(delete_query)
        self.connection.commit()

    def select_data(self, table_name, columns=None, condition=None):
        columns = ', '.join(columns) if columns else '*'
        select_query = f"SELECT {columns} FROM {table_name}"
        if condition:
            select_query += f" WHERE {condition}"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

# Example usage:
# Initialize database object
db = SQLiteDatabase('example.db')

# Create table
db.create_table('users', [('id', 'INTEGER PRIMARY KEY'), ('name', 'TEXT'), ('age', 'INTEGER')])

# Insert data
db.insert_data('users', {'name': 'Alice', 'age': 30})

# Update data
db.update_data('users', {'age': 31}, 'name = "Alice"')

# Select data
result = db.select_data('users')
print(result)

# Delete data
db.delete_data('users', 'name = "Alice"')

# Close connection
db.close()
