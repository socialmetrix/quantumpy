from quantumpy import QuantumAPI

conn = QuantumAPI(741, 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJTTVgiLCJpYXQiOjE0MjM3NDY1NDQsImV4cCI6MTQ1NTI4MjU0NCwicmVxdWVzdCI6eyJ1c2VySWQiOiJkYjNjNTA2ZTIyOWI5MzgwZTk1NmQ3Yjk3OWU3MTdmYiJ9fQ.-I7neE_Es72E22HFRdr_Nj39S9sZL5q2jJ5oltbQseU')

projects = conn.get_projects()

for project in projects:
    print(project['name'], project['_id'])
    if project['_id'] == 4:
        for brand in project['brands']:
            print(brand['name'], brand['id'], brand['source']['id'])

stat_summary = conn.get_fanpages_stat_summary('4', '2015-01-10', '2015-01-11', '165175370206522')

print(stat_summary)
