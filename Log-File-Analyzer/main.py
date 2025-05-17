from log_parser import analyze_logs

def print_summary(analysis):
    if not analysis:
        return

    print(f"📊 Total Logs: {analysis['total_logs']}")
    print("\n🔸 Log Levels Count:")
    for level, count in analysis['log_counts'].items():
        print(f"  {level}: {count}")

    if analysis['ip_activity']:
        most_active_ip = analysis['ip_activity'].most_common(1)[0]
        print(f"\n🔸 Most Active IP: {most_active_ip[0]} ({most_active_ip[1]} times)")
    else:
        print("\n🔸 No IP activity found.")

    if analysis['error_messages']:
        most_common_error = analysis['error_messages'].most_common(1)[0]
        print(f"\n🔸 Most Common Error: '{most_common_error[0]}' ({most_common_error[1]} times)")
    else:
        print("\n🔸 No ERROR logs found.")

if __name__ == "__main__":
    file_path = 'sample_log.txt'
    analysis = analyze_logs(file_path)
    print_summary(analysis)
