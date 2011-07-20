#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Jul 14 06:22:35 2011

import wx

# begin wxGlade: extracode
# end wxGlade

class ServerData():
    pass


class ServerAdd(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ServerAdd.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.StatusBar = self.CreateStatusBar(1, 0)
        self.Servers = wx.StaticText(self, -1, "Servers")
        self.ServerList = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.static_line_1 = wx.StaticLine(self, -1)
        self.ServerName = wx.StaticText(self, -1, "ServerName")
        self.ServerNameText = wx.TextCtrl(self, -1, "")
        self.URL = wx.StaticText(self, -1, "URL")
        self.URLText = wx.TextCtrl(self, -1, "")
        self.Username = wx.StaticText(self, -1, "Username")
        self.UsernameText = wx.TextCtrl(self, -1, "")
        self.Password = wx.StaticText(self, -1, "Password")
        self.PasswordText = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.static_line_2 = wx.StaticLine(self, -1)
        self.Save = wx.Button(self, -1, "Save")
        self.Remove = wx.Button(self, -1, "Remove")
        self.AddNew = wx.Button(self, -1, "AddNew")
        self.Quit = wx.Button(self, -1, "Quit")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnServerList, self.ServerList)
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.Save)
        self.Bind(wx.EVT_BUTTON, self.OnRemove, self.Remove)
        self.Bind(wx.EVT_BUTTON, self.OnAddNew, self.AddNew)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.Quit)
        # end wxGlade
         
        self.__populate_URL_List(self.ServerList)

    def __set_properties(self):
        # begin wxGlade: ServerAdd.__set_properties
        self.SetTitle("AddServer")
        self.SetSize((422, 250))
        self.StatusBar.SetStatusWidths([-1])
        # statusbar fields
        StatusBar_fields = ["StatusBar"]
        for i in range(len(StatusBar_fields)):
            self.StatusBar.SetStatusText(StatusBar_fields[i], i)
        self.Servers.SetMinSize((90, 17))
        self.ServerList.SetMinSize((189, 29))
        self.ServerName.SetMinSize((90, 20))
        self.ServerNameText.SetMinSize((189, 25))
        self.URL.SetMinSize((90, 20))
        self.URLText.SetMinSize((189, 25))
        self.Username.SetMinSize((90, 20))
        self.UsernameText.SetMinSize((189, 25))
        self.Password.SetMinSize((90, 20))
        self.PasswordText.SetMinSize((189, 25))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ServerAdd.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.Servers, 0, 0, 0)
        sizer_2.Add(self.ServerList, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_3.Add(self.ServerName, 0, 0, 0)
        sizer_3.Add(self.ServerNameText, 0, 0, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_4.Add(self.URL, 0, 0, 0)
        sizer_4.Add(self.URLText, 0, 0, 0)
        sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.Username, 0, 0, 0)
        sizer_5.Add(self.UsernameText, 0, 0, 0)
        sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add(self.Password, 0, 0, 0)
        sizer_6.Add(self.PasswordText, 0, 0, 0)
        sizer_1.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizer_7.Add(self.Save, 0, 0, 0)
        sizer_7.Add(self.Remove, 0, 0, 0)
        sizer_7.Add(self.AddNew, 0, 0, 0)
        sizer_7.Add(self.Quit, 0, 0, 6)
        sizer_1.Add(sizer_7, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def __populate_URL_List(self, ComboBox):
    	f = open('serverList.txt','r')
        lines = f.readlines()
        self.servers = {}
        for line in lines:
            row = line.split()
            print 'row =' 
            print row
            if(len(row) == 4) :
                servername = row[0]
                url = row[1]
                username = row[2]
                password = row[3]
                serverdata = ServerData()
                serverdata.servername = servername
                serverdata.url = url
                serverdata.username = username
                serverdata.password = password
                self.servers[servername] = serverdata
                name = row[0]+" "+row[1]
                print 'yoyo '+name
                ComboBox.Append(name)
        f.close()
        print self.servers
        
    def __update_URL_List(self):
        self.ServerList.Clear()
        for k,v in self.servers.iteritems():
            name = v.servername+" "+v.url
            self.ServerList.Append(name)
        
    def OnSave(self, event): # wxGlade: ServerAdd.<event_handler>
        #print "Event handler `OnSave' not implemented"
        newServerName = self.ServerNameText.GetValue()
        if(self.servers.has_key(newServerName)):
            print 'Server Name already exists'
            return
            
        newUrl = self.URLText.GetValue()
        newUserName = self.UsernameText.GetValue()
        newPassword = self.PasswordText.GetValue()
        
        serverData = ServerData()
        #self.ServerList.Append(newServerName+" "+newUrl)
        
        url = newUrl.split()
        if(len(newUrl) != 0 and len(newServerName) != 0 and len(newUserName) !=0 and len(newPassword) != 0 ):
            serverData.servername = newServerName
            serverData.url = newUrl
            serverData.username = newUserName
            serverData.password = newPassword
            self.servers[newServerName] = serverData
            f = open('serverList.txt','a')
            f.write(newServerName+" "+newUrl+ " "+newUserName+" "+newPassword+"\n")
            f.close()
            self.selectedURL = newUrl
            print self.selectedURL
            print self.servers
            self.__update_URL_List()
  	    #Update_Url_List(newServerName+" "+newUrl)
        else:
            print "Please Fill all the fields"
        event.Skip()

    def OnRemove(self, event): # wxGlade: ServerAdd.<event_handler>
        serverName = self.ServerNameText.GetValue()
        if(len(serverName) > 0):
            print self.servers
            del self.servers[serverName]
            self.__update_URL_List()
            self.ServerNameText.Clear()
            self.PasswordText.Clear()
            self.URLText.Clear()
            self.UsernameText.Clear()
            print self.servers
        else:
            print 'No server selected'
        #print "Event handler `OnRemove' not implemented"
        
        event.Skip()

    def OnAddNew(self, event): # wxGlade: ServerAdd.<event_handler>
        #print "Event handler `OnAddNew' not implemented"
        self.ServerNameText.Clear()
        self.PasswordText.Clear()
        self.URLText.Clear()
        self.UsernameText.Clear()
        event.Skip()

    def OnQuit(self, event): # wxGlade: ServerAdd.<event_handler>
        out = open('serverList.txt','w')
        for k,v in self.servers.iteritems():
            out.write(v.servername+" "+v.url+" "+v.username+" "+v.password+"\n")
        #print "Event handler `OnQuit' not implemented"
        event.Skip()

    def OnServerList(self, event): # wxGlade: ServerAdd.<event_handler>
        #print self.ServerList.CurrentSelection
        url = self.ServerList.GetValue()
        print 'here'
        print url
        urlarr = url.split()
        print urlarr
        print self.servers
        if(len(urlarr)==2):
            self.selectedServer = self.servers[urlarr[0]]
            print self.selectedServer
            self.ServerNameText.SetValue(self.selectedServer.servername)
            self.URLText.SetValue(self.selectedServer.url)
            self.UsernameText.SetValue(self.selectedServer.username)
            self.PasswordText.SetValue(self.selectedServer.password)
        else:
            print "Wrong format of URL selected"
            
        #self.ServerNameText.SetValue(self.servers)
        print "Event handler `OnServerList' not implemented"
        event.Skip()

# end of class ServerAdd

def AddServerFrame():
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = ServerAdd(None, -1, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = ServerAdd(None, -1, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
