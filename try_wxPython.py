import wx

app = wx.App()

frm = wx.Frame(None, title="Hello World")
st = wx.StaticText(frm, label="Hello World!")
font = st.GetFont()
st.SetFont(font)
frm.Show()

app.MainLoop()