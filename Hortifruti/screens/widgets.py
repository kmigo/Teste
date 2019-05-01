# -*- coding: utf-8 -*-

#import libs
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.metrics import dp

from kivymd.card import MDCard
from kivymd.textfields import MDTextField
from kivymd.label import MDLabel


accord_kv = """
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
<Accord@Screen>:
	
	name:'accordion'
	BoxLayout:

        MDAccordion:
            orientation: 'vertical'
            size_hint_x: None
            width: '240dp'

            MDAccordionItem:
                title:'ESTOQUE'
                icon: 'home'
                MDAccordionSubItem:
                    text: "Estoque"
                MDAccordionSubItem:
                    text: "Entrada de produto"
                    on_release:root.obj.show_input_product()
                MDAccordionSubItem:
                    text: "Saida de produto"
                MDAccordionSubItem:
                	text: "Inventario"
            MDAccordionItem:
                title:'CADASTRO'
                icon: 'clipboard-text'
                MDAccordionSubItem:
                    text: "Produtos"
                MDAccordionSubItem:
                    text: "Cliente"
                MDAccordionSubItem:
                    text: "Fornecedor"
            MDAccordionItem:
                title:'FINANCEIRO'
                icon: 'bank'
                MDAccordionSubItem:
                    text: "Contas a pagar"
                MDAccordionSubItem:
                    text: "Contas a receber"
                MDAccordionSubItem:
                    text: "Movimentação do caixa"
                    
		BoxLayout:
			Button:
				id:bt
				text:app.page_before[1]
				on_release:root.page()
		
"""

