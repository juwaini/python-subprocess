import subprocess


def main():
    ls = subprocess.run(['ls'], capture_output=True)
    print(ls)
    print(ls.returncode)
    print(ls.stdout)
    print(f'ls type: {type(ls)}')


if __name__ == '__main__':
    main()
