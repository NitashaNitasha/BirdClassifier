import pandas as pd

class_names=pd.read_csv('classes.txt')

def get_classes():
    return list(class_names)

def main():
    print(get_classes())


if __name__ == '__main__':
    main()