import csv

def read_csv(fileName):

    with open(fileName, 'Ur') as f:
        data = list(tuple(rec) for rec in csv.reader(f, delimiter='|'))

    return data

def what_state(coordinates):
    return

if __name__ == "__main__":
    read_csv('states.csv')

