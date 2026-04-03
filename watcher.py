# контейнер мониторинга, который будет перехватывать ARP-пакеты и отправлять их на проверку в контейнер decision-engine
from scapy.all import sniff, ARP
import requests
import os
import json
from datetime  import datetime

# Адрес контейнера, который будет проверять ARP-пакеты
decision_engine_url = os.getenv ('DECISION_ENGINE_URL', 'http://decision-engine:8080/check')

# IP-адреса принтеров
printer_ips = ['192.168.1.100', '192.168.1.101', '192.168.1.102']

def send_to_engine(packet_data):
  try:
     response = requests.post(decision_engine_url, json=packet_data, timeout=1)
     print(f'Sent to engine, status: {response.status_code}')
  except  Exception as e: 
     print(f'Fail to send: {e}')

def handle_arp(packet):
  
  # Если отправитель пакета в списке принтеров
  if packet.haslayer(ARP):
     arp = packet[ARP]

     if arp.psrc in printer_ips:
       data = {
         'timestamp': datetime.now().isoformat(),
         'src_ip': arp.psrc,
         'src_mac': arp.hwsrc,
         'target_ip': arp.pdst,
         'operation': 'is-at' if arp.op == 2 else 'who-has'
       }
       print(f'Detected ARP packet: {data}')
       send_to_engine(data)

# Запуск сниффера
print('ARP watcher started. Monitoring printers...')
sniff(prn=handle_arp, filter='arp', store=0)