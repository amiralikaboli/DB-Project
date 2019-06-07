import mysql.connector
import xlrd

password=input('enter yout database password: ')
connection = mysql.connector.connect(host='localhost', user='root', password=password)

cursor = connection.cursor()

cursor.execute('drop database digikala;')
cursor.execute('create database digikala;')
cursor.execute('use digikala;')
cursor.execute('create table book(id int primary key,'
               'fatitle varchar(255),'
               'entitle varchar(255),'
               'url varchar(255),'
               'facategory varchar(255),'
               'keyword varchar(255),'
               'fabrand varchar(255),'
               'enbrand varchar(255));')
cursor.execute('create table altbook(id int primary key auto_increment,'
               'productid int,'
               'title varchar(255),'
               'foreign key (productid) references book(id));')

cursor.execute('create table puzzle(id int primary key,'
               'fatitle varchar(255),'
               'entitle varchar(255),'
               'url varchar(255),'
               'facategory varchar(255),'
               'keyword varchar(255),'
               'fabrand varchar(255),'
               'enbrand varchar(255));')
cursor.execute('create table altpuzzle(id int primary key auto_increment,'
               'productid int,'
               'title varchar(255),'
               'foreign key (productid) references puzzle(id));')

cursor.execute('create table mouse(id int primary key,'
               'fatitle varchar(255),'
               'entitle varchar(255),'
               'url varchar(255),'
               'facategory varchar(255),'
               'keyword varchar(255),'
               'fabrand varchar(255),'
               'enbrand varchar(255));')
cursor.execute('create table altmouse(id int primary key auto_increment,'
               'productid int,'
               'title varchar(255),'
               'foreign key (productid) references mouse(id));')

cursor.execute('create table keyboard(id int primary key,'
               'fatitle varchar(255),'
               'entitle varchar(255),'
               'url varchar(255),'
               'facategory varchar(255),'
               'keyword varchar(255),'
               'fabrand varchar(255),'
               'enbrand varchar(255));')
cursor.execute('create table altkeyboard(id int primary key auto_increment,'
               'productid int,'
               'title varchar(255),'
               'foreign key (productid) references keyboard(id));')

cursor.execute('create table screenguard(id int primary key,'
               'fatitle varchar(255),'
               'entitle varchar(255),'
               'url varchar(255),'
               'facategory varchar(255),'
               'keyword varchar(255),'
               'fabrand varchar(255),'
               'enbrand varchar(255));')
cursor.execute('create table altscreenguard(id int primary key auto_increment,'
               'productid int,'
               'title varchar(255),'
               'foreign key (productid) references screenguard(id));')

cursor.execute('create table pouchcover(id int primary key,'
               'fatitle varchar(255),'
               'entitle varchar(255),'
               'url varchar(255),'
               'facategory varchar(255),'
               'keyword varchar(255),'
               'fabrand varchar(255),'
               'enbrand varchar(255));')
cursor.execute('create table altpouchcover(id int primary key auto_increment,'
               'productid int,'
               'title varchar(255),'
               'foreign key (productid) references pouchcover(id));')

cursor.execute('create table infbook(productid int primary key,foreign key (productid) references book(id));')
cursor.execute('create table infpuzzle(productid int primary key,foreign key (productid) references puzzle(id));')
cursor.execute('create table infmouse(productid int primary key,foreign key (productid) references mouse(id));')
cursor.execute('create table infkeyboard(productid int primary key,foreign key (productid) references keyboard(id));')
cursor.execute(
    'create table infscreenguard(productid int primary key,foreign key (productid) references screenguard(id));')
cursor.execute(
    'create table infpouchcover(productid int primary key,foreign key (productid) references pouchcover(id));')

data = xlrd.open_workbook('data/5-awte8wbd.xlsx')
sheet = data.sheet_by_name('Sheet1')

