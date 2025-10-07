# Name: Elise Tuttle
# Student ID: 93100225
# Email: eltuttle@umich.edu
# GenAI: Used ChatGPT for help with setup, understanding code, and clarifying
import csv

def read_csv_file(filename):
    """
    reads penguins CSV and returns a list of dictionaries.
    """
    data = []
    with open(filename, newline='', encoding="utf-8", errors="ignore") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # convert bill_length_mm to float if it's not empty or NA
            if row['bill_length_mm'] != 'NA' and row['bill_length_mm'] != '':
                row['bill_length_mm'] = float(row['bill_length_mm'])
            else:
                row['bill_length_mm'] = None
            data.append(row)
    return data
def average_bill_length_per_species(data):
    """
    Calculates average bill length per species.
    """
    species_totals = {}
    species_counts = {}

    for row in data:
        species = row['species']
        bill_length = row['bill_length_mm']
        if species and bill_length is not None:
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