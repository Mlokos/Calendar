from fpdf import FPDF
from typing import Tuple

pdf = FPDF(format='A4', unit='mm')


class Month:
    def __init__(self, cell_side_length: int) -> None:
        self.cell_side_length = cell_side_length
    
    def get_height(self):
        return 9*self.cell_side_length

    def get_width(self):
        return 6*self.cell_side_length
    
    def draw_layout(self, start_position: Tuple[int, int]) -> None:
        pdf.set_xy(*start_position)
        pdf.cell(self.get_width(), self.cell_side_length, '', border=1, align='')
        pdf.ln(self.cell_side_length)
        pdf.set_x(start_position[0])
        for i in range(7):
            for j in range(6):
                pdf.cell(self.cell_side_length, self.cell_side_length, '', border=1)
            pdf.ln(self.cell_side_length)
            pdf.set_x(start_position[0])
        pdf.cell(self.get_width(), self.cell_side_length, '', border=1)
    
    def write_left_column(self, start_position: Tuple[int, int]) -> None:
        pdf.set_xy(*start_position)
        pdf.ln(self.cell_side_length)
        pdf.set_x(start_position[0])
        for week_day in ['Pon', 'Wt', 'Śr', 'Czw', 'Pt', 'Sb', 'Nd']:
            pdf.ln(-(2/7)*self.cell_side_length)
            pdf.set_x(start_position[0])
            pdf.cell(self.cell_side_length, self.cell_side_length, week_day, border=0, align='L')
            pdf.ln((9/7)*self.cell_side_length)

    def write_top_column():
        pass

    def write_center():
        pass

if __name__ == "__main__":
    pdf.add_page()
    pdf.add_font("NotoSans", style="", fname="four_month_calendar/noto-sans/NotoSans-Regular.ttf", uni=True)
    pdf.add_font("NotoSans", style="B", fname="four_month_calendar/noto-sans/NotoSans-Bold.ttf", uni=True)
    pdf.set_font('NotoSans', '', 8.0) 

    m = Month(13)
    spacing = 14

    top_left = (20, 23)
    top_right = tuple(map(sum, zip(top_left, (m.get_width() + spacing, 0))))
    bottom_left = tuple(map(sum, zip(top_left, (0, m.get_height() + spacing))))
    bottom_right = tuple(map(sum, zip(top_left, (m.get_width() + spacing, m.get_height() + spacing))))

    m.draw_layout(top_left)
    m.write_left_column(top_left)
    m.draw_layout(top_right)
    m.draw_layout(bottom_left)
    m.draw_layout(bottom_right)

    pdf.output('table-using-cell-borders.pdf','F')
