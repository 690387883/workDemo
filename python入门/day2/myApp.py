import wx
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="第一个python应用",size=(300,200),pos=(300,300))
        panel = wx.Panel(parent = self)  # 创建一个面板
        self.panelText = wx.StaticText(parent=panel,label="Hello,world!",pos=(10,10))   # 放置静态文字
        button = wx.Button(parent=panel,label="切换",pos=(10,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,button)
        vbox=wx.BoxSizer(wx.VERTICAL)
        # ALIGN_CENTER 布局属性,proportion两个控件都占1水平分，
        vbox.Add(self.panelText,proportion=2,flag=wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.TOP,border=30)
        vbox.Add(button,proportion=1,flag=wx.EXPAND|wx.BOTTOM,border=10)
        panel.SetSizer(vbox)
    def on_click(self,event):
            self.panelText.SetLabelText("Goodbye,world!")