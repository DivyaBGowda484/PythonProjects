import re
from collections import Counter
from datetime import datetime

def parse_log_line(line):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+?)(?: from (\d{1,3}(?:\.\d{1,3}){3}))?$'
    match = re.match(pattern, line)
    if match:
        timestamp_str, log_level, message, ip_address = match.groups()
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        return {
            'timestamp': timestamp,
            'level': log_level,
            'message': message.strip(),
            'ip': ip_address
        }
    return None

def analyze_logs(file_path):
    log_counts = Counter()
    ip_activity = Counter()
    error_messages = Counter()
    total_logs = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                log_entry = parse_log_line(line)
                if log_entry:
                    total_logs += 1
                    log_counts[log_entry['level']] += 1
                    if log_entry['ip']:
                        ip_activity[log_entry['ip']] += 1
                    if log_entry['level'] == 'ERROR':
                        error_messages[log_entry['message']] += 1
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return None

    return {
        'total_logs': total_logs,
        'log_counts': log_counts,
        'ip_activity': ip_activity,
        'error_messages': error_messages
    }
