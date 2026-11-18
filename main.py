import subprocess
import time
from datetime import datetime

def check_disk(disk_percent):
  if disk_percent >= 90:
    return "FULL!"
  elif disk_percent >= 70:
    return "WARNING!"
  else:
    return "OK!"

def check_ram(available_ram):
  if available_ram < 2:
    return "CRITICAL"
  elif available_ram >= 2 and available_ram < 4:
    return "WARNING"
  else:
    return "NORMAL"

def cpu_usage(cpu_percent):
  if cpu_percent >= 90:
    return "CRITICAL"
  elif cpu_percent >= 70 and cpu_percent < 90:
    return "WARNING"
  else:
    return "NORMAL"

print("Checking. . . .")

while True:
 now = datetime.now()
 f_time = now.strftime("%d-%m-%Y %H:%M:%S")
 result = subprocess.run(
    ["free", "-m"],
    capture_output = True,
    text = True
    )
 try:
  lines = result.stdout.splitlines()
  ram = lines[1].split()
  available_ram = float(ram[6])
  available_ram = available_ram / 1024
  total_ram = float(ram[1]) / 1024
  used_ram = float(ram[2]) / 1024
  status = check_ram(available_ram)
 except (IndexError, ValueError):
   total_ram = "?"
   status = "?"
   available_ram = "?"
   used_ram = "?"

 cpu = subprocess.run(
    ["top", "-bn1"],
    capture_output = True,
    text = True
 )
 cpu_lines = cpu.stdout.splitlines()
 cpu_status = cpu_lines[2].replace(",", ", ").split()
 for index, value in enumerate(cpu_status):
    if value == "id,":
        idle = cpu_status[index - 1]

 try:
  cpu_percent = 100 - float(idle)
  cpu_state = cpu_usage(cpu_percent)
 except ValueError:
  cpu_percent = "?"
  cpu_state = "?"

 disk = subprocess.run(
    ["df", "-h", "/"],
    capture_output = True,
    text = True
 )
 try:
  disk_lines = disk.stdout.splitlines()
  disk_usage = disk_lines[1].split()
  disk_percent = disk_usage[4]
  disk_percent = disk_percent.replace("%", "")
 except IndexError:
    disk_percent = "Unknown"

 try:
   disk_percent = int(disk_percent)
   disk_status = check_disk(disk_percent)
 except ValueError:
   disk_percent = "?"
   disk_status = "?"

 print(f"TIME:{f_time}")
 print("=========================================")
 print(f"Available RAM: {available_ram:.2f} GiB")
 print("-----------------------------------------")
 print(f"RAM Status: {status}")
 print("-----------------------------------------")
 print(f"Total RAM: {total_ram:.2f} GiB")
 print("-----------------------------------------")
 print(f"Used RAM: {used_ram:.2f} GiB")
 print("-----------------------------------------")
 print(f"CPU Usage: {cpu_percent:.2f} %")
 print("-----------------------------------------")
 print(f"CPU Status: {cpu_state}")
 print("-----------------------------------------")
 print(f"Disk Usage: {disk_percent}%")
 print("-----------------------------------------")
 print(f"Disk Status: {disk_status}")
 print("=========================================")
 print(" ")

 with open("Server_log.txt", "a") as file:
  file.write("=========================================\n")
  file.write(f"TIME:{f_time}\n")
  file.write("-----------------------------------------\n")
  file.write(f"CPU Usage: {cpu_percent:.2f} %  |  STATUS:{cpu_state}\n")
  file.write("-----------------------------------------\n")
  file.write(f"Available RAM: {available_ram:.2f} GiB  |  Total RAM: {total_ram:.2f} GiB  |  RAM Status: {status}\n")
  file.write("-----------------------------------------\n")
  file.write(f"Disk Usage: {disk_percent}%  |  Disk Status: {disk_status}\n")
  file.write("=========================================\n")
  file.write(" \n")
 time.sleep(10)