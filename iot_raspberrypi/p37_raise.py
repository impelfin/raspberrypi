list = []

try:
    while True:
        print('아이템 개수 : ', len(list))
        print('인벤토리 : ', list)

        if len(list) >= 4:
            raise Exception('인벤토리 부족')
        item = 'item' + str(len(list))
        list.append(item)
except Exception as e:
    print('인벤토리가 꽉 찼습니다.')
    print(e)
