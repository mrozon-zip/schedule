from fpdf import FPDF
from functions import schedule_dataframe
import datetime as dt

pdf = FPDF(orientation='P', unit='mm',format='A4')

# Set start dates
start = dt.date(2023, 8, 30)
start2 = dt.date(2023, 9, 1)
rotations = 20
# set rooms
df = schedule_dataframe(start, start2, rotations)

for i in range(0,20*12,12):
    rotation = df.iloc[i:i+12, :]
    pdf.add_page()

    # set header
    columns = list(df.columns)
    columns = [item.capitalize() for item in columns]
    pdf.set_font(family='Helvetica', size=18, style='B')
    pdf.cell(w=60, h=14, txt=str(columns[0]), align='C', border=1)
    pdf.cell(w=60, h=14, txt=str(columns[1]), align='C', border=1)
    pdf.cell(w=60, h=14, txt=str(columns[2]), align='C', border=1, ln=1)

    for index, row in rotation.iterrows():

        # set rows
        pdf.set_font(family='Helvetica', size=18)
        pdf.cell(w=60, h=14, txt=str(row['dates']), align='C', border=1)
        pdf.cell(w=60, h=14, txt=str(row['trash']), align='C', border=1)
        pdf.cell(w=60, h=14, txt=str(row['cleaning']), align='C', border=1, ln=1)

    pdf.cell(w=0, h=10, ln=1)

    pdf.cell(w=180, h=10, txt="Names", align='C', border=1, ln=1)

    names = df.iloc[i:i+6, :]

    for index, row in names.iterrows():

        # set rows
        pdf.set_font(family='Helvetica', size=18)
        pdf.cell(w=45, h=10, txt=str(row['trash']), align='C', border=1)
        pdf.cell(w=45, h=10, txt="", align='C', border=1)
        pdf.cell(w=45, h=10, txt=str(row['cleaning']), align='C', border=1)
        pdf.cell(w=45, h=10, txt="", align='C', border=1, ln=1)


pdf.output('schedule.pdf')