def seven(a):
    a_dict = {}
    count_i = 0
    last_point = (0, 0)
    for i in a:
        count_i += 1
        last_space = 0
        a_dict.clear()
        for j in range(len(i)):
            if i[j] == " " or j == len(i) - 1:
                if last_space == 0:
                    temp = i[last_space : j]
                else:
                    temp = i[last_space + 1: j]
                last_space = j
                if temp.lower() in a_dict.keys():
                    a_dict[temp.lower()] += 1
                else:
                    a_dict[temp.lower()] = 1
            if i[j] == "." or i[j] == "?" or i[j] == "!":
                word = max(a_dict, key=a_dict.get)
                print(word)
                temp_i, temp_j = last_point
                if count_i - 1 > temp_i:
                    temp_str = a[temp_i]
                    temp_s = temp_str[temp_j:]
                    i_of_word = 0
                    while i_of_word != -1:
                        i_of_word = temp_s.find(word.lower())
                        if i_of_word + 1 == " " and i_of_word == 0 or i_of_word + 1 == " " and i_of_word - 1 == " ":
                            temp_s = temp_s[:i_of_word] + temp_s[i_of_word + len(word):]
                    a[temp_i] = temp_str[:temp_j] + temp_s
                    temp_i += 1
                    while count_i != temp_i:
                        temp_s = a[temp_i]
                        i_of_word = 0
                        while i_of_word != -1:
                            i_of_word = temp_s.find(word)
                            if i_of_word + 1 == " " and i_of_word == 0 or i_of_word + 1 == " " and i_of_word - 1 == " ":
                                temp_s = temp_s[:i_of_word] + temp_s[i_of_word + len(word):]
                        a[temp_i] = temp_s
                        temp_i += 1
                if temp_i == count_i - 1:
                    temp_s = i[temp_j : j]
                    i_of_word = 0
                    while i_of_word <= j:
                        i_of_word = temp_s.find(word)
                        if i_of_word + 1 == " " and i_of_word == 0 or i_of_word + 1 == " " and i_of_word - 1 == " ":
                            temp_s = temp_s[:i_of_word] + temp_s[i_of_word + len(word):]
                    a[temp_i] = temp_s
    return a

ar = ["И сказал воин и да.",
      "Что же ты сделал то ты такое."]
temp = seven(ar)
print(temp)

