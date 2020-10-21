__author__ = 'Souvik'

import csv
#import matplotlib.pyplot as plt

def count_status():
    try:
        fname = input("Enter the file name with the .csv extension : ")
        f = open(fname, 'r', newline='')
        file = csv.reader(f)
        status = dict()
        for row in file:
            if row[2] != ' ':
                stat_count = row[2]
                if stat_count not in status:
                    status[stat_count] = 1
                else:
                    status[stat_count] += 1
        print(status)
        #plot_status(status)

    except:
        print("ERROR : No file found in current directory or check file extension")
        exit()


'''
def plot_status(status):

    f = b = p = ns = 0
    labels = 'Failed', 'Blocked', 'Passed', 'Not Started'
    sizes = [f, b, p, ns]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0) # exploding first slice

    #Plot
    plt.pie(sizes, explode = explode, labels = labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

'''
if __name__ == '__main__':
    count_status()