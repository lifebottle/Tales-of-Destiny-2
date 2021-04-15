# coding=utf8

### Start Code by pnvnd, double-check code! ###
t = open("C:/tod2/00019.bin", "r")
rstone = t.read()
big_ass_array = list(rstone)
t.close()
### End Code by pnvnd, double-check code! ###


### Start Code by Ethanol ###
output = ""
table_name = 'dump.tbl'

for index in range(len(big_ass_array)):

    lower_byte = (index % 0xBB)
    upper_byte = int(((index - lower_byte) / 0xBB) + 0x99)

    lower_byte = lower_byte + 0x40

    if lower_byte >= 0x5D:
        lower_byte = lower_byte + 0x01
    if lower_byte >= 0x80:
        lower_byte = lower_byte + 0x01
    if upper_byte >= 0xA0:
        upper_byte = upper_byte + 0x40

    resulting_character = (upper_byte << 8) | lower_byte
    
    output += format(resulting_character, 'X') + "=" + str(big_ass_array[index]) + "\n"
    #print(hex(resulting_character) + "=" + str(big_ass_array[index]))

with open(table_name, 'w', encoding='utf8') as f:
    f.write(output)
### End Code by Ethanol ###