mxbook = mxpuzzle = mxmouse = mxkeyboard = mxscreen = mxcover = ''
insrtbook = 'insert into book values(%s,%s,%s,%s,%s,%s,%s,%s)'
insrtpuzzle = 'insert into puzzle values(%s,%s,%s,%s,%s,%s,%s,%s)'
insrtkeyboard = 'insert into keyboard values(%s,%s,%s,%s,%s,%s,%s,%s)'
insrtscreen = 'insert into screenguard values(%s,%s,%s,%s,%s,%s,%s,%s)'
insrtmouse = 'insert into mouse values(%s,%s,%s,%s,%s,%s,%s,%s)'
insrtcover = 'insert into pouchcover values(%s,%s,%s,%s,%s,%s,%s,%s)'
insrtInfbook = 'insert into infbook values(%s)'
insrtInfkeyboard = 'insert into infkeyboard values(%s)'
insrtInfpuzzle = 'insert into infpuzzle values(%s)'
insrtInfmouse = 'insert into infmouse values(%s)'
insrtInfscreen = 'insert into infscreenguard values(%s)'
insrtInfcover = 'insert into infpouchcover values(%s)'
insrtAltbook = 'insert into altbook values(default,%s,%s);'
insrtAltpuzzle = 'insert into altpuzzle values(default,%s,%s);'
insrtAltmouse = 'insert into altmouse values(default,%s,%s);'
insrtAltkeyboard = 'insert into altkeyboard values(default,%s,%s);'
insrtAltscreen = 'insert into altscreenguard values(default,%s,%s);'
insrtAltcover = 'insert into altpouchcover values(default,%s,%s);'

for i in range(1, sheet.nrows):
    facategory = sheet.cell(i, 5).value
    attribute = sheet.cell(i, 9).value
    if facategory == 'کتاب چاپی':
        if len(mxbook) < len(attribute.split('},{')):
            mxbook = attribute[2:-2]
    if facategory == 'پازل':
        if len(mxpuzzle) < len(attribute.split('},{')):
            mxpuzzle = attribute[2:-2]
    if facategory == 'ماوس (موشواره)':
        if len(mxmouse) < len(attribute.split('},{')):
            mxmouse = attribute[2:-2]
    if facategory == 'کیبورد (صفحه کلید)':
        if len(mxkeyboard) < len(attribute.split('},{')):
            mxkeyboard = attribute[2:-2]
    if facategory == 'محافظ صفحه نمایش گوشی':
        if len(mxscreen) < len(attribute.split('},{')):
            mxscreen = attribute[2:-2]
    if facategory == 'کیف و کاور گوشی':
        if len(mxcover) < len(attribute.split('},{')):
            mxcover = attribute[2:-2]

mxbook = mxbook.split('},{')
bookset = []
for i in range(len(mxbook)):
    str = mxbook[i] + '}'
    ind = str.find('"', 7)
    colname = str[7:ind]
    colname = colname.replace(' ', '_')
    colname = colname.replace('/', '_')
    colname = colname.replace('\_', '_')
    if colname not in bookset:
        cursor.execute('alter table infbook add ' + colname + ' varchar(255);')
        bookset.append(colname)
        insrtInfbook = insrtInfbook[:-1] + ',%s)'

mxpuzzle = mxpuzzle.split('},{')
puzzleset = []
for i in range(len(mxpuzzle)):
    str = mxpuzzle[i] + '}'
    ind = str.find('"', 7)
    colname = str[7:ind]
    colname = colname.replace(' ', '_')
    if colname not in puzzleset:
        cursor.execute('alter table infpuzzle add ' + colname + ' varchar(255);')
        puzzleset.append(colname)
        insrtInfpuzzle = insrtInfpuzzle[:-1] + ',%s)'

