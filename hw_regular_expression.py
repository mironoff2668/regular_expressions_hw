from pprint import pprint
import re
import csv


with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)


correct_list = []
for contact in contact_list:
    name = ' '.join(contact[0:3]).split(' ')
    contact[0:3] = name[0:3]
    pattern_num = r'(\+7|8)?(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})' \
                  r'(\-*)(\d{2})(\-*)(\d{2})(\s*)(\(*)' \
                  r'(доб)*(\.*)(\s*)(\d+)*(\)*)'
    substitusion_num = r'+7(\4)\8-\10-\12\13\15\16\18'
    result = re.sub(pattern_num, substitusion_num, contact[5])
    contact[5] = result
    correct_list.append(contact)



contacts = {}
for i in correct_list:
    if i[0] not in contacts:
        contacts[i[0]] = i[1:]
# print(contacts.values())


# pprint(contacts.items())
# result = '; '.join(f'{key.capitalize()} {value}' for key, value in contacts.items()).split(',')
#
# finish = []
# finish.append(result)

# correct_list = [f'{key}, {value}' for key, value in contacts.items()]
# pprint(correct_list)
#
# pprint(correct_list)


with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')

    # Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts.items())
