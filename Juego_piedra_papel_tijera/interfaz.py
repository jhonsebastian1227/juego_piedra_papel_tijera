# Importaciones
import customtkinter as ctk, random, os
from PIL import Image


# configuraciones iniciales de customtkinter
ctk.set_appearance_mode('systen')
ctk.set_default_color_theme('blue')


# Configuracion de fuentes
fuente_titulo = ('Calibri', 32, "bold")
fuente_btn = ('Calibri', 14, "bold")
fuente_ganador = ('Calibri', 22,)


# Buscar capeta de ubicacion de imagenes
carpeta_principal = os.path.dirname(__file__)
carpeta_img = os.path.join(carpeta_principal, 'img')


# configuracion de imagenes
ancho_img = 120
alto_img = 120
piedra_img = ctk.CTkImage(light_image=Image.open((os.path.join(carpeta_img, 'piedra.png'))), size=(ancho_img, alto_img))
papel_img  = ctk.CTkImage(light_image=Image.open((os.path.join(carpeta_img, 'papel.png'))), size=(ancho_img, alto_img))
tijera_img = ctk.CTkImage(light_image=Image.open((os.path.join(carpeta_img, 'tijera.png'))), size=(ancho_img, alto_img))


# Creacion de una clase para crear ventanas automaticas
class Inicio:
    def __init__(self, nombre_ventana, titulo_ventana, dimenciones):
        # configuraciones iniciales de las ventanas
        self.ventana = ctk.CTk()
        self.ventana.title(f'{nombre_ventana}')
        self.ventana.geometry(f'{dimenciones}')
        self.ventana.resizable(0,0)
        self.ventana.grab_set()
        
        # boton para llamar a la funcion de crear ventana de juego e instruciones
        ctk.CTkButton(self.ventana,
                      text=f"Jugar",
                      width=170,
                      font=fuente_ganador,
                      command=self.arrancar_juego,
                      ).pack(anchor='center', padx=(10,10), pady=(160,0))
        ctk.CTkButton(self.ventana,
                      text=f"Instruciones",
                      width=170,
                      font=fuente_ganador,
                      command=self.mostrar_instruciones,
                      ).pack(anchor='center', padx=(10,10), pady=(10,0))
        # bucle
        self.ventana.mainloop()
    
    # funcion para crear la ventana de juego
    def arrancar_juego(self):
        self.ventana.destroy()
        juego = Juego('Juego', 'Piedra, papel o tijera', '350x400+120+120')
    def mostrar_instruciones(self):
        instrucines.iniciando_intruciones()


