# charge_api
the python server for smart charge

本程序为应用于智能充电桩的`微信支付接口服务端`程序，结合设备端使用可实现生成任意收款金额二维码，支持扫码支付功能

- 爬取第三方网站`微信支付二维码`生成网站API与二维码图片
- 部署于服务器上进行二维码图片爬取与分辨率，格式转换，并开发`获取`、`查询`API 
- 终端设备（野火STM32开发板）触摸屏的bmp图像驱动显示程序修改[支持1bit位深]与开发
- 终端设备使用W5500网络模块接入网络并访问服务端API

