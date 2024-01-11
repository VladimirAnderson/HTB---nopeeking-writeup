part_one = [0x301, 0x3F5, 0x3A0, 0x369, 0x3DF, 0x364, 0x35D, 0x33F, 0x38B, 0x34F, 0x31E,0x327, 0x3AE]            # each value have increased 
part_two = [0x361 ,0x340 ,0x315 ,0x376 ,0x310 ,0x3F8 ,0x340 ,0x3AA ,0x3BB ,0x3A4, 0x39F, 0x34F, 0x32B]           # on the 0x300
gamma = [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]

encr_flag = []
idx_p2 = 0
idx_p1 = 0

for i in range(len(part_one) + len(part_two)):

    if gamma[i] == 0:
        encr_flag.append(part_two[idx_p2])
        idx_p2 += 1
        
    elif gamma[i] == 1:
         encr_flag.append(part_one[idx_p1])
         idx_p1 += 1
        
        
i = 0 
index = 0
flag = ""

for i in range(len(encr_flag)):
    flag += chr((( encr_flag[i] ^ ( (0x2c * index )%0x100 )) - 0x1a + index + 1 ) % 0x100)
    index += 1
print(flag)
