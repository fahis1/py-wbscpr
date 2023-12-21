import openpyxl
import random

# Generate a random integer between 4 and 12 (multiples of 5 between 20 and 60)

wb = openpyxl.load_workbook(r'C:\Users\fahis\OneDrive\Desktop\assesment\scraper\project.xlsx')
sheet = wb.active
print("opened")
row = 21  
for i in range(40):
    random_number = random.randint(4, 12) * 5
    sheet.cell(row=row, column=7).value = random_number
    print("saved")
    row += 1
wb.save('project.xlsx')
print("saved")