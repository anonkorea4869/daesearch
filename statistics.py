def isExistenceKeyword(list, search_key):
    for dictionary in list:
        if search_key in dictionary:
            return True
    return False

def isExistenceNextKeyword(dictionary_list, search_key, search_next_key):
    pass

def insertNextKeywordCount(dictionary_list, search_key, search_next_key):
    pass

def plusNextKeywordCount(list, search_key, search_next_key) :
    pass

with open("regex.txt", "r") as file:
    lines = [line.rstrip()[1:] for line in file]

# lines = "/frontend/frontend/register.css"

# [{"frontend" : [{"css" : 1}, {"js" : 2}]}, {"backend" : [{"php" : 1}, {"jsp" : 2}]}]
path_dict_list = [{"frontend" : [{"css" : 1}]}]

for line in lines :
    path_list = line.split("/")

    # 마지막 키워드는 안함
    for i in range(len(path_list) -1) :
        # print(path_list[i], end=" -> ")

        keyword = path_list[i]
        next_keyword = path_list[i+1]

        # 해당 키워드가 리스트에 존재 하는지
        if not isExistenceKeyword(path_dict_list, keyword): # 없으면
            path_dict_list.append({keyword : []}) # 새로운 리스트 추가
    
        # 다음 키워드가 해당 dict의 리스트에 있는지
        if isExistenceNextKeyword(path_dict_list, keyword, next_keyword) : # 있으면
            # path_dict_list = plusNextKeywordCount(path_dict_list, keyword, next_keyword)
            print(keyword, next_keyword, "있습니다.")
        else : # 없으면
            # path_dict_list = insertNextKeywordCount(path_dict_list, keyword, next_keyword)
            print(keyword, next_keyword, "없습니다.")

        print(path_dict_list)
        print()