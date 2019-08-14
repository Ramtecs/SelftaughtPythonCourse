
'''
1. Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant",
"Inception"], ["Training Day", "Man on Fire", "Flight"]]
and write them to a CSV file. The data from each list should be a row in the file, with each item in the list separated by a comma.
2.Move it a notch by putting a header with threee columns, Interesting, Less Interesting, Boring for the movie rating.
'''
import csv
list= [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant","Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open('test.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['Interesting ', 'Less Interesting', 'Boring'])
    writer.writeheader()
    writer = csv.writer(csv_file, lineterminator='\n')
    writer.writerows(list)

'''
output:

Interesting ,Less Interesting,Boring
Top Gun,Risky Business,Minority Report
Titanic,The Revenant,Inception
Training Day,Man on Fire,Flight

'''