input_product_kv = """
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import images_path kivymd.images_path
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDLabel kivymd.label.MDLabel
#:import MDSwiperManager kivymd.managerswiper.MDSwiperManager
#:import MDTextField kivymd.textfields.MDTextField
#:import Window kivy.core.window
#:import MDRaisedButton kivymd.button.MDRaisedButton



<InputProduct@Screen>:
	name:'input_product'
	BoxLayout:
		orientation:'vertical'
		id:box
		#ScreenManager:
#			id:ip_manager
#			Devolu:
#		BoxLayout:
#			id:box
#			size_hint_y:.3
#			padding:10
#			orientation:'vertical'
#			canvas:
#				Color:
#					rgba:.5,.5,.1,.3
#				Rectangle:
#					size:self.size
#					pos:self.pos
#			BoxLayout:
#				padding:dp(5)
#				orientation:'vertical'
#				
#				MDSwiperManager:
#					id:swiper_manager
#					
#					Screen:
#						name:'devo'
#						BoxLayout:
#							id:scr1
#					Screen:
#						name:'Compra'
#						id:scr2
#					
#					Screen:
#						name:'bonifi'
#						id:scr3

		
<InputProductDev>:
	text:'Devolução'
	scr_name:'dev'
	BoxLayout:
		orientation:'vertical'
		padding:dp(5)
		BoxLayout:
			size_hint_y:.1
			canvas:
				Color:
					rgba:.3,.3,.1,.8
			
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[20]
			MDLabel:
				text:root.text.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
		
		BoxLayout:
			orientation:'vertical'
			padding:dp(7)
			
			MyCard:
				elevation:10
				BoxLayout:
					spacing:dp(10)
					orientation:'vertical'
					padding:dp(15)
					FieldText:
						hint_text:'Cod. do produto'
						
						
					FieldText:
						hint_text:'Quantidade'
						
					
					TextValor:
						hint_text:'Preço'
						
					
					MyCard:
						size_hint_y:None
						height:dp(100)
						
						BoxLayout:
							ScrollView:
								GridLayout:
									orientation:'vertical'
									size_hint_y:None
									height:self.minimum_height
									id:grid_ip
									cols:4
					
					MyCard:
						BoxLayout:
							MDLabel:
								text:'Desconto: '
								halign:'center'
								font_style:'Title'
							
							MDLabel:
								text:'R$ 0,00'
								halign:'center'
								font_style:'Title'
			
					
					Screen:
						MDRaisedButton:
							
							text:'gerar'
							pos_hint:{'center_x':.5,'center_y':.5}
						
				
				
		
		BoxLayout:
			size_hint_y:.1
			canvas.before:
				Color:
					rgba:.3,.3,.1,.8
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[50,]
			MDLabel:
				text:''.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
			MDLabel:
				text:'compra'.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				font_style:'Body2'
			MDLabel:
				text:'>'.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				font_style:'Title'
			
		
		
 
<InputProductCom>:
	
	text:'Compra'
	scr_name:'com'
	BoxLayout:
		orientation:'vertical'
		padding:dp(5)
		BoxLayout:
			size_hint_y:.1
			canvas:
				Color:
					rgba:.3,.3,.1,.8
			
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[20]
			MDLabel:
				text:root.text.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
		
		BoxLayout:
			orientation:'vertical'
			padding:dp(7)
			MyCard:
				elevation:10
				BoxLayout:
					spacing:dp(10)
					orientation:'vertical'
					padding:dp(15)
					FieldText:
						hint_text:'Cod. do produto'
						
						
					FieldText:
						hint_text:'Quantidade'
						
					
					TextValor:
						hint_text:'Preço'
						
					
					MyCard:
						size_hint_y:None
						height:dp(100)
						
						BoxLayout:
							ScrollView:
								GridLayout:
									orientation:'vertical'
									size_hint_y:None
									height:self.minimum_height
									id:grid_ip
									cols:4
					
					MyCard:
						BoxLayout:
							MDLabel:
								text:'Total: '
								halign:'center'
								font_style:'Title'
							
							MDLabel:
								text:'R$ 0,00'
								halign:'center'
								font_style:'Title'
					Screen:
						MDRaisedButton:
							text:'comprar'
							pos_hint:{'center_x':.5,'center_y':.5}
		
		BoxLayout:
			size_hint_y:.1
			canvas.before:
				Color:
					rgba:.3,.3,.1,.8
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[50,]
			MDLabel:
				text:'<'.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				font_style:'Title'
			MDLabel:
				text:'Devolução'.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				font_style:'Body2'
			MDLabel:
				text:'Bonificação'.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				font_style:'Body2'
				
			MDLabel:
				text:'>'.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				font_style:'Title'
		
				
					
<InputProductBon>:
	text:'Bonificação'
	scr_name:'bon'
	BoxLayout:
		padding:dp(5)
		orientation:'vertical'
		BoxLayout:
			size_hint_y:.1
			canvas:
				Color:
					rgba:.3,.3,.1,.8
			
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[20]
			MDLabel:
				text:root.text.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
		
		BoxLayout:
			orientation:'vertical'
			padding:dp(7)
			MyCard:
				elevation:10
				BoxLayout:
			
					
		
		BoxLayout:
			size_hint_y:.1
			canvas.before:
				Color:
					rgba:.3,.3,.1,.8
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[50,]
			MDLabel:
				text:'<'.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				font_style:'Title'
			MDLabel:
				text:'compra'.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				font_style:'Body2'
			MDLabel:
				text:''.upper()
				halign:'center'
				theme_text_color: 'Custom'
				text_color:(1,1,1,1)
				bold:True
				

<Devolu>:
	name:'dev'
	Button:

<Bonifi>:
	name:'bon'
	text:'troco'
	
		
		
"""



class Screens(object):
	
	accordion = None
	input_product = None
	
	def show_accord(self):
		if not self.accordion:
			Builder.load_string(accord_kv)
			self.accordion = Accord(self)
			self.ids.scr_mngr.add_widget(self.accordion)
			self.ids.scr_mngr.current='accordion'
			
		else:
			self.ids.scr_mngr.current = 'accordion'
			
			
			
			
	def show_input_product(self):
		from kivymd.managerswiper import MDSwiperPagination
		if not self.input_product:
			Builder.load_string(input_product_kv)
			self.input_product = InputProduct()
			self.ids.scr_mngr.add_widget(self.input_product)
			
			App.get_running_app(
			).page_before=['input_product',
			'Entr. de produtos']
			carousel=Carousel()
			carousel.add_widget(InputProductDev(self))
			carousel.add_widget(InputProductCom(self))
			carousel.add_widget(InputProductBon(self))
			self.input_product.ids.box.add_widget(carousel)
			self.ids.scr_mngr.current = 'input_product'
			
			
	
		
		else:
			self.ids.scr_mngr.current = 'input_product'
			App.get_running_app(
			).page_before=['input_product',
			'Entrada de produtos']
	

		
	
	def page_before(self):
		self.ids.scr_mngr.current=App.get_running_app(
		).page_before[0]
		
		
