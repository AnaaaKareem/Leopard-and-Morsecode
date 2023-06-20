import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        try:
            with open(filepath, 'r') as file:
                self.file_reader = csv.reader(file)
                # Assigns column headers
                self.file_header = next(self.file_reader)
                # Used for store rows of a column
                self.rows = []
                # Used for stats method storing data
                self.num_store = []
                # Used for stats method dictionary use
                self.head_list = []
                self.count = []
                self.mean = []
                self.min = []
                self.max = []
                self.full_dict = {}
                # Assign the data under the header
                for i in self.file_reader:
                    self.rows.append(i)
                    if bool(self.rows) is False:
                        print("empty file")
                        break
        except (FileNotFoundError, IOError):
            print("file not found")

    def get_header(self) -> list:
        return self.file_header

    def get_data(self) -> list:
        return self.rows

    def stats(self) -> dict:
        global row
        # Loop over the number of columns
        for num in range(len(self.file_header)):
            # Check in row 2 if the cell has a numeric number for each column
            if self.rows[1][num].isnumeric():
                for row in self.rows:
                    # Check if a number doesn't exist
                    # If true continue
                    # row[num] is the position of the cell
                    if row[num] == "NA":
                        continue
                    elif row[num] == "-":
                        continue
                    elif row[num] is None:  # if element is empty
                        continue
                    # If the column is numeric add number to list
                    else:
                        try:
                            self.num_store.append(int(row[num]))
                        except ValueError:
                            continue
                # Get count, mean, min, max
                self.head_list.append(
                    self.file_header[num])  # Get column header
                self.count.append(
                    len(self.num_store))  # Get count
                self.mean.append(
                    round(sum(self.num_store) /
                          len(self.num_store), 2))  # Get average
                self.min.append(min(self.num_store))  # Get Minimum
                self.max.append(max(self.num_store))  # Get Maximum
                # Clear Number list for the next column
                self.num_store.clear()
            else:
                continue

        # Make nested dictionary
        for head_list, count, mean, minimum, maximum in zip(
                self.head_list, self.count, self.mean, self.min, self.max):
            self.full_dict.update({head_list: {'Count': count, 'Mean': mean,
                                               'Minimum': minimum, 'Maximum': maximum}})

        return self.full_dict

    def html_stats(self, stats: dict, filepath: str) -> None:
        with open(filepath, 'w') as file:
            file.write("<html>\n")
            file.write("<head>\n")
            file.write("<style>\n")
            file.write("table, th, td {border: 1px solid; "
                       "border-collapse: "
                       "collapse; width: 1520px;}\n")
            file.write("th {padding: 5px; text-align: center; "
                       "background-color: Black; color: White;}\n")
            file.write("td {padding: 5px; text-align: center; "
                       "background-color: aquamarine;}\n")
            file.write("h1 {text-align: center; color: Black;}\n")
            file.write("</style>\n")
            file.write(f"<title>{filepath}</title>\n")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write(f"<h1>{filepath} Data</h1>\n")
            file.write("<table>\n")
            file.write("<tr>\n")
            file.write("<th>Name</th>\n")
            file.write("<th>Count</th>\n")
            file.write("<th>Mean</th>\n")
            file.write("<th>Min</th>\n")
            file.write("<th>Max</th>\n")
            file.write("</tr>\n")
            # Write headers and write to the first row of the table
            for key, value in stats.items():
                file.write("<tr>\n")
                file.write("<td>" + str(key) + "</td>\n")
                # Get the calculations and write after the headers
                for keys, values in value.items():
                    file.write("<td>" + str(values) + "</td>\n")
                file.write("</tr>\n")
            file.write("</table>\n")
            file.write("</body>\n")
            file.write("</html>\n")

    def count_instances(self, colhead, criteria) -> int:
        """
        Firstly, Colhead argument is placed to input the column name
        with the criteria to check what elements to count.
        Head variable is assigned then a for loop is responsible
        to assign the headers. List_data list to store column's data.
        After an if condition is placed to check is the argument
        colhead value in the header if true gather the indexes
        found within a variable and create a separate list to store
        the element and a variable to count them.
        """
        global list_data, pos, list_

        head = self.file_header
        # Store column headers into an array
        for h in range(len(self.file_header)):
            head[h] = head[h].lower()

        # Get Column Data
        list_data = [[data.lower() for data in part] for part in self.rows]

        # Check and count the criteria if found
        if colhead.lower() in head:
            pos = head.index(colhead.lower())
        list_ = [elem[pos] for elem in list_data]
        instances = list_.count(criteria.lower())

        return instances


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    print()

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    print(test2.get_header())
    print(test2.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    print()

    # test student.csv
    test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test3.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")
