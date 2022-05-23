import csv


def read_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        info_list = []

        all_file_info = csv.reader(f)
        # print(all_file_info)

        for row in all_file_info:
            info_list.append(row)

    return info_list


path = r"D:\PythonProject\first\rw_csv_files\0001.csv"

info = read_csv(path)
