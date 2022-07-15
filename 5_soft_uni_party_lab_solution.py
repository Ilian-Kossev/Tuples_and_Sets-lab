n = int(input())
invited_guests_record = set()
for _ in range(n):
    guest = input()
    invited_guests_record.add(guest)
command = input()
while not command == 'END':
    if command in invited_guests_record:
        invited_guests_record.remove(command)
    command = input()
print(len(invited_guests_record))


n = int(input())
guest_list = {input() for _ in range(n)}
while True:
    command = input()
    if command == 'END':
        break
    guest_list.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


vip_guest = sorted([g for g in guest_list if is_vip(g)])
regular_guest = sorted([g for g in guest_list if not is_vip(g)])
[print(g) for g in vip_guest]
[print(g) for g in regular_guest]