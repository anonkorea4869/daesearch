def isExistenceKeyword(dictionary_list, search_key):
    for dictionary in dictionary_list :
        if search_key in dictionary :
            return True

    return False

def isExistenceNextKeyword(dictionary_list, search_key, search_next_key):
    for dictionary in dictionary_list :
        if search_key in dictionary :
            sub_dictionary = dictionary[search_key]
            if search_next_key in sub_dictionary.keys() :
                return True

    return False
        

def insertNextKeywordCount(dictionary_list, search_key, search_next_key):
    for dictionary in dictionary_list :
        if search_key in dictionary :
            dictionary[search_key].update({search_next_key: 1})
            break
    
    return dictionary_list
        

def plusNextKeywordCount(dictionary_list, search_key, search_next_key) :
    for dictionary in dictionary_list :
        if search_key in dictionary :
            dictionary[search_key][search_next_key] += 1
    
    return dictionary_list

with open("regex.txt", "r") as file:
    lines = [line.rstrip()[1:] for line in file]

path_dict_list = []

for line in lines :
    path_list = line.split("/")

    # 마지막 키워드는 안함
    for i in range(len(path_list) -1) :
        # print(path_list[i], end=" -> ")

        keyword = path_list[i]
        next_keyword = path_list[i+1]

        # 해당 키워드가 리스트에 존재 하는지
        if not isExistenceKeyword(path_dict_list, keyword): # 없으면
            path_dict_list.append({keyword : {}}) # 새로운 딕셔너리 추가
    
        # 다음 키워드가 해당 dict의 리스트에 있는지
        if isExistenceNextKeyword(path_dict_list, keyword, next_keyword) : # 있으면
            path_dict_list = plusNextKeywordCount(path_dict_list, keyword, next_keyword)
        else : # 없으면
            path_dict_list = insertNextKeywordCount(path_dict_list, keyword, next_keyword)

print(path_dict_list)