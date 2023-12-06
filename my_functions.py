def length(list_str):
    list_str = list_str[1:-1]
    if len(list_str) == 0:
        return 0
    else:
        return list_str.count(",") + 1

def total(list_str):
    list_str = list_str[1:-1]
    if len(list_str) == 0:
        return 0
    else:
        list_num = [int(i) for i in list_str.split(",") if i.isdigit()]
        return sum(list_num)

def contains(list_str, item):
    list_str = list_str[1:-1]
    if len(list_str) == 0:
        return False
    else:
        list_items = [i.strip() for i in list_str.split(",")]
        return item in list_items

def find_item(list_str, item):
    list_str = list_str[1:-1]
    if len(list_str) == 0:
        return -1
    else:
        list_items = [i.strip() for i in list_str.split(",")]
        if item in list_items:
            return list_items.index(item)
        else:
            return -1

def reduce(IPv4_address):
    return '.'.join(str(int(i)) for i in IPv4_address.split('.'))

def filter_numbers(str):
    return ','.join([i for i in str.split() if i.isdigit()])

def filter_numbers(str):
    return ','.join([i for i in str.split() if i.isdigit()])

def split_quotation(str):
    return re.findall(r'"([^"]*)"', str)