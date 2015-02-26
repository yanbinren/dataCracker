path_in1 = 'rec_log_train_pre_3.txt'
path_in2 = '../track1/user_profile.txt'
path_in3 = '../track1/user_key_word.txt'
path_in4 = '../track1/user_sns.txt'
path_in5 = '../track1/user_action.txt'

file_in1 = open(path_in1, "r")
userID = set([])
for line in file_in1:
    l = line.split()
    i = 0
    while i<len(l):
        userID.add(l[i])
        i = i+4
file_in1.close()
print "file 1"
g1 = set([])
g2 = set([])
g3 = set([])
g4 = set([])
g5 = set([])
g6 = set([])
g7 = set([])
g8 = set([])
g9 = set([])
g10 = set([])
g11 = set([])
g12 = set([])
g13 = set([])
file_in2 = open(path_in2, "r")
for line in file_in2:
    l = line.split()
    try:
        age = 2012 - int(l[1])
    except ValueError:
        age = -1
    gender = int(l[2])
    if l[0] in userID:
        if gender == 0 or age == -1:
		    g13.add(l[0])
        elif gender == 1 and age >= 0 and age <= 15:
    	    g1.add(l[0])
        elif gender == 2 and age >= 0 and age <= 15:
            g2.add(l[0])
        elif gender == 1 and age > 15 and age <= 20:
            g3.add(l[0])
        elif gender == 2 and age > 15 and age <= 20:
            g4.add(l[0])
        elif gender == 1 and age > 20 and age <= 25:
            g5.add(l[0])
        elif gender == 2 and age > 20 and age <= 25:
            g6.add(l[0])
        elif gender == 1 and age > 25 and age <= 30:
            g7.add(l[0])
        elif gender == 2 and age > 25 and age <= 30:
            g8.add(l[0])
        elif gender == 1 and age > 30 and age <= 45:
            g9.add(l[0])
        elif gender == 2 and age > 30 and age <= 45:
            g10.add(l[0])
        elif gender == 1 and age > 45:
            g11.add(l[0])
        elif gender == 2 and age > 45:
            g12.add(l[0])
file_in2.close()

file_in5 = open(path_in5, "r")
user_action_file1 = open('preprocessing/user_action_1.txt', "w")
user_action_file2 = open('preprocessing/user_action_2.txt', "w")
user_action_file3 = open('preprocessing/user_action_3.txt', "w")
user_action_file4 = open('preprocessing/user_action_4.txt', "w")
user_action_file5 = open('preprocessing/user_action_5.txt', "w")
user_action_file6 = open('preprocessing/user_action_6.txt', "w")
user_action_file7 = open('preprocessing/user_action_7.txt', "w")
user_action_file8 = open('preprocessing/user_action_8.txt', "w")
user_action_file9 = open('preprocessing/user_action_9.txt', "w")
user_action_file10 = open('preprocessing/user_action_10.txt', "w")
user_action_file11 = open('preprocessing/user_action_11.txt', "w")
user_action_file12 = open('preprocessing/user_action_12.txt', "w")
user_action_file13 = open('preprocessing/user_action_13.txt', "w")
for line in file_in5:
    l = line.split()
    if l[1] not in userID:
        continue
    if l[0] in g1:
        user_action_file1.write(line)
    elif l[0] in g2:
        user_action_file2.write(line)
    elif l[0] in g3:
        user_action_file3.write(line)
    elif l[0] in g4:
        user_action_file4.write(line)
    elif l[0] in g5:
        user_action_file5.write(line)
    elif l[0] in g6:
        user_action_file6.write(line)
    elif l[0] in g7:
        user_action_file7.write(line)
    elif l[0] in g8:
        user_action_file8.write(line)
    elif l[0] in g9:
        user_action_file9.write(line)
    elif l[0] in g10:
        user_action_file10.write(line)
    elif l[0] in g11:
        user_action_file11.write(line)
    elif l[0] in g12:
        user_action_file12.write(line)
    elif l[0] in g13:
        user_action_file13.write(line)
file_in5.close()
user_action_file1.close()
user_action_file2.close()
user_action_file3.close()
user_action_file4.close()
user_action_file5.close()
user_action_file6.close()
user_action_file7.close()
user_action_file8.close()
user_action_file9.close()
user_action_file10.close()
user_action_file11.close()
user_action_file12.close()
user_action_file13.close()