class Juego:
    def __init__(self, nombre_ventana, titulo_ventana, dimenciones):
        # configuraciones iniciales de las ventanas
        self.ventana = ctk.CTk()
        self.ventana.title(f'{nombre_ventana}')
        self.ventana.geometry(f'{dimenciones}')
        self.titulo_ventana = titulo_ventana
        self.contador_jugador = 0
        self.contador_computador = 0
        
        # Titulo pincipal
        ctk.CTkLabel(self.ventana,
                     text=f'{titulo_ventana}',
                     font=fuente_titulo,
                     ).pack(pady=(15,25))
        
        # marco de imagenes y otro widgets
        marco = ctk.CTkFrame(self.ventana,
                             border_width=1,
                             corner_radius=10
                             )
        marco.pack()
        
        # texto de jugadores
        ctk.CTkLabel(marco,
                     text='Jugador',
                     ).grid(row=0, column=0, pady=(3,0))
        ctk.CTkLabel(marco,
                     text='Computadora',
                     ).grid(row=0, column=1, pady=(3,0))
        
        # imagenes
        self.jugador = ctk.CTkLabel(marco,
                                    image=papel_img,
                                    text='',
                                    )
        self.jugador.grid(row=1, column=0, padx=(10,10))
        self.computadora = ctk.CTkLabel(marco,
                                        image=papel_img,
                                        text='',
                                        )
        self.computadora.grid(row=1, column=1, padx=(10,10))
        
        # puntos de los jugadores
        self.puntos_jugador = ctk.CTkLabel(marco,
                                           text='0',
                                           font=fuente_ganador,
                                           )
        self.puntos_jugador.grid(row=2, column=0, pady=(10,1))
        self.puntos_computador = ctk.CTkLabel(marco,
                                              text='0',
                                              font=fuente_ganador,
                                              )
        self.puntos_computador.grid(row=2, column=1, pady=(10,1))
        
        # marco para botones y label
        marco_btn = ctk.CTkLabel(self.ventana,
                                 text='',
                                 )
        marco_btn.pack()
        
        # label para mostar si ganaste, perdiste o empate
        self.respuesta_ganador = ctk.CTkLabel(marco_btn,
                                              text='Pulse un boton\n🆚',
                                              font=fuente_ganador,
                                              )
        self.respuesta_ganador.grid(row=0, columnspan=3, pady=(10,0))
        
        # botones piedra papel y tijera
        nombre_btn = {'Piedra': lambda: self.estado_boton(1),
                      'Papel' : lambda: self.estado_boton(2),
                      'Tijera': lambda: self.estado_boton(3),
                      }
        pos_column = 0
        for key, value in nombre_btn.items():
            ctk.CTkButton(marco_btn,
                          text=f"{key}",
                          width=80,
                          command=value,
                          font=fuente_btn,
                          ).grid(row=2, column=pos_column, padx=(10,10), pady=(15,0))
            pos_column += 1
            
        # bucle
        self.ventana.mainloop()
    
    # funcion para establecer el ganador
    def estado_boton(self, texto):
        aleatorio = random.randint(1,3)
        dic = {1: piedra_img,
               2: papel_img,
               3: tijera_img,
               }
        
        self.jugador.configure(image=dic[texto])
        self.computadora.configure(image=dic[aleatorio])
        
        if texto == aleatorio:
            self.respuesta_ganador.configure(text='Empate\n💤')
        elif (texto == 1 and aleatorio == 3 or
              texto == 2 and aleatorio == 1 or
              texto == 3 and aleatorio == 2
              ):
            self.contador_jugador += 1
            self.puntos_jugador.configure(text=self.contador_jugador)
            self.respuesta_ganador.configure(text='Ganaste\n😎')
        else:
            self.contador_computador += 1
            self.puntos_computador.configure(text=self.contador_computador)
            self.respuesta_ganador.configure(text='Perdiste\n💀')


class Instrucines:
    def iniciando_intruciones(self):
        # configuraciones iniciales de las ventanas
        ventana = ctk.CTkToplevel()
        ventana.title('Intruciones')
        ventana.geometry('350x400+120+120')
        #ventana.resizable(0,0)
        ventana.grab_set()
        mensaje = '''"¡Bienvenido al juego de Piedra,\nPapel y Tijera! En este emocionante juego,\ntu objetivo es vencer a la computadora\neligiendo sabiamente entre tres opciones:\n'Piedra', 'Papel' y 'Tijera'.\nSelecciona el botón 'Piedra'\npara elegir esa opción y aplastar las tijeras.\nUtiliza el botón 'Papel' para envolver la piedra y ganar.\nSi prefieres cortar el papel, elige el botón 'Tijera'.\n¡Juega varias rondas y que la suerte te acompañe!\nDiviértete jugando."'''
        
        # label de instruciones
        ctk.CTkLabel(ventana,
                     text=mensaje,
                     justify='center',
                     ).pack(padx=(10,10), pady=(15,0))
        
        # boton para salir de las instruciones
        ctk.CTkButton(ventana,
                      text=f"Salir",
                      width=80,
                      command=lambda: ventana.destroy(),
                      font=fuente_btn,
                      ).pack(padx=(10,10), pady=(20,0))


instrucines = Instrucines()
