# Name: Elise Tuttle
# Student ID: 93100225
# Email: eltuttle@umich.edu
# GenAI: Used ChatGPT for help with setup, understanding code, and clarifying

import csv

def read_csv_file(filename):
    """
    reads a csv and returns a list of dictionaries
    """
    data = []
    with open(filename, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def average_bill_length_per_species(data):
    """
    calculates average bill length per species
    """
    species_totals = {}
    species_counts = {}

    for row in data:
        species = row['species']
        bill_length = row['bill_length_mm']
        if species == '' or bill_length == '':
            continue
        bill_length = float(bill_length)
        if species in species_totals:
            species_totals[species] += bill_length
            species_counts[species] += 1
        else:
            species_totals[species] = bill_length
            species_counts[species] = 1

    averages = {}
    for species in species_totals:
        averages[species] = species_totals[species] / species_counts[species]

    return averages

def main():
    """
    main function to run the program
    """
    filename = "penguins.csv"  # make sure your csv file is named correctly
    data = read_csv_file(filename)
    averages = average_bill_length_per_species(data)
    print("Average bill length per species:")
    for species, avg in averages.items():
        print(f"{species}: {avg}")

if __name__ == "__main__":
    main()
