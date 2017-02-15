import connector

# from m

cnx = connector.connect(user='scott', password='tiger',
                        host='127.0.0.1',
                        database='employees')
cnx.close()
