import punto_fijo
import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

TITLE_SIZE = 40
SUBTITLE_SIZE = 23
STRING_SIZE = 18
COLUMN_SPAN = 4

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Proyecto final - Métodos numéricos")
        self.geometry("1200x850")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        ###########################
        # Create navigation frame #
        ###########################

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Métodos \ndisponibles", compound="center", font=customtkinter.CTkFont(size=SUBTITLE_SIZE, weight="bold"))

        self.navigation_frame_label.grid(row=0, column=0, padx=50, pady=(40,30))


        self.punto_fijo_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Punto fijo",font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w", command=self.punto_fijo_button_event)

        self.punto_fijo_button.grid(row=1, column=0, sticky="ew")


        self.gauss_seidel_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Gauss-Seidel",font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w", command=self.gauss_seidel_button_event)

        self.gauss_seidel_button.grid(row=2, column=0, sticky="ew")


        self.biseccion_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Bisección",font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.biseccion_button_event)

        self.biseccion_button.grid(row=3, column=0, sticky="ew")


        ###########################
        # Create punto_fijo frame #
        ###########################

        self.punto_fijo_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.punto_fijo_frame.grid_columnconfigure(3, weight=1)

        self.punto_fijo_title = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Punto Fijo", compound="center", font=customtkinter.CTkFont(size=TITLE_SIZE, weight="bold"))

        self.punto_fijo_title.grid(row=0, column=0, padx=0, pady=(70,20),sticky="nsew",columnspan=4)

        self.descripcion_punto_fijo = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Para calcular el punto fijo, se inserta el g(x) de la función despejada 'g(x) = x'. El número de iteraciones y el valor \ninicial son datos opcionales, ya que por defecto las iteraciones calculadas son 100 y el valor inicial se toma como\n el promedio de los extremos del intervalo, dejar en blanco en caso de no trabajar con ellos.",compound="left", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))

        self.descripcion_punto_fijo.grid(row=1, column=0, padx=0, pady=(20, 0),columnspan=4)


        self.descripcion_funcion_entry = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Ingrese la función en Python*",compound="left", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.descripcion_funcion_entry.grid(row=2, column=0, padx=20, pady=(50,0))

        self.funcion_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame,width=300,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.funcion_entry.grid(row=3, column=0, padx=30, pady=(0,30))
        #self.funcion_entry.place(relx=0.2, rely=0.35, anchor=tkinter.CENTER)

        # self.extremo_izquierdo_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame, placeholder_text="Extremo *",width=100,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        # self.funcion_entry.grid(row=2, column=1, padx=30, pady=30)
        #self.funcion_entry.place(relx=0.2, rely=0.35, anchor=tkinter.CENTER)




        # Create second frame
        self.gauss_seidel_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Create third frame
        self.biseccion_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Select default frame
        self.select_frame_by_name("punto_fijo")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.punto_fijo_button.configure(fg_color=("gray75", "gray25") if name == "punto_fijo" else "transparent")
        self.gauss_seidel_button.configure(fg_color=("gray75", "gray25") if name == "gauss_seidel" else "transparent")
        self.biseccion_button.configure(fg_color=("gray75", "gray25") if name == "biseccion" else "transparent")

        # show selected frame
        if name == "punto_fijo":
            self.punto_fijo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.punto_fijo_frame.grid_forget()
        if name == "frame_2":
            self.gauss_seidel_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gauss_seidel_frame.grid_forget()
        if name == "biseccion":
            self.biseccion_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.biseccion_frame.grid_forget()

    def punto_fijo_button_event(self):
        self.select_frame_by_name("punto_fijo")

    def gauss_seidel_button_event(self):
        self.select_frame_by_name("gauss_seidel")

    def biseccion_button_event(self):
        self.select_frame_by_name("biseccion")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()