class InputProduct(Screen):
	pass

class Accord(Screen):
	def __init__(self,obj,**kwargs):
		super(Accord,self).__init__(**kwargs)
		self.obj = obj
		
	def on_pre_enter(self):
		self.ids.bt.text=App.get_running_app().page_before[1]
	
	def page(self):
		self.obj.page_before()


class InputProductDev(Screen):
	text = StringProperty('')
	scr_name = StringProperty('')
	colums=['N.','Nome','Uni.','R$']
	
	def __init__(self,obj,**kwargs):
		super(InputProductDev,self).__init__(**kwargs)
		self.obj=obj
		self.colums_bar()
		
	def on_pre_enter(self):
		self.obj.ids.ip_manager.add_widget(Devolu())
		self.obj.ids.ip_manager.current = 'dev'
	
	def colums_bar(self):
		for cada in self.colums:
			self.ids.grid_ip.add_widget(MDLabel(
			text=cada,
			halign='center',
			size_hint=(None,None),
			size=(dp(70),dp(50))))
		


class InputProductCom(Screen):
	text = StringProperty('')
	scr_name = StringProperty('')
	colums=['N.','Nome','Uni.','R$']
	def __init__(self,obj,**kwargs):
		super(InputProductCom,self).__init__(**kwargs)
		self.obj=obj
		self.colums_bar()
	
	def colums_bar(self):
		for cada in self.colums:
			self.ids.grid_ip.add_widget(MDLabel(
			text=cada,
			halign='center',
			size_hint=(None,None),
			size=(dp(70),dp(50))))

class InputProductBon(Screen):
	text = StringProperty('')
	scr_name = StringProperty('')
	
	def __init__(self,obj,**kwargs):
		super(InputProductBon,self).__init__(**kwargs)
		self.obj=obj
	
	def on_pre_enter(self):
		self.obj.ids.ip_manager.add_widget(Bonifi())
		self.obj.ids.ip_manager.current= 'bon'


class FieldText(MDTextField):
	pass


class TextValor(MDTextField):
	def __init__(self,**kwargs):
		super(TextValor,self).__init__(**kwargs)
		self.nv=''
		self.input_filter='int'
	def on_focus(self,instance,value):
		
		nv=''

			
		if value :
			for c in self.text:
				if c.isdigit():
					nv+=c
			self.text=nv
			self.hint_text=''
			
			
			
		if not value:
			for c in self.text:
				if c.isdigit():
					nv+=c
			
			
		
			if len(nv) == 1 and int(nv) > 0:
				self.text='R$'+nv+',00'
				self.nv=float(nv)
			if len(nv) == 2 and int(nv) >0:
				self.text='R$'+nv[:1]+','+nv[1:]
				self.nv=float(nv[:1]+'.'+nv[1:])
			
			if len(nv) == 3 and int(nv) > 0:
				self.text='R$'+nv[:2]+','+nv[2:]
				self.nv=float(nv[:2]+'.'+nv[2:])
			
			if len(nv) > 0:
				if int(nv[0]) == 0:
					self.text='R$'+nv[0]+','+nv[1:]
					self.nv=float(nv[0]+'.'+nv[1:])
			
			if len(nv) == 4 and int(nv[0]) >0:
				self.text = 'R$'+nv[:2]+','+nv[2:]
				self.nv=float(nv[:2]+'.'+nv[2:])
			
			if len(nv) == 5 or len(nv) == 6 and int(nv[0]) >0:
				self.text = 'R$'+nv[:3]+','+nv[3:]
				self.nv=float(nv[:3]+'.'+nv[3:])
				
			if len(nv) == 7 and int(nv[0]) >0:
				self.text = 'R$'+nv[:3]+','+nv[3:6]+'.'+nv[6:]
				self.nv=float(nv[:4]+'.'+nv[4:])
			
			if len(nv) > 7 and int(nv[0]) >0:
				self.text = 'R$'+nv[:3]+','+nv[3:6]+'.'+nv[6:]
				self.nv=float(nv[:4]+'.'+nv[4:])
			
			
				
			
			
		
		
				
		
	
		
	

class MyCard(MDCard):
	pass
		
	

