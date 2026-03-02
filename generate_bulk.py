import os
import csv
from jinja2 import Environment, FileSystemLoader

# Template env setup
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('access_switch.j2')

os.makedirs("outputs", exist_ok=True)

# Open and read the CSV file
with open('data/switches.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
   # Loop through each switch in the CSV
    for row in csv_reader:
        
        # --- PROCESS VLAN DATABASE ---
        raw_vlan = row['vlan_database'].split(' ')
        structured_vlan = []
        for vlan in raw_vlan:
            v_id, v_name = vlan.split(':')
            structured_vlan.append({
                "id": v_id,
                "name": v_name
            })
        row['vlan_database'] = structured_vlan

        # --- PROCESS ACCESS INTERFACES ---
        raw_access = row['access_interfaces'].split(' ')
        structured_access = []
        for item in raw_access:
            if_name, if_vlan = item.split(':')
            structured_access.append({
                "name": if_name,
                "id": if_vlan
            })
        row['access_interfaces'] = structured_access
        
        # --- PROCESS TRUNK INTERFACES ---
        structured_trunks = []
        # Only process if the CSV cell isn't empty
        if row.get('trunk_interfaces'):
            raw_trunks = row['trunk_interfaces'].split(' ')
            for item in raw_trunks:
                if_name, allowed_vlans = item.split(':')
                structured_trunks.append({
                    "name": if_name,
                    "vlans": allowed_vlans
                })
        row['trunk_interfaces'] = structured_trunks

        # Render the template for the current row
        rendered_config = template.render(row)
        
        # Save the output
        output_filename = f"outputs/{row['hostname']}.cfg"
        with open(output_filename, "w") as out_file:
            out_file.write(rendered_config)
            
        print(f"Success: Generated {output_filename}")

print("Bulk deployment configuration complete!")