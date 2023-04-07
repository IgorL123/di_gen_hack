import win32com.client as win32
import win32api
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
import settings
import pythoncom


def generate(targets, duties, requirements, position, company_name, director_name, filename = "Result"):

    pythoncom.CoInitializeEx(0)
    
    out_path_ = os.getcwd()+"\\docs\\"+filename+".docx"
    word = win32.gencache.EnsureDispatch('Word.Application')

    doc = word.Documents.Open(settings.TEMPLATE_PATH)
    table = doc.Tables(2)

    cell = table.Cell(3, 1)
    list_format = cell.Range.ListFormat
    list_format.ApplyBulletDefault()
    list_format.ApplyNumberDefault()
    text_to_ins = ""
    for i in range(len(targets)-1):
        text_to_ins+=targets[i]+"\n"
    cell.Range.Text = text_to_ins+targets[-1]
    settings.set_font(cell)

    k = 1
    for req_now in requirements:
        to_add_now = ''
        for i in range(len(req_now)-1):
            to_add_now+=req_now[i]+'\n'
        to_add_now+=req_now[len(req_now)-1]

        if(k>6):
            print("Warning! The number of items in the list responsible for the requirements of the position exceeds 6. An error is possible.")
            break
        cell = table.Cell(5+k, 2)
        cell.Range.Text = to_add_now
        settings.set_font(cell)
        k+=1

    for dut_now in duties:
        row = table.Rows.Add(table.Rows(5))
        cell = row.Cells(1)
        cell.Range.Text = dut_now
        settings.set_font(cell)

    doc.SaveAs(out_path_)
    doc.Close()

    doc = DocxTemplate(out_path_)
    context = { 'position' : position, 'company_name':company_name, 'director_name':director_name}
    doc.render(context)
    doc.save(out_path_)


    convert(out_path_, os.path.splitext(out_path_)[0]+".pdf")
