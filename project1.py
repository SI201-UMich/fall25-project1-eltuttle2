# Name: Elise Tuttle
# Student ID: 93100225
# Email: eltuttle@umich.edu
# GenAI: Used ChatGPT for help with setup and debugging

import unittest

def read_csv_file(filename):
    """
    reads CSV file and returns a list of dictionaries,
    cleaning extra quotation marks from headers and values.
    """
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        header = [h.strip('"') for h in header]
        for line in lines[1:]:
            parts = line.strip().split(',')
            parts = [p.strip('"') for p in parts]
            row = dict(zip(header, parts))
            data.append(row)
    return data

def average_bill_length_per_species(data):
    """
    calculates the average bill length per species
    """
    species_totals = {}
    species_counts = {}
    for row in data:
        species = row.get('species', '')
        bill_length = row.get('bill_length_mm', '')
        if species == '' or bill_length in ('', 'NA'):
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

def average_flipper_length_per_species(data):
    """
    calculates the average flipper length per species
    """
    species_totals = {}
    species_counts = {}
    for row in data:
        species = row.get('species', '')
        flipper_length = row.get('flipper_length_mm', '')
        if species == '' or flipper_length in ('', 'NA'):
            continue
        flipper_length = float(flipper_length)
        if species in species_totals:
            species_totals[species] += flipper_length
            species_counts[species] += 1
        else:
            species_totals[species] = flipper_length
            species_counts[species] = 1
    averages = {}
    for species in species_totals:
        averages[species] = species_totals[species] / species_counts[species]
    return averages

def main():
    """
    main function to read data and print averages
    """
    filename = 'penguins.csv'
    data = read_csv_file(filename)
    
    bill_averages = average_bill_length_per_species(data)
    flipper_averages = average_flipper_length_per_species(data)
    
    print("Average bill length per species:")
    for species, avg in bill_averages.items():
        print(f"{species}: {avg}")
    
    print("\nAverage flipper length per species:")
    for species, avg in flipper_averages.items():
        print(f"{species}: {avg}")

class TestPenguinsFunctions(unittest.TestCase):
    """
    simple tests for average functions using a small sample
    """
    def setUp(self):
        self.sample_data = [
            {'species': 'Adelie', 'bill_length_mm': '39.1', 'flipper_length_mm': '181'},
            {'species': 'Adelie', 'bill_length_mm': '39.5', 'flipper_length_mm': '186'},
            {'species': 'Adelie', 'bill_length_mm': 'NA', 'flipper_length_mm': 'NA'},
            {'species': 'Gentoo', 'bill_length_mm': '47.0', 'flipper_length_mm': '210'},
            {'species': 'Gentoo', 'bill_length_mm': '48.0', 'flipper_length_mm': '220'},
        ]

    def test_average_bill_length(self):
        result = average_bill_length_per_species(self.sample_data)
        self.assertAlmostEqual(result['Adelie'], (39.1 + 39.5)/2)
        self.assertAlmostEqual(result['Gentoo'], (47.0 + 48.0)/2)

    def test_average_flipper_length(self):
        result = average_flipper_length_per_species(self.sample_data)
        self.assertAlmostEqual(result['Adelie'], (181 + 186)/2)
        self.assertAlmostEqual(result['Gentoo'], (210 + 220)/2)

if __name__ == "__main__":
    #main()
    unittest.main()
