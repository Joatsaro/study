import openpyxl
import os
os.chdir('/')

workbook = openpyxl.load_workbook('example.xlsx')
type(workbook)
sheet = workbook.get_sheet_by_name('Sheet1')
workbook.get_sheet_names()
