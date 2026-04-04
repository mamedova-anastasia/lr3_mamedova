# Контейнер мониторинга ARP-трафика 

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import random

# НАСТРОЙКИ
printer_ips = ['192.168.1.100', '192.168.1.101', '192.168.1.102']

# Ожидаемые MAC для принтеров (эталон)
expected_macs = {
    '192.168.1.100': '00:11:22:33:44:55',
    '192.168.1.101': '66:77:88:99:AA:BB',
    '192.168.1.102': 'CC:DD:EE:FF:00:11'
}

# Хранилище данных
detected_packets = []
attack_log = []

# ========== ФУНКЦИЯ ЭМУЛЯЦИИ ПАКЕТОВ ==========
def emulate_arp_packets(num_packets=50):
    """
    Эмулирует получение ARP-пакетов от принтеров.
    Часть пакетов — легитимные, часть — атаки (подмена MAC).
    """
    for i in range(num_packets):
        # Выбираем случайный принтер
        printer_ip = random.choice(printer_ips)

        # С вероятностью 30% генерируем атаку (подменённый MAC)
        is_attack = random.random() < 0.3

        if is_attack:
            # Генерируем случайный поддельный MAC
            fake_mac = ':'.join(f'{random.randint(0,255):02X}' for _ in range(6))
            src_mac = fake_mac
        else:
            # Берём правильный MAC
            src_mac = expected_macs[printer_ip]

        data = {
            'timestamp': datetime.now().isoformat(),
            'src_ip': printer_ip,
            'src_mac': src_mac,
            'target_ip': '192.168.1.1',  # шлюз
            'operation': random.choice(['is-at', 'who-has']),
            'is_attack': is_attack
        }

        detected_packets.append(data)

        if is_attack:
            attack_log.append(data)
            print(f'[ATTACK] {printer_ip} объявил MAC {src_mac} (ожидался {expected_macs[printer_ip]})')
        else:
            print(f'[OK] {printer_ip} -> MAC {src_mac}')

# ========== ВИЗУАЛИЗАЦИЯ ==========
def show_tables_and_charts():
    if not detected_packets:
        print("Нет данных")
        return

    df = pd.DataFrame(detected_packets)

    print("\n" + "="*60)
    print("ТАБЛИЦА 1: Обнаруженные ARP-пакеты")
    print("="*60)
    print(df[['timestamp', 'src_ip', 'src_mac', 'operation', 'is_attack']].to_string())

    print("\n" + "="*60)
    print("ТАБЛИЦА 2: Статистика по принтерам")
    print("="*60)
    printer_stats = df.groupby('src_ip').size().reset_index(name='packet_count')
    print(printer_stats)

    if attack_log:
        df_attacks = pd.DataFrame(attack_log)
        print("\n" + "="*60)
        print("ТАБЛИЦА 3: Зафиксированные атаки")
        print("="*60)
        attack_summary = df_attacks.groupby(['src_ip', 'src_mac']).size().reset_index(name='count')
        print(attack_summary)

    # ГРАФИК 1: Количество пакетов по принтерам
    plt.figure(figsize=(10, 6))
    counts = df['src_ip'].value_counts()
    plt.bar(counts.index, counts.values, color='skyblue', edgecolor='black')
    plt.xlabel('IP принтера')
    plt.ylabel('Количество пакетов')
    plt.title('Статистика ARP-пакетов по принтерам')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('printer_stats.png')

    # ГРАФИК 2: Атаки vs легитимные пакеты
    plt.figure(figsize=(8, 6))
    attack_count = len(attack_log)
    legit_count = len(detected_packets) - attack_count
    plt.pie([legit_count, attack_count], 
            labels=['Легитимные', 'Атаки'],
            autopct='%1.1f%%',
            colors=['green', 'red'],
            explode=(0, 0.1))
    plt.title('Соотношение легитимных пакетов и атак')
    plt.savefig('attacks_pie.png')

    # ГРАФИК 3: Количество атак по принтерам
    plt.figure(figsize=(10, 6))
    if attack_log:
        attack_counts = Counter([a['src_ip'] for a in attack_log])
        plt.bar(attack_counts.keys(), attack_counts.values(), color='red', edgecolor='black')
        plt.xlabel('IP принтера')
        plt.ylabel('Количество атак')
        plt.title('Атаки по принтерам')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('attacks_by_printer.png')



print('='*60)
print('КОНТЕЙНЕР МОНИТОРИНГА ARP-ТРАФИКА (ЭМУЛЯЦИЯ)')
print('Для лабораторной работы по УЖЦИС')
print('='*60)
print('\nЭмулируем получение ARP-пакетов от принтеров...\n')

emulate_arp_packets(num_packets=50)

show_tables_and_charts()

