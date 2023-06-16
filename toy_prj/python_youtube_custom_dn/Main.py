import os
import subprocess
import time
import pytube
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter.font as tkFont


class App:
	def __init__(self, root):
		#	Store root in self
		self.root = root
                
		#	Default settings
		self.L = 1000
		self.H = 700
		root.title("Youtube Downloader")
		root.geometry(str(self.L) + "x" + str(self.H))

		
		#	GUI frame
		#		Button_1: 주소 입력 및 화질 받기
		self.lbl_1 = Label(root, text = "Youtube 주소",font=fontStyle)
		self.lbl_1.place(x = self.L/2 - 40, y = 20)

		
		self.txt_1 = Entry(root, width = self.L - 50, font=fontStyle)
		self.txt_1.place(x = 30, y = 60, height = 30)
		self.txt_1.insert(END, "https://www.youtube.com/watch?v=I5fpzGIeLmc")

		self.btn_1 = Button(root, text = "Youtube 다운로드 화질 확인", bg = 'white', command = self.button_1_Click, font=fontStyle)
		self.btn_1.place(x = self.L/2 - 270, y = 100, width = 500, height = 50)

		
		
		# self.btn_1.bind("<Button-1>", self.button_1_Click)
		#		LBL_2: 유튜브 영상 이름
		self.lbl_2 = Label(root, text = "Youtube 제목", font=fontStyle)
		self.lbl_2.place(x = 50, y = 185, width = self.L - 100)
		#		CBB_2: 화질 콤보 박스
		self.cbb_2 = Combobox(root, height = 20, font=fontStyle)
		self.cbb_2.place(x = 25, y = 190, width = self.L - 50, height = 50)
		#		Button_3: 다운로드 버튼
		self.btn_3 = Button(root, text = "다운로드", bg = 'white', command = self.button_3_Click, font=fontStyle)
		self.btn_3.place(x = self.L/2 - 100, y = 250, width = 200, height = 50)
		# self.btn_3.bind("<Button-1>", self.button_3_Click)
		#		Button_Q: 프로그램 종료
		self.btn_Q = Button(root, text = "종료", bg = 'white')
		self.btn_Q.place(x = self.L/2 - 50, y = self.H - 60, width = 100, height = 40)
		self.btn_Q.bind("<Button-1>", self.button_Q_Click)


	def button_1_Click(self):
		self.btn_1['bg'  ] = "lawn green"
		self.btn_1['text'] = "화질 확인 중"
		self.root.update()

		self.URL = self.txt_1.get()
		self.YT = pytube.YouTube(self.URL)
		self.YT.register_on_progress_callback(self.Progress_F)
		self.VD = self.YT.streams
		self.cbb_2['values'] = self.Construct_cbb_2()
		self.cbb_2.current(0)

		self.btn_1['bg'] = 'white'
		self.btn_1['text'] = "Youtube 다운로드 화질 확인"
		self.lbl_2['text'] = self.YT.title
		self.btn_3['bg'] = 'white'
		self.btn_3['text'] = "다운로드"
		self.root.update()


	def button_3_Click(self):
		self.btn_3['bg'  ] = "yellow"
		self.root.update()
		
		idx = self.cbb_2.current()
		#	Video with audio
		if (self.VD[idx].audio_codec):
			self.VD[idx].download("./Output/")

		#	Video without audio
		else:
			#	Download video
			idxv = idx
			self.VD[idxv].download(output_path = "./Output", filename = "video")
			#	Find best audio
			idx = 0
			abr = 0.0
			for i in range(len(self.VD)):
				flag = not self.VD[i].includes_video_track
				if (flag and self.VD[i].abr):
					abr_ = self.VD[i].abr
					abr_ = float(''.join(filter(str.isdigit, abr_)))	#	string to fload
					if (abr_ >= abr):
						idx = i
						abr = abr_
			#	Download audio
			idxa = idx
			self.VD[idxa].download(output_path = "./Output", filename = "audio")
			#	Combine video and audio
			extv = os.path.splitext(self.VD[idxv].default_filename)
			exta = os.path.splitext(self.VD[idxa].default_filename)
			extv = extv[1]
			exta = exta[1]
			subprocess.call(["ffmpeg", 
								"-i", "./Output/video" + extv, 
								"-i", "./Output/audio" + exta, 
								"-c", "copy", "./Output/" + self.VD[idxv].default_filename])
			os.remove("./Output/video" + extv)
			os.remove("./Output/audio" + exta)

		self.btn_3['bg'  ] = "lawn green"
		self.btn_3['text'] = "다운로드 완료"
		self.root.update()


	def button_Q_Click(self, event):
		self.root.destroy()

	def Construct_cbb_2(self):
		cbb_value = ()
		n = len(self.VD)
		for i in range(n):
			str_ = self.VD[i].type + ", "
			str_ = str_ + "화질: " + str(self.VD[i].resolution) + ", "
			#str_ = str_ + "FPS: " + str(self.VD[i]) + ", "
			str_ = str_ + "타입: " + str(self.VD[i].mime_type) + ", "
			if (not self.VD[i].includes_video_track):
				str_ = str_ + "음질: " + str(self.VD[i].abr) + ", "
			# str_ = str_ + "Audio: " + str(self.VD[i].audio_codec) + ", "
			#str_ = str_ + "itag: " + str(self.VD[i].itag)
			cbb_value = cbb_value + (str_, )
		return cbb_value


	def Progress_F(self, stream, chunk, bytes_remaining):
		self.btn_3['text'] = "{0:.3f}% 완료".format((1-bytes_remaining/stream.filesize)*100)
		self.root.update()



root = Tk()
fontStyle=tkFont.Font(family="Lucida Grande", size=20)
root.option_add("*TCombobox*Listbox*Font", fontStyle)
App(root)
root.mainloop()
