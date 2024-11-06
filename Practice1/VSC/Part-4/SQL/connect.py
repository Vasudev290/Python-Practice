import mysql.connector

print("Starting script")

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="11pm",
        connection_timeout=5  # Adding a timeout
    )

    if connection.is_connected():
        print("Connected to MySQL Database")
    else:
        print("Failed to connect")

except mysql.connector.Error as err:
    print(f"Error: {err}")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")
