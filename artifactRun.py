

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

if __name__=="__main__":
    fields = ['CHARACTER', 'ROLE', 'ARTIFACT', 'MAINSTATS', 'SUBSTATS']
    df = pd.read_excel('genshinPythonExcel.xlsx', usecols=fields)

    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_columns', None)

    df = df.replace('\n', ' ', regex=True)
    df = df.fillna("Unknown")
    df['ARTIFACT'] = df['ARTIFACT'].apply(shorten_text)

    # print(df.ARTIFACT)
    artInput= input("Enter an artifact set: ")
    artInput=artInput.capitalize()
    mask = df["ARTIFACT"].str.contains(artInput)

    # # print the corresponding rows
    # print(df[mask])

    # create a PyQt5 application
    app = QtWidgets.QApplication([])

    # create a PyQt5 table widget
    table = QtWidgets.QTableWidget()

    # set the number of rows and columns of the table
    table.setRowCount(df[mask].shape[0])
    table.setColumnCount(df[mask].shape[1])

    # set the column labels of the table
    table.setHorizontalHeaderLabels(df[mask].columns)

    # fill the table with the filtered dataframe values
    for i in range(df[mask].shape[0]):
        for j in range(df[mask].shape[1]):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(df[mask].iloc[i, j])))

    table.resize(2000, 1000)

    for x in range(0,5):
        table.resizeColumnToContents(x)

    # show the table
    table.show()

    # run the application
    app.exec_()
