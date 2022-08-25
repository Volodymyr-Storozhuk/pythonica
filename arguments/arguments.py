
import sys


def use_script():
    using = """
    Please use:
    > python arguments.py [<command>]

    The following commands are available:
      --test     first argument
      --test2    second argument
      --help     general info
    """
    return using


def find_argument(argument):
    if argument in sys.argv:
        return True
    else:
        return False


def present_of_arguments():
    try:
        if sys.argv[1]:
            if find_argument('--test') or find_argument('--test2'):
                pass
            else:
                print(use_script())
    except Exception:
        print('No present of arguments:')
        print(use_script())
        # return False


def main():
    print(sys.argv)
    if present_of_arguments():

        if find_argument('--test') or find_argument('--test2'):
            print('One of two arguments is present!')

            if find_argument('--test'):
                print('Present of argument: --test')
            if find_argument('--test2'):
                print('Present of argument: --test2')

        if find_argument('--help'):
            print(use_script())


if __name__ == '__main__':
    main()
