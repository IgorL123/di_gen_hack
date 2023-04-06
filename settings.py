TEMPLATE_PATH = 'C:\\Users\\manyg\\Desktop\\projects\\python\\test\\wordGen\\Example.docx'

def set_font(cell):
    cell.Range.Font.Name = 'Times New Roman'
    cell.Range.Font.Size = 11
    cell.Range.Font.Bold = False
    cell.Range.Font.Italic = False
    cell.Range.Font.Underline = False
