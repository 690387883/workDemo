import wx
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="第一个python应用",size=(300,200),pos=(300,300))
        panel = wx.Panel(parent = self)  # 创建一个面板
        contaniner=wx.BoxSizer(wx.VERTICAL)
        self.title=wx.StaticText(parent=panel,label="Hello,world!")
        btnBox=wx.BoxSizer(wx.HORIZONTAL)
        save = wx.Button(parent=panel,label="保存")
        cancel = wx.Button(parent=panel,label="取消")
        btnBox.Add(save,proportion=1)
        btnBox.Add(cancel,proportion=1)
        contaniner.Add(self.title,proportion=1,flag=wx.ALIGN_CENTER|wx.ALL,border=10)
        contaniner.Add(btnBox,proportion=1,flag=wx.ALIGN_CENTER|wx.ALL,border=10)
        panel.Bind(wx.EVT_BUTTON,self.save,save)
        panel.Bind(wx.EVT_BUTTON,self.cancel,cancel)
        panel.SetSizer(contaniner)
    def save(self,event):
        self.title.SetLabelText("保存成功")
    def cancel(self,event):
        self.title.SetLabelText("取消成功")        

app=wx.App()
frame=MyFrame()
frame.Show()
app.MainLoop()