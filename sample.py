import csv

def main():
    for i in range(1,9):
        with open('cood.csv', 'a')as file:
            writer = csv.writer(file)      
            writer.writerow([2,2])
    
main()