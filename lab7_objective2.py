import csv
import yaml
 
csv_data = []
with open("requirements.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_data.append(dict(row))
with open("/etc/ansible/roles/router/vars/main.yaml", "w") as outfile:
    outfile.write("---\n")
    outfile.write(yaml.dump({'routers': csv_data}))