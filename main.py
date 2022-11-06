import flet
from flet import *
from flet import colors,icons

class Childapp(UserControl):
	def __init__(self,username,deleteparent):
		super().__init__()
		self.username = username
		self.deleteparent = deleteparent
	def build(self):
		self.nama = Text(value=self.username,size=30)
		self.editanddeleteBtn = Row([
			IconButton(icon=icons.CREATE_OUTLINED,
				icon_color=colors.BLUE,
				icon_size=30,
				on_click=self.editbtn
				),
			IconButton(icon=icons.DELETE,
				icon_color=colors.RED,
				icon_size=30,
				on_click=self.deleteBtn
				),
			])
		self.textforUpadate = TextField(
			visible=False,
			width=120,
			value=self.nama.value,
			)
		self.btnUpdate = ElevatedButton("update",
			visible=False,
			on_click=self.saveBtnEdit)
		return Column(
			controls=[
				Row([
					self.textforUpadate,
					self.nama,
					self.editanddeleteBtn,
					self.btnUpdate
					],alignment="spaceEvenly")
			],alignment="center"
			)
		
	def editbtn(self,e):
		self.textforUpadate.visible = True
		self.nama.visible = False
		self.editanddeleteBtn.visible = False
		self.btnUpdate.visible = True
		self.nama.value = self.textforUpadate.value
		self.update()
	def saveBtnEdit(self,e):
		self.textforUpadate.visible = False
		self.nama.visible = True
		self.editanddeleteBtn.visible = True
		self.btnUpdate.visible = False
		self.nama.value = self.textforUpadate.value
		self.update()

	def deleteBtn(self,e):
		self.deleteparent(self)

class Homeapp(UserControl):
	def build(self):
		self.name = TextField(label="Username")
		self.listdata = Column()
		return Column(
			[
			Row(
			controls=[
			self.name,
			FloatingActionButton(
				bgcolor=colors.BLUE,
				icon=icons.ADD,
				on_click=self.addtask,
				),
			]
			),
			self.listdata
			]

			)
	def addtask(self,e):
		self.listdata.controls.append(
			Childapp(self.name.value,self.deleteparent)
			)
		self.update()

	def deleteparent(self,task):
		self.listdata.controls.remove(task)
		self.update()

def main(page:Page):
	page.update()
	Home = Homeapp()
	page.add(Home)
		


flet.app(target=main)
