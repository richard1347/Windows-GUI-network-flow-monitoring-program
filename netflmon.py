import socket,psutil,time,tkinter
from PIL import Image,ImageTk

def network_state():
    bytessentBefore=psutil.net_io_counters(pernic=True)['ETHERNET'].bytes_sent                      #Replace 'ETHERNET' with your network connection's name whether it's wired or wireless
    psutil.net_io_counters()
    bytesrecvBefore=psutil.net_io_counters(pernic=True)['ETHERNET'].bytes_recv
    time.sleep(1)

    bytessentAfter=psutil.net_io_counters(pernic=True)['ETHERNET'].bytes_sent
    bytesrecvAfter=psutil.net_io_counters(pernic=True)['ETHERNET'].bytes_recv

    sent_rate=bytessentAfter-bytessentBefore
    recv_rate=bytesrecvAfter-bytesrecvBefore

    if sent_rate<1024 and recv_rate<1024:
        print('Sent: '+str(sent_rate)+' B/s')
        print('Recv: '+str(recv_rate)+' B/s')
        upFlowLabel.configure(text=str(sent_rate)+' B/s')
        downFlowLabel.configure(text=str(recv_rate)+' B/s')
        mainWindow.after(1000, network_state)
    elif sent_rate > 1024 or recv_rate > 1024:
        sent_rate=round((bytessentAfter-bytessentBefore) / 1024, 1)
        recv_rate=round((bytesrecvAfter-bytesrecvBefore) / 1024, 1)
        print('Sent: '+str(sent_rate)+' kB/s')
        print('Recv: '+str(recv_rate)+' kB/s')
        upFlowLabel.configure(text=str(sent_rate) + ' kB/s')
        downFlowLabel.configure(text=str(recv_rate) + ' kB/s')
        mainWindow.after(1000, network_state)
    else:
        sent_rate=round((bytessentAfter-bytessentBefore) / 1024 / 1024, 1)
        recv_rate=round((bytesrecvAfter-bytesrecvBefore) / 1024 /1024 , 1)
        print('Sent: '+str(sent_rate)+' MB/s')
        print('Recv: '+str(recv_rate)+' MB/s')
        upFlowLabel.configure(text=str(sent_rate) + ' MB/s')
        downFlowLabel.configure(text=str(recv_rate) + ' MB/s')
        mainWindow.after(1000, network_state)

if __name__=='__main__':
    mainWindow=tkinter.Tk()
    mainWindow.title('NetFlow Monitor')
    mainWindow.iconbitmap('netmon2.ico')
    #define your UI window's position according to your screen size and position
    print(f"Your screen size: {mainWindow.winfo_screenwidth(),mainWindow.winfo_screenheight()}")
    mainWindow.geometry('270x70-20-20')
    mainWindow.resizable(False,False)

    upFlowLabel=tkinter.Label(mainWindow,fg='green',font=("Arial", 12))
    upFlowLabel.grid(row=0, column=1)
    downFlowLabel=tkinter.Label(mainWindow,fg='blue',font=("Arial", 12))
    downFlowLabel.grid(row=1, column=1)

    img_open1=Image.open('up.png')
    img_png1=ImageTk.PhotoImage(img_open1)
    upFlowImage=tkinter.Label(mainWindow,relief=tkinter.GROOVE,width=30,image=img_png1)
    upFlowImage.grid(row=0,column=0)

    img_open2=Image.open('down.png')
    img_png2=ImageTk.PhotoImage(img_open2)
    downFlowImage=tkinter.Label(mainWindow,relief=tkinter.GROOVE,width=30,image=img_png2)
    downFlowImage.grid(row=1,column=0)

    network_state()
    mainWindow.mainloop()