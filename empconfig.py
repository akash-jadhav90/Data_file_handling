import json

from flask import Flask,request,render_template

from Empinfo import Emp

app=Flask(__name__)


FILESPATH='G:\\Flask_JSON_Project\\Data'
JSON_FILE_PATH=FILESPATH+"EMPLOYEE.json"
TEXT_FILE_PATH=FILESPATH+"EMPLOYEE.txt"
CSV_FILE_PATH=FILESPATH+"EMPLOYEE.csv"
EXCEL_FILE_PATH=FILESPATH+"EMPLOYEE.xlsx"
SQLITE_FILE_PATH=FILESPATH+"EMPLOYEE.sqlite"

def write_json(emp):
    with open(JSON_FILE_PATH,'w') as file:
        json.dump(emp.__dict__,file)


def write_csv(emp):
    with open(CSV_FILE_PATH,'w') as file:
        empstr=str(emp.empid)+','+emp.empage+','+emp.empname+','+emp.empemail+','+emp.empsalary
        file.writelines(empstr)

def write_text(emp):
    with open(TEXT_FILE_PATH,'w') as file:
        empstr=str(emp.empid)+'\t\t'+emp.empage+'\t\t'+emp.empname+'\t\t'+emp.empemail+'\t\t'+emp.empsalary
        file.writelines(empstr)

import openpyxl
def write_excel(emp):
    workbook= openpyxl.workbook
    sheet=workbook.create_sheet('emp_data')
    sheet['A1']=emp.empid
    sheet['B1'] = emp.empname
    sheet['C1'] = emp.empage
    sheet['D1'] = emp.empsalary
    sheet['E1'] = emp.empemail
    workbook.save(EXCEL_FILE_PATH
                  )


def write_sqlite(emp):
    pass

File_type_ref_fun={
        "j": write_json,
        "c": write_csv,
        "t": write_text,
        "s": write_sqlite,
        "e": write_excel
        }

@app.route('/welcome')
@app.route('/svae/info' ,methods=['post','get'])
def Save_emp_detalis():
    mes = ''
    if request.method=='POST':
        formdata=request.form
        emp=Emp(eid=formdata.get('eid'),enm=formdata.get('enm'),esalary=formdata.get('esalary'),eemail=formdata.get('eemail'),eage=formdata.get('eage'))            #formdata--> dict --> Emp object (map kar ke deta hai)
        print(emp)
        Files=formdata.getlist('filetype')

        if Files:
            for type in Files:
                ref_fun=File_type_ref_fun.get(type)
                ref_fun(emp)
        else:
            mes='you should be select files'


    return render_template('employee.html',result=mes)





if __name__ == '__main__':
    app.run(debug=True,port=9000)