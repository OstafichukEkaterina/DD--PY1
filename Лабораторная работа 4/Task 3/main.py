def delete(list_, index=None):
    if index == None or index == -1:
        new_list_ = list_[:-1]
    elif index > len(list_) or index * (-1) > len(list_):
        new_list_=list_
    else:
        new_list_ = list_[:index] + list_[index + 1:]
    return new_list_

print(delete([0, 0, 1, 2], index=0)) # [0, 1, 2]
print(delete([0, 1, 2, 3], index=6)) # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4], index=-1)) # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4], index=-6)) #[0, 1, 2, 3, 4]
print(delete([0, 1, 2, 3, 4], index=-3)) #[0, 1, 3, 4]
print(delete([0, 1, 2, 3, 4], index=-2)) #[0, 1, 2, 4]
print(delete([0, 1, 2, 3, 4, 5])) # [0, 1, 2, 3, 4]