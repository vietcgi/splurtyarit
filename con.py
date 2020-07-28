import psycopg2

def postgres_test():

    try:
        conn = psycopg2.connect("dbname='splurty_production' user='plurty host='localhost' password='mypassword' connect_timeout=1 ")
        conn.close()
        return True
    except:
        return False