print "file 2"
#sclice rec_log_train.txt
file_in1 = open(path_in1, "r")
rec_log_train_file1 = open('preprocessing/rec_log_train_1.txt', "w")
rec_log_train_file2 = open('preprocessing/rec_log_train_2.txt', "w")
rec_log_train_file3 = open('preprocessing/rec_log_train_3.txt', "w")
rec_log_train_file4 = open('preprocessing/rec_log_train_4.txt', "w")
rec_log_train_file5 = open('preprocessing/rec_log_train_5.txt', "w")
rec_log_train_file6 = open('preprocessing/rec_log_train_6.txt', "w")
rec_log_train_file7 = open('preprocessing/rec_log_train_7.txt', "w")
rec_log_train_file8 = open('preprocessing/rec_log_train_8.txt', "w")
rec_log_train_file9 = open('preprocessing/rec_log_train_9.txt', "w")
rec_log_train_file10 = open('preprocessing/rec_log_train_10.txt', "w")
rec_log_train_file11 = open('preprocessing/rec_log_train_11.txt', "w")
rec_log_train_file12 = open('preprocessing/rec_log_train_12.txt', "w")
rec_log_train_file13 = open('preprocessing/rec_log_train_13.txt', "w")
for line in file_in1:
    l = line.split()
    i = 0
    while i<len(l)-3:
        if l[i] in g1:
            rec_log_train_file1.write(" ".join(l[i:i+4]))
            rec_log_train_file1.write("\n")
        elif l[i] in g2:
            rec_log_train_file2.write(" ".join(l[i:i+4]))
            rec_log_train_file2.write("\n")
        elif l[i] in g3:
            rec_log_train_file3.write(" ".join(l[i:i+4]))
            rec_log_train_file3.write("\n")
        elif l[i] in g4:
            rec_log_train_file4.write(" ".join(l[i:i+4]))
            rec_log_train_file4.write("\n")
        elif l[i] in g5:
            rec_log_train_file5.write(" ".join(l[i:i+4]))
            rec_log_train_file5.write("\n")
        elif l[i] in g6:
            rec_log_train_file6.write(" ".join(l[i:i+4]))
            rec_log_train_file6.write("\n")
        elif l[i] in g7:
            rec_log_train_file7.write(" ".join(l[i:i+4]))
            rec_log_train_file7.write("\n")
        elif l[i] in g8:
            rec_log_train_file8.write(" ".join(l[i:i+4]))
            rec_log_train_file8.write("\n")
        elif l[i] in g9:
            rec_log_train_file9.write(" ".join(l[i:i+4]))
            rec_log_train_file9.write("\n")
        elif l[i] in g10:
            rec_log_train_file10.write(" ".join(l[i:i+4]))
            rec_log_train_file10.write("\n")
        elif l[i] in g11:
            rec_log_train_file11.write(" ".join(l[i:i+4]))
            rec_log_train_file11.write("\n")
        elif l[i] in g12:
            rec_log_train_file12.write(" ".join(l[i:i+4]))
            rec_log_train_file12.write("\n")
        elif l[i] in g13:
            rec_log_train_file13.write(" ".join(l[i:i+4]))
            rec_log_train_file13.write("\n")
        i =  i + 4
