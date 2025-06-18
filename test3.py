import cx_Oracle

def connect_to_oracle(username, password, host, port, service_name):
    """
    Connect to an Oracle database and return the connection object.

    :param username: Database username
    :param password: Database password
    :param host: Hostname or IP address of the Oracle server
    :param port: Port number of the Oracle server
    :param service_name: Service name of the Oracle database
    :return: Oracle database connection object
    """
    try:
        dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
        print("Connection successful!")
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"Database connection error: {e}")
        return None