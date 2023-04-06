import os

TEMPLATE_PATH = os.getcwd()+"\\Template.docx"

def set_font(cell):
    cell.Range.Font.Name = 'Times New Roman'
    cell.Range.Font.Size = 11
    cell.Range.Font.Bold = False
    cell.Range.Font.Italic = False
    cell.Range.Font.Underline = False
