import csv


def write_csv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for row_data in data:
            writer.writerow(row_data)


path = r"D:\PythonProject\first\rw_csv_files\0002.csv"

write_csv(path, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
