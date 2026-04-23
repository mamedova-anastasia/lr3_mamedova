import unittest
import os
from unittest.mock import patch

def get_frame_status(burst_count, threshold, is_attack, ftype):
    if ftype == 'DEAUTH' and is_attack:
        if burst_count >= threshold:
            return 'BLOCKED'
        else:
            return 'WARN'
    else:
        return 'OK'

class TestWiFiSnifferLogic(unittest.TestCase):
    def test_normal_traffic_ok(self): # проверка нормального трафика
        status = get_frame_status(0, 3, False, 'DATA')
        self.assertEqual(status, 'OK')

    def test_deauth_warn_threshold_not_reached(self): # проверка деаутентификации
        status = get_frame_status(1, 3, True, 'DEAUTH')
        self.assertEqual(status, 'WARN')

    def test_deauth_blocked_threshold_reached(self): # проверка блокировки
        status = get_frame_status(3, 3, True, 'DEAUTH')
        self.assertEqual(status, 'BLOCKED')

    def test_deauth_blocked_threshold_exceeded(self): # проверка превышения порога
        status = get_frame_status(5, 3, True, 'DEAUTH')
        self.assertEqual(status, 'BLOCKED')

    def test_reset_on_normal_frame(self): # проверка сброса при нормальном кадре
        status = get_frame_status(2, 3, False, 'DEAUTH')
        self.assertEqual(status, 'OK')

class TestEnvironmentConfig(unittest.TestCase): # проверка переменных окружения
    @patch.dict(os.environ, {'Deauth_threshold': '5'}, clear=True)
    def test_read_threshold_from_env(self): # проверка чтения порога из переменных окружения
        threshold = int(os.environ.get('Deauth_threshold', '3'))
        self.assertEqual(threshold, 5)

    def test_default_threshold_when_not_set(self): # проверка значения по умолчанию
        if 'Deauth_threshold' in os.environ:
            del os.environ['Deauth_threshold']
        threshold = int(os.environ.get('Deauth_threshold', '3'))
        self.assertEqual(threshold, 3)

    @patch.dict(os.environ, {}, clear=True)
    def test_default_ap_mac(self): # проверка значения по умолчанию для MAC
        ap_mac = os.environ.get('AP_MAC', 'AA:BB:CC:DD:EE:FF')
        self.assertEqual(ap_mac, 'AA:BB:CC:DD:EE:FF')

if __name__ == '__main__':
    unittest.main()