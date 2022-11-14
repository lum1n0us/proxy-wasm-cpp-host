#!/usr/bin/env python3

import os
import pprint
import re
import sys

def collect_data(log_path):
    content = []
    vm_p = re.compile("(Vm\S+):\s+(\d+) kB")
    rss_p = re.compile("(Rss\S+):\s+(\d+) kB")

    with open(log_path, "r") as f:
        current_catch = ""
        current_catch_content = {}
        for line in f:
            line = line.strip()

            if line.startswith("==> ") or line.startswith("[MEM]"):
                space_idx = line.find(" ")
                current_catch = line[space_idx + 1:]
                current_catch = current_catch.lower()
                current_catch_content = {}
            elif line == "==========":
                assert(current_catch)

                content.append([current_catch, current_catch_content])
            elif line.startswith("Vm"):
                m = re.match(vm_p, line)
                assert(m)

                k, v = m.groups()
                current_catch_content[k] = int(v)
            elif line.startswith("Rss"):
                m = re.match(rss_p, line)
                assert(m)

                k, v = m.groups()
                current_catch_content[k] = int(v)
            else:
                pass

    return content

def calculate_delta(data):
    """
    add columes
    """
    data_w_delta = []

    prev = ["", {}]
    for i in range(len(data)):
        # [tag, {data of the row}]
        cur = data[i]
        cur_mod = [cur[0], {}]

        for k in cur[1].keys():
            cur_v = cur[1].get(k, 0)
            prev_v = prev[1].get(k, 0)

            cur_mod[1][k] = cur_v
            cur_mod[1][k+"_delta"] = cur_v - prev_v

        prev = cur
        data_w_delta.append(cur_mod)

    return data_w_delta

def write_report(data):
    interested = ["VmRSS", "VmRSS_delta", "RssAnon", "RssAnon_delta", "RssFile", "VmSize", "VmData", "VmExe", "VmStk", "VmLib"]

    keys_data = data[0][1].keys()

    # header
    content = "| |"
    content += "|".join([f"{s}(kB)" for s in interested if s in keys_data])
    content += "|"
    content += os.linesep

    # separator
    content += "| --"
    content += "| -- " * len(keys_data)
    content += "|"
    content += os.linesep

    # summary
    for chk_info in data:
        # chk_info is in a form likes: [tag, {info}]
        content += f"|{chk_info[0]}|"
        content += "|".join(str(chk_info[1][k]) for k in interested if k in keys_data)
        content += "|"
        content += os.linesep

    return content

def main():
    log_path = sys.argv[1]

    print(f"processing {log_path}...\n\n")

    status_data = collect_data(log_path)

    data_w_deleta = calculate_delta(status_data)
    # pprint.pprint(status_data)

    content = write_report(data_w_deleta)
    print(content)

    print("Done")

    return 0

if __name__ == "__main__":
    sys.exit(main())
