SVG:ScalableVectorGraph，可缩放矢量图。  

# 艰难的问题
给定一堆图片，要求把这些图片转成svg格式，并且要求生成的svg尽量小。 
如果直接使用base64，最终生成的svg肯定比较大。  

# 一个icon网站
基于SVG可以做许多有趣的事情，main.py实现了一个生成svg的接口，使用这个接口，可以生成字符图标。  
运行python main.py，访问http://127.0.0.1:5000/?text=我&color=black&background=yellow  即可查看图标。

# 教程
* [w3school]( https://www.w3school.com.cn/svg/svg_example.asp)
* [mdn](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Tutorial)  
  * [SVG元素参考](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Element)  
  * SVG属性参考：https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute
* 菜鸟网：https://www.runoob.com/svg/svg-rect.html  


# SVG相关网站
* http://www.heropatterns.com/  
使用svg作为背景，在这个网站上可以挑选背景图案，生成CSS。   
* https://philiprogers.com/svgpatterns/#halfrombes   
05-svg-patterns是这个网页的备份。  
* http://svg-wow.org/

# svg编辑器
https://c.runoob.com/more/svgeditor/  
http://www.zuohaotu.com/svg/  

# svg库
* svg优化：https://www.npmjs.com/package/svgo  