file_in1.close()
rec_log_train_file1.close()
rec_log_train_file2.close()
rec_log_train_file3.close()
rec_log_train_file4.close()
rec_log_train_file5.close()
rec_log_train_file6.close()
rec_log_train_file7.close()
rec_log_train_file8.close()
rec_log_train_file9.close()
rec_log_train_file10.close()
rec_log_train_file11.close()
rec_log_train_file12.close()
rec_log_train_file13.close()
print "file 3"
#slice key word file
file_in3 = open(path_in3, "r")
user_key_word_file1 = open('preprocessing/user_key_word_1.txt', "w")
user_key_word_file2 = open('preprocessing/user_key_word_2.txt', "w")
user_key_word_file3 = open('preprocessing/user_key_word_3.txt', "w")
user_key_word_file4 = open('preprocessing/user_key_word_4.txt', "w")
user_key_word_file5 = open('preprocessing/user_key_word_5.txt', "w")
user_key_word_file6 = open('preprocessing/user_key_word_6.txt', "w")
user_key_word_file7 = open('preprocessing/user_key_word_7.txt', "w")
user_key_word_file8 = open('preprocessing/user_key_word_8.txt', "w")
user_key_word_file9 = open('preprocessing/user_key_word_9.txt', "w")
user_key_word_file10 = open('preprocessing/user_key_word_10.txt', "w")
user_key_word_file11 = open('preprocessing/user_key_word_11.txt', "w")
user_key_word_file12 = open('preprocessing/user_key_word_12.txt', "w")
user_key_word_file13 = open('preprocessing/user_key_word_13.txt', "w")
for line in file_in3:
    l = line.split()
    if l[0] in g1:
        user_key_word_file1.write(line)
    elif l[0] in g2:
        user_key_word_file2.write(line)
    elif l[0] in g3:
        user_key_word_file3.write(line)
    elif l[0] in g4:
        user_key_word_file4.write(line)
    elif l[0] in g5:
        user_key_word_file5.write(line)
    elif l[0] in g6:
        user_key_word_file6.write(line)
    elif l[0] in g7:
        user_key_word_file7.write(line)
    elif l[0] in g8:
        user_key_word_file8.write(line)
    elif l[0] in g9:
        user_key_word_file9.write(line)
    elif l[0] in g10:
        user_key_word_file10.write(line)
    elif l[0] in g11:
        user_key_word_file11.write(line)
    elif l[0] in g12:
        user_key_word_file12.write(line)
    elif l[0] in g13:
        user_key_word_file13.write(line)
file_in3.close()
user_key_word_file1.close()
user_key_word_file2.close()
user_key_word_file3.close()
user_key_word_file4.close()
user_key_word_file5.close()
user_key_word_file6.close()
user_key_word_file7.close()
user_key_word_file8.close()
user_key_word_file9.close()
user_key_word_file10.close()
user_key_word_file11.close()
user_key_word_file12.close()
user_key_word_file13.close()
print "file 4"
#slice sns file
file_in4 = open(path_in4, "r")
user_sns_file1 = open('preprocessing/user_sns_1.txt', "w")
user_sns_file2 = open('preprocessing/user_sns_2.txt', "w")
user_sns_file3 = open('preprocessing/user_sns_3.txt', "w")
user_sns_file4 = open('preprocessing/user_sns_4.txt', "w")
user_sns_file5 = open('preprocessing/user_sns_5.txt', "w")
user_sns_file6 = open('preprocessing/user_sns_6.txt', "w")
user_sns_file7 = open('preprocessing/user_sns_7.txt', "w")
user_sns_file8 = open('preprocessing/user_sns_8.txt', "w")
user_sns_file9 = open('preprocessing/user_sns_9.txt', "w")
user_sns_file10 = open('preprocessing/user_sns_10.txt', "w")
user_sns_file11 = open('preprocessing/user_sns_11.txt', "w")
user_sns_file12 = open('preprocessing/user_sns_12.txt', "w")
user_sns_file13 = open('preprocessing/user_sns_13.txt', "w")
for line in file_in4:
    l = line.split()
    if l[1] not in userID:
        continue
    if l[0] in g1:
        user_sns_file1.write(line)
    elif l[0] in g2:
        user_sns_file2.write(line)
    elif l[0] in g3:
        user_sns_file3.write(line)
    elif l[0] in g4:
        user_sns_file4.write(line)
    elif l[0] in g5:
        user_sns_file5.write(line)
    elif l[0] in g6:
        user_sns_file6.write(line)
    elif l[0] in g7:
        user_sns_file7.write(line)
    elif l[0] in g8:
        user_sns_file8.write(line)
    elif l[0] in g9:
        user_sns_file9.write(line)
    elif l[0] in g10:
        user_sns_file10.write(line)
    elif l[0] in g11:
        user_sns_file11.write(line)
    elif l[0] in g12:
        user_sns_file12.write(line)
    elif l[0] in g13:
        user_sns_file13.write(line)
file_in4.close()
user_sns_file1.close()
user_sns_file2.close()
user_sns_file3.close()
user_sns_file4.close()
user_sns_file5.close()
user_sns_file6.close()
user_sns_file7.close()
user_sns_file8.close()
user_sns_file9.close()
user_sns_file10.close()
user_sns_file11.close()
user_sns_file12.close()
user_sns_file13.close()
#slice user_action




