from openpyxl import Workbook

# Create a new workbook
wb = Workbook()
ws = wb.active

# Assume 'A1' contains the date/time data
# Get the cell
cell = ws['A1']

# Calculate the width needed to display the content properly
# Here, 'datetime' is the content type and '12/12/2022 12:34:56' is a sample datetime string
# You can replace it with your actual datetime value
width = len(str(cell.value)) * 1.2

# Set the column width
ws.column_dimensions[cell.column_letter].width = width

# Save the workbook
wb.save('attendance.xlsx')
