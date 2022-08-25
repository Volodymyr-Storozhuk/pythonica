import json


def read_json_file(path):
    with open(path) as f:
        j_obj = json.load(f)

    # full data from json file
    print(f'type object: {type(j_obj)}')
    print(j_obj)

    # full data from sql section
    print(f'sql dict: {j_obj["sql"]}')
    print((j_obj['sql'])['ip'])

    # get sql data section
    sql = j_obj['sql']
    print(f'sql server ip address: {sql["ip"]}')

    # get ftp data section
    ftp = j_obj['ftp']
    print(f'ftp server ip address: {ftp["ip"]}')


def main():
    try:
        read_json_file('setup.json')
    except Exception:
        print('No json file in current directory.')


if __name__ == "__main__":
    main()
