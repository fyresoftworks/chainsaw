import sys

def main():
    print('hi from tool1')
    if len(sys.argv) > 1:
        print('you passed:', ' '.join(sys.argv[1:]))

if __name__ == '__main__':
    main()
