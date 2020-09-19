
from cassandra.cluster import Cluster

cluster = Cluster()

session = cluster.connect('test_keyspace')

rows = session.execute("SELECT * from employee_by_uuid")

for row in rows:

    print row.first_name,row.last_name

    print "Finished ...!!"