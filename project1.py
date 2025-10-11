# Name: Elise Tuttle
# Student ID: 93100225
# Email: eltuttle@umich.edu
# GenAI: Used ChatGPT for help with setup and debugging

def read_csv_file(filename):
    """
    Reads a CSV file and returns a list of dictionaries,
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
    Calculates the average bill length per species.
    """
    species_totals = {}
    species_counts = {}
    for row in data:
        species = row.get('species', '')
        bill_length = row.get('bill_length_mm', '')
        if species == '' or bill_length == '' or bill_length == 'NA':
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
    Main function to read data and print average bill lengths per species.
    """
    filename = 'penguins.csv'
    data = read_csv_file(filename)
    averages = average_bill_length_per_species(data)
    print("Average bill length per species:")
    for species, avg in averages.items():
        print(f"{species}: {avg}")


if __name__ == "__main__":
    main()
