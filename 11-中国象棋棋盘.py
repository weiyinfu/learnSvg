filename = "12-中国象棋棋盘.svg"
board_rect = [0, 0, 10, 11]
out_rect = [0, 0, 8, 9]
lines = []
grid = 30  # 每个格子的像素
for i in range(1, 9):
    lines.append((0, i, 8, i))
for i in range(1, 8):
    if i == 0 or i == 8:
        lines.append((i, 0, i, 9))
    else:
        lines.append((i, 0, i, 4))
        lines.append((i, 5, i, 9))
lines.append((3, 0, 5, 2))
lines.append((5, 0, 3, 2))
lines.append((3, 9, 5, 7))
lines.append((3, 7, 5, 9))


def get_rect(rect):
    return f'<rect x="{rect[0] * grid}" y="{rect[1] * grid}" width="{rect[2] * grid - rect[0] * grid}" height="{rect[3] * grid - rect[1] * grid}" style="fill:#ffa500;fill-opacity:1;stroke-opacity:1"></rect>'


def get_stroke_rect(rect):
    rect = [i + 1 for i in rect]
    w, h = rect[2] - rect[0], rect[3] - rect[1]
    return f'''<rect width="{w * grid}" height="{h * grid}" x="{rect[0] * grid}" y="{rect[1] * grid}"
    style="fill-opacity:0;stroke-width:1.45%;stroke:black"></rect>'''


def get_line(line):
    line = [i + 1 for i in line]
    return f'<line x1="{line[0] * grid}" y1="{line[1] * grid}" x2="{line[2] * grid}" y2="{line[3] * grid}" style="stroke:black;stroke:black;stroke-width:1.45%;"></line>'


def line_str():
    return '\n'.join(get_line(line) for line in lines)


svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{9 * grid + grid}" height="{10 * grid + grid}">
    <title>画一个象棋棋盘</title>
    <desc>有两下子</desc>
    {get_rect(board_rect)}
    {get_stroke_rect(out_rect)}
    {line_str()}
</svg>
"""
open(filename, 'w').write(svg)
