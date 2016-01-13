name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count_dict = dict()
for line in handle:
    if not line.startswith("From "): continue
    time = line.split()[5]
    hour = time.split(":")[0]
    count_dict[hour] = count_dict.get(hour, 0) + 1

for hr, count in sorted(count_dict.items()):
    print hr, count
