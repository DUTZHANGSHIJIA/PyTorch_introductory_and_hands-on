char_set = set()    #创建集合，集合可自动去重
for title in academy_titles:
    for char in title:
        char_set.add(char)
