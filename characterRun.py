import pandas as pd
from PyQt5 import QtCore, QtWidgets

#Source for excel sheet as of February 1st
#https://docs.google.com/spreadsheets/d/1gNxZ2xab1J6o1TuNVWMeLOZ7TPOqrsf3SshP5DLvKzI/edit#gid=2001372201
# Define a function to shorten the text
def shorten_text(text):
    # Split the text by " 2. "
    parts = text.split(' 2. ', 1)
    # Remove "1. " from the first part
    return parts[0].replace('1. ', '', 1) if parts else text

def shorten_text2(text):
    # Split the text by " 2. "
    parts = text.split(' 2. ', 1)
    # Remove "1. " from the first part
    return parts[0].replace('1. ', '', 1) if parts else text


if __name__=="__main__":
    fields = ['CHARACTER', 'ROLE', 'ARTIFACT', 'MAINSTATS', 'SUBSTATS']
    df = pd.read_excel('genshinPythonExcel.xlsx', usecols=fields)

    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_columns', None)

    value_to_check = input('Enter a character name: ')
    value_to_check = value_to_check.capitalize()

    # Use the boolean indexing to filter rows
    matching_rows = df[df['CHARACTER'] == value_to_check]
    matching_rows = matching_rows.replace('\n', ' ', regex=True)
    matching_rows['ARTIFACT'] = matching_rows['ARTIFACT'].apply(shorten_text)

    # print(matching_rows)

    # create a PyQt5 application
    app = QtWidgets.QApplication([])

    # create a PyQt5 table widget
    table = QtWidgets.QTableWidget()

    # set the number of rows and columns of the table
    table.setRowCount(matching_rows.shape[0])
    table.setColumnCount(matching_rows.shape[1])

    # set the column labels of the table
    table.setHorizontalHeaderLabels(matching_rows.columns)

    # fill the table with the filtered dataframe values
    for i in range(matching_rows.shape[0]):
        for j in range(matching_rows.shape[1]):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(matching_rows.iloc[i, j])))

    table.resize(2000, 1000)

    for x in range(0,5):
        table.resizeColumnToContents(x)

    # show the table
    table.show()

    # run the application
    app.exec_()