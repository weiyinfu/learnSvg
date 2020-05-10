from flask import Flask, request, make_response
import re

app = Flask(__name__)

s = """
<svg version="1.1" 
    xmlns="http://www.w3.org/2000/svg" 
    width="80px" 
    height="80px"
    style="background:{background}">
  <text x="50%" y="50%" font-size="60px" fill="{color}" style=' dominant-baseline: central;text-anchor: middle; font-family: "CESI楷体-GB2312,宋体,隶书,仿宋,Droid Serif", "DejaVu Serif", "STIX", serif;'>{text}</text>
</svg>
"""


def rewrite_color(color):
    try:
        int(color, 16)
        color = '#' + color
    except:
        return color


@app.route("/")
def get():
    # 根据字符串创建svg
    background = request.args.get('background', "#dddddd")
    color = request.args.get('color', '#42b983')
    text = request.args.get('text', '我').strip() or '我'
    if len(text) > 1:
        text = text[0]
    background = rewrite_color(background)
    color = rewrite_color(color)
    resp = make_response(s.format(background=background, color=color, text=text))
    resp.headers['Content-Type'] = "image/svg+xml"
    return resp


if __name__ == '__main__':
    app.run(debug=True)
