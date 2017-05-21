import os

def get_mac_address_float():
    f = '/Users/tianyongkang/test01'
    if os.path.exists(f):
        with file(f,'r') as fr:
            for i in fr.readlines():
                r = i.strip()
                yield r
    

def get_mac_address_fixed():
    fixed_mac_address = []
    f = '/Users/tianyongkang/test02'
    if os.path.exists(f):
        with file(f,'r') as fr:
            for i in fr.readlines():
                r = i.strip()
                fixed_mac_address.append(r)
    return fixed_mac_address         

def main():
    for i in get_mac_address_float():
        if i not in get_mac_address_fixed():
            print i
            

if __name__ == '__main__':
    main()