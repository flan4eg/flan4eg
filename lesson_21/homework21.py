from datetime import datetime


def heartbeating_sample_analize(input_file='hblog.txt', output_file='hb_test.log'):
    key_value = "Key TSTFEED0300|7E3E|0400"
    timestamps = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if key_value in line:
                timestamp_index = line.find("Timestamp ")
                if timestamp_index != -1:
                    time_str = line[timestamp_index + len("Timestamp "): timestamp_index + len("Timestamp ") + 8]
                    ts = datetime.strptime(time_str, "%H:%M:%S")
                    timestamps.append((ts, line.strip()))

    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(f"- Heartbeat Analysis for {key_value} -\n")

        for i in range(len(timestamps) - 1):
            current_time, current_line = timestamps[i]
            next_time, next_line = timestamps[i + 1]

            diff = next_time - current_time
            diff_seconds = diff.total_seconds()

            if 31 < diff_seconds < 33:
                out.write(
                    f"[WARNING] There may be a malfunction in the cardiac monitoring system at {current_time.strftime('%H:%M:%S')} (diff={diff_seconds:.1f}s)\n"
                    f"Line: {current_line}\n"
                )

            elif diff_seconds >= 33:
                out.write(
                    f"[ERROR] Heartbeat is missed at {current_time.strftime('%H:%M:%S')} (diff={diff_seconds:.1f}s)\n"
                    f"Line: {current_line}\n"
                )

    print()
    print(f"Result is saved to '{output_file}'")


if __name__ == "__main__":
    heartbeating_sample_analize()
