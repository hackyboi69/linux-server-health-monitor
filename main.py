servers = [
{"name": "Web-01", "cpu": 45, "ram": 60},
    {"name": "DB-01", "cpu": 92, "ram": 85},
    {"name": "API-01", "cpu": 78, "ram": 95},
    {"name": "Backup-01", "cpu": 25, "ram": 30},
    {"name": "Cloud-01", "cpu": 97, "ram": 98}
]
def cpu_health(servers):
 warning_status = 0
 critical_status = 0
 normal_status = 0
 cpu_statuses = []
 for server in servers:
    if server["cpu"] >= 90:
     cpu_status = "CRITICAL"
     critical_status = critical_status + 1
     cpu_statuses.append("CRITICAL")
    elif server["cpu"] >= 70:
        cpu_status = "WARNING"
        warning_status = warning_status + 1
        cpu_statuses.append("WARNING")
    else:
        cpu_status = "NORMAL"
        normal_status = normal_status + 1
        cpu_statuses.append("NORMAL")
 return cpu_statuses, warning_status, critical_status, normal_status
cpu_statuses, cpu_warning_counter, cpu_critical_counter, cpu_normal_counter = cpu_health(servers)

def ram_health(servers):
 warning_status = 0
 critical_status = 0
 normal_status = 0
 ram_statuses = []
 for server in servers:
    if server["ram"] >= 90:
     ram_status = "CRITICAL"
     critical_status = critical_status + 1
     ram_statuses.append("CRITICAL")
    elif server["ram"] >= 70:
        ram_status = "WARNING"
        warning_status = warning_status + 1
        ram_statuses.append("WARNING")
    else:
        ram_status = "NORMAL"
        normal_status = normal_status + 1
        ram_statuses.append("NORMAL")
 return ram_statuses, warning_status, critical_status, normal_status

ram_statuses, ram_warning_counter, ram_critical_counter, ram_normal_counter = ram_health(servers)

server_count = len(servers)

cpu_sum = 0
for server in servers:
    cpu_sum = cpu_sum + server["cpu"]
average_cpu_usage = cpu_sum / server_count

ram_sum =0
for server in servers:
    ram_sum = ram_sum + server["ram"]
average_ram_usage = ram_sum / server_count

highest_cpu_usage = servers[0]["cpu"]
highest_cpu_server = servers[0]["name"]

for server in servers:
    if server["cpu"] > highest_cpu_usage:
     highest_cpu_usage = server["cpu"]
     highest_cpu_server = server["name"]

lowest_cpu_usage = servers[0]["cpu"]
lowest_cpu_server = servers[0]["name"]

for server in servers:
    if server["cpu"] < lowest_cpu_usage:
     lowest_cpu_usage = server["cpu"]
     lowest_cpu_server = server["name"]

highest_ram_usage = servers[0]["ram"]
highest_ram_server = servers[0]["name"]

for server in servers:
    if server["ram"] > highest_ram_usage:
     highest_ram_usage = server["ram"]
     highest_ram_server = server["name"]

lowest_ram_usage = servers[0]["ram"]
lowest_ram_server = servers[0]["name"]

for server in servers:
    if server["ram"] < lowest_ram_usage:
     lowest_ram_usage = server["ram"]
     lowest_ram_server = server["name"]

for index, server in enumerate(servers):
    print("=================================================================")
    print(f"{server["name"]} RAM: {server["ram"]}% - {ram_statuses[index]}  |  CPU: {server["cpu"]}% - {cpu_statuses[index]}")
print("=====================================================================")
print(f"Servers:{server_count}")
print("---------------------------------------------------------------------")
print(f"CPU CRITICALS:{cpu_critical_counter}  |  RAM CRITICALS:{ram_critical_counter}")
print("---------------------------------------------------------------------")
print(f"CPU WARNINGS:{cpu_warning_counter}  |  RAM WARNINGS:{ram_warning_counter}")
print("-------------------------------------------------------------------- ")
print(f"CPU NORMAL:{cpu_normal_counter}  |  RAM NORMAL:{ram_normal_counter}")
print("---------------------------------------------------------------------")
print(f"AVERAGE CPU USAGE:{average_cpu_usage}%")
print("---------------------------------------------------------------------")
print(f"AVERAGE RAM USAGE:{average_ram_usage}%")
print("---------------------------------------------------------------------")
print(f"HIGHEST CPU USAGE:{highest_cpu_server} - {highest_cpu_usage}%")
print("---------------------------------------------------------------------")
print(f"LOWEST CPU USAGE:{lowest_cpu_server} - {lowest_cpu_usage}%")
print("---------------------------------------------------------------------")
print(f"HIGHEST RAM USAGE:{highest_ram_server} - {highest_ram_usage}%")
print("---------------------------------------------------------------------")
print(f"LOWEST RAM USAGE:{lowest_ram_server} - {lowest_ram_usage}%")
print("=====================================================================")