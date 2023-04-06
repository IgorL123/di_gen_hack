import win32com.client as win32
import win32api
from docxtpl import DocxTemplate
from docx2pdf import convert
import os

import settings

def generate(duties, requirements, position, company_name, director_name, out_path):
    word = win32.gencache.EnsureDispatch('Word.Application')

    #####################Путь к шаблону
    doc = word.Documents.Open(settings.TEMPLATE_PATH)
    table = doc.Tables(2)

    for req_now in requirements:
        row = table.Rows.Add(table.Rows(4))
        cell = row.Cells(1)
        settings.set_font(cell)
        cell.Range.Text = req_now

    for dut_now in duties:
        row = table.Rows.Add(table.Rows(3))
        cell = row.Cells(1)
        settings.set_font(cell)
        cell.Range.Text = dut_now

    doc.SaveAs(out_path)
    doc.Close()

    doc = DocxTemplate(out_path)
    context = { 'position' : position, 'company_name':company_name, 'director_name':director_name}
    doc.render(context)
    doc.save(out_path)


    convert(out_path, os.path.splitext(out_path)[0]+".pdf")
