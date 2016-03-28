# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
bg99 = Blueprint('bg99', __name__, url_prefix='/bg99', template_folder='templates')

@bg99.route('/task0')
def task0():
    return "bg99 task0"
    
@bg99.route('/task1')
def task1():
    #return "bg99 task1"
    return render_template('task1.html', var1="來自 bg99 的 task1 變數")
    
# 展示傳回 Brython 程式
@bg99.route('/task3')
def task3():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  

def task3(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    # basic1 轉 -120 度
    basic1.rotate(-120)

    cmbr.appendPath(basic1)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 3 倍
    cgo.render(cmbr, x, y, 3, rot)

task3(-100, -130, 0, 0, 0, "blue", True, 4)
'''
    return outstring
    
@bg99.route('/bezier')
def bezier():
    outstring = '''
    <!-- 導入 Brython 函式庫 -->

<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>

<!-- 導入 Cango2d 函式庫 -->

<script type="text/javascript" src="http://cadlab.mde.tw/post/js/Cango2D.js"></script>

<!-- 導入 Cango 函式庫 -->

<script type="text/javascript" src="http://cadlab.mde.tw/post/js/Cango-min.js"></script>

<!-- 導入 gearUtils 函式庫 -->

<script type="text/javascript" src="http://cadlab.mde.tw/post/js/gearUtils.js"></script>

<!-- 導入 CangoAnimation.js 函式庫 -->

<script type="text/javascript" src="http://cadlab.mde.tw/post/js/CangoAnimation.js"></script>

<!-- window 導入後, 啟動 brython() -->

<script>
window.onload=function(){
brython(1);
}
</script>
<p>Bezier 曲線與滑鼠:</p>
<!-- 建立畫布 -->
<canvas id="plotarea" width="600" height="600"></canvas>
<script type="text/python">
from browser import window
from javascript import JSConstructor

cango = JSConstructor(window.Cango2D)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

x1, y1 = 40, 20
cx1, cy1 = 90, 120
x2, y2 = 120, 100
cx2, cy2 = 130, 20
cx3, cy3 = 150, 120
x3, y3 = 180, 60

def dragC1(mousePos):
    global cx1, cy1
    cx1 = mousePos.x
    cy1 = mousePos.y
    drawCurve()

def dragC2(mousePos):
    global cx2, cy2
    cx2 = mousePos.x
    cy2 = mousePos.y
    drawCurve()

def dragC3(mousePos):
    global cx3, cy3
    cx3 = mousePos.x
    cy3 = mousePos.y
    drawCurve()

def drawCurve():
    # curve change shape so it must be re-draw each time
    # draw a quadratic bezier from x1,y2 to x2,y2
    qbez = obj2d(['M', x1, y1, 'Q', cx1, cy1, x2, y2], "PATH",  {
          "strokeColor":'blue'})
    cbez = obj2d(['M', x2, y2, 'C', cx2, cy2, cx3, cy3, x3, y3], "PATH",  {
          "strokeColor":'green'})
    # show lines to control point
    L1 = obj2d(['M', x1, y1, 'L', cx1, cy1, x2, y2], "PATH", {
      "strokeColor":"rgba(0, 0, 0, 0.2)",
      "dashed":[4]})  # semi-transparent gray
    L2 = obj2d(['M', x2, y2, 'L', cx2, cy2], "PATH", {
      "strokeColor":"rgba(0, 0, 0, 0.2)",
      "dashed":[4]})
    L3 = obj2d(['M', x3, y3, 'L', cx3, cy3], "PATH", {
      "strokeColor":"rgba(0, 0, 0, 0.2)",
      "dashed":[4]})
    # draw draggable control points CangoAnimation-3v01.js
    c1.transform.reset()
    c1.transform.translate(cx1, cy1)
    c2.transform.reset()
    c2.transform.translate(cx2, cy2)
    c3.transform.reset()
    c3.transform.translate(cx3, cy3)
    grp = cgo.createGroup2D(qbez, cbez, L1, L2, L3, c1, c2, c3)
    cgo.renderFrame(grp)

cgo.clearCanvas("lightyellow")
cgo.setWorldCoords(0, 0, 200)

# draggable control points
c1 = obj2d(shapedefs.circle(4), "SHAPE", {"fillColor":'red'})
c1.enableDrag(None, dragC1, None)
c2 = c1.dup()
c2.enableDrag(None, dragC2, None)
c3 = c1.dup()
c3.enableDrag(None, dragC3, None)
drawCurve();
</script>
'''
    return outstring

@bg99.route('/fourchain')
def fourchain():
    outstring = '''
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-200, -200, 400, 400) 

#畫座標軸線

cgo.drawAxes(0, 200, 0, 100, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 10,
    "xLabelInterval": 20,
    "yTickInterval": 10,
    "yLabelInterval": 10})

deg = math.pi/180

#選擇長弧, 且向內畫弧
def chain1(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "black",
            "lineWidth": linewidth })
    # 尺寸放大兩倍
    cgo.render(cmbr, x, y, 2, rot)
    cgo.drawText("1-長向內", x, y-10, {"fontSize":10, "fontWeight": 1200, "lorg":5 })

# 選擇短弧, 且向內畫弧
def chain2(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 0, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "black",
            "lineWidth": linewidth })
    # 尺寸放大兩倍
    cgo.render(cmbr, x, y, 2, rot)
    cgo.drawText("2-短向內", x, y-10, {"fontSize":10, "fontWeight": 1200, "lorg":5 })

#選擇長弧, 且向外畫弧
def chain3(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 1, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "black",
            "lineWidth": linewidth })
    # 尺寸放大兩倍
    cgo.render(cmbr, x, y, 2, rot)
    cgo.drawText("3-長向外", x, y-30, {"fontSize":10, "fontWeight": 1200, "lorg":5 })

#選擇短弧, 且向外畫弧
def chain4(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 0, 1, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "black",
            "lineWidth": linewidth })
    # 尺寸放大兩倍
    cgo.render(cmbr, x, y, 2, rot)
    cgo.drawText("4-短向外", x, y-30, {"fontSize":10, "fontWeight": 1200, "lorg":5 })

yellow = "#f4c20d"
white = "#ffffff"
chain1(0, 0, 0, 0, 0, white, True, 4)
chain2(35, 0, 0, 0, 0, white, True, 4)
chain3(70, 0, 0, 0, 0, white, True, 4)
chain4(105, 0, 0, 0, 0, white, True, 4)
</script>
'''
    return outstring
    
    