mxmouse = mxmouse.split('},{')
mouseset = []
for i in range(len(mxmouse)):
    str = mxmouse[i] + '}'
    ind = str.find('"', 7)
    colname = str[7:ind]
    colname = colname.replace(' ', '_')
    if colname not in mouseset:
        cursor.execute('alter table infmouse add ' + colname + ' varchar(255);')
        mouseset.append(colname)
        insrtInfmouse = insrtInfmouse[:-1] + ',%s)'

mxkeyboard = mxkeyboard.split('},{')
keyboardset = []
for i in range(len(mxkeyboard)):
    str = mxkeyboard[i] + '}'
    ind = str.find('"', 7)
    colname = str[7:ind]
    colname = colname.replace(' ', '_')
    if colname not in keyboardset:
        cursor.execute('alter table infkeyboard add ' + colname + ' varchar(255);')
        keyboardset.append(colname)
        insrtInfkeyboard = insrtInfkeyboard[:-1] + ',%s)'

mxscreen = mxscreen.split('},{')
screenset = []
for i in range(len(mxscreen)):
    str = mxscreen[i] + '}'
    ind = str.find('"', 7)
    colname = str[7:ind]
    colname = colname.replace(' ', '_')
    colname = colname.replace(':', '')
    if colname not in screenset:
        cursor.execute('alter table infscreenguard add ' + colname + ' varchar(255);')
        screenset.append(colname)
        insrtInfscreen = insrtInfscreen[:-1] + ',%s)'

mxcover = mxcover.split('},{')
coverset = []
for i in range(len(mxcover)):
    str = mxcover[i] + '}'
    ind = str.find('"', 7)
    colname = str[7:ind]
    colname = colname.replace(' ', '_')
    if colname not in coverset:
        cursor.execute('alter table infpouchcover add ' + colname + ' varchar(255);')
        coverset.append(colname)
        insrtInfcover = insrtInfcover[:-1] + ',%s)'

