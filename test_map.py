from btree_map import BTree_Class

while True:
    _ = input('1: Создать\n'
              '2: Удалить\n'
              '3: Найти\n'
              '4: Все дерево\n'
              '5: Выход\n')
    match _:
        case '1':
            key = int(input('Введите ключ'))
            data = input('Введите данные')
            BTree_Class.add_Node(key, data)
        case '2':
            choice_del = input('1: Удалить по ключу\n'
                               '2: Удалить все\n')
            match choice_del:
                case '1':
                    key = int(input('Введите ключ'))
                    BTree_Class.remove_key(int(key))
                case '2':
                    BTree_Class.remove_all()
        case '3':
            key = int(input('Введите ключ'))
            BTree_Class.key_value(int(key))
        case '4':
            BTree_Class.print_Tree()
        case '5':
            break