for i in range(1, sheet.nrows):
    id = int(sheet.cell(i, 0).value)
    fattile = sheet.cell(i, 1).value
    entitle = None if (sheet.cell(i, 2).value == '' or sheet.cell(i, 2).value == 'NULL') else sheet.cell(i, 2).value
    url = sheet.cell(i, 3).value
    alttitle = '' if sheet.cell(i, 4).value == 'NULL' else sheet.cell(i, 4).value
    facategory = sheet.cell(i, 5).value
    keyword = sheet.cell(i, 6).value
    fabrand = sheet.cell(i, 7).value
    enbrand = sheet.cell(i, 8).value
    attribute = sheet.cell(i, 9).value
    if alttitle != '':
        alttitle = alttitle.replace('،', ',')
        alttitle = alttitle.replace('--', ',')
        alttitle = alttitle.replace('-', ',')
        alttitle = alttitle.replace('#', ',')
        alttitle = alttitle.replace('/', ',')
        alttitle = alttitle.replace(' ,', ',')
        alttitle = alttitle.replace(', ', ',')
        alttitle = alttitle[:-1] if alttitle[-1] == ',' else alttitle
    if attribute != '':
        attribute = attribute[1:-1]
        repatt = attribute.replace(' ', '_')
        repatt = repatt.replace('/', '_')
        repatt = repatt.replace('\_', '__')
    mainvalues = (id, fattile, entitle, url, facategory, keyword, fabrand, enbrand)

    if facategory == 'کتاب چاپی':
        cursor.execute(insrtbook, mainvalues)
        if alttitle != '':
            alttitle = alttitle.split(',')
            for j in range(len(alttitle)):
                altvalues = (id, alttitle[j])
                cursor.execute(insrtAltbook, altvalues)
        if attribute != '':
            infvalues = [id]
            for j in range(len(bookset)):
                val = attribute[attribute.find('Value', repatt.find(bookset[j])) + 8:attribute.find('}', repatt.find(
                    bookset[j])) - 1]
                val = None if (len(val) == 0 or len(val) > 100) else val
                infvalues.append(val)
            infvalues = tuple(infvalues)
            cursor.execute(insrtInfbook, infvalues)

    if facategory == 'پازل':
        cursor.execute(insrtpuzzle, mainvalues)
        if alttitle != '':
            alttitle = alttitle.split(',')
            for j in range(len(alttitle)):
                altvalues = (id, alttitle[j])
                cursor.execute(insrtAltpuzzle, altvalues)
        if attribute != '':
            infvalues = [id]
            for j in range(len(puzzleset)):
                val = attribute[attribute.find('Value', repatt.find(puzzleset[j])) + 8:attribute.find('}', repatt.find(
                    puzzleset[j])) - 1]
                val = None if (len(val) == 0 or len(val) > 100) else val
                infvalues.append(val)
            infvalues = tuple(infvalues)
            cursor.execute(insrtInfpuzzle, infvalues)

    if facategory == 'ماوس (موشواره)':
        cursor.execute(insrtmouse, mainvalues)
        if alttitle != '':
            alttitle = alttitle.split(',')
            for j in range(len(alttitle)):
                altvalues = (id, alttitle[j])
                cursor.execute(insrtAltmouse, altvalues)
        if attribute != '':
            infvalues = [id]
            for j in range(len(mouseset)):
                val = attribute[attribute.find('Value', repatt.find(mouseset[j])) + 8:attribute.find('}', repatt.find(
                    mouseset[j])) - 1]
                val = None if (len(val) == 0 or len(val) > 100) else val
                infvalues.append(val)
            infvalues = tuple(infvalues)
            cursor.execute(insrtInfmouse, infvalues)

    if facategory == 'کیبورد (صفحه کلید)':
        cursor.execute(insrtkeyboard, mainvalues)
        if alttitle != '':
            alttitle = alttitle.split(',')
            for j in range(len(alttitle)):
                altvalues = (id, alttitle[j])
                cursor.execute(insrtAltkeyboard, altvalues)
        if attribute != '':
            infvalues = [id]
            for j in range(len(keyboardset)):
                val = attribute[attribute.find('Value', repatt.find(keyboardset[j])) + 8:attribute.find('}',
                                                                                                        repatt.find(
                                                                                                            keyboardset[
                                                                                                                j])) - 1]
                val = None if (len(val) == 0 or len(val) > 100) else val
                infvalues.append(val)
            infvalues = tuple(infvalues)
            cursor.execute(insrtInfkeyboard, infvalues)

    if facategory == 'محافظ صفحه نمایش گوشی':
        cursor.execute(insrtscreen, mainvalues)
        if alttitle != '':
            alttitle = alttitle.split(',')
            for j in range(len(alttitle)):
                altvalues = (id, alttitle[j])
                cursor.execute(insrtAltscreen, altvalues)
        if attribute != '':
            infvalues = [id]
            for j in range(len(screenset)):
                val = attribute[attribute.find('Value', repatt.find(screenset[j])) + 8:attribute.find('}', repatt.find(
                    screenset[j])) - 1]
                val = None if (len(val) == 0 or len(val) > 100) else val
                infvalues.append(val)
            infvalues = tuple(infvalues)
            cursor.execute(insrtInfscreen, infvalues)

    if facategory == 'کیف و کاور گوشی':
        cursor.execute(insrtcover, mainvalues)
        if alttitle != '':
            alttitle = alttitle.split(',')
            for j in range(len(alttitle)):
                altvalues = (id, alttitle[j])
                cursor.execute(insrtAltcover, altvalues)
        if attribute != '':
            infvalues = [id]
            for j in range(len(coverset)):
                val = attribute[attribute.find('Value', repatt.find(coverset[j])) + 8:attribute.find('}', repatt.find(
                    coverset[j])) - 1]
                val = None if (len(val) == 0 or len(val) > 100) else val
                infvalues.append(val)
            infvalues = tuple(infvalues)
            cursor.execute(insrtInfcover, infvalues)

connection.commit()
cursor.close()
connection.close()