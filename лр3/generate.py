import customtkinter as ctk
from string import ascii_uppercase
from random import randint
from PIL import Image
import functions

def generate_screen(game_name: str,
                    img_path: str, gif_path: str, sound_path: str,
                    color_btn_normal:str,
                    color_btn_select:str):
    app = ctk.CTk()
    app.geometry("400x700+0+0")
    app.title(game_name)
    app.resizable(False, False)
    ctk.set_appearance_mode("Dark")

    img = ctk.CTkLabel(app,
                       image=ctk.CTkImage(light_image=Image.open(img_path), size=(150, 150)),
                       text='')

    title = ctk.CTkLabel(app, text=game_name, font=ctk.CTkFont(size=20, weight='bold'))
    code_box = ctk.CTkTextbox(app, width=250, height=30,
                              font=ctk.CTkFont(size=15))

    title.place(relx=0.5, y=20, anchor="center")
    img.place(relx=0.5, y=120, anchor="center")
    code_box.place(relx=0.5, y=330, anchor="center")

    def open_main():
        functions.error_destroy(app)
        import main
        main.main()

    def generate_code():
        res_str = ''
        for i in range(3):
            indexes_for_numbers = set()
            while len(indexes_for_numbers) != 2:
                indexes_for_numbers.add(randint(0, 5))
            for j in range(6):
                if j in indexes_for_numbers:
                    res_str += str(randint(0, 9))
                else:
                    res_str += str(ascii_uppercase[randint(0, 25)])
            if i != 2:
                res_str += '-'
        code_box.delete('0.0', 'end') # начиная с 0.0 и до конца удаляем
        code_box.tag_config("center", justify="center") # создаем тег (текст посередине)
        code_box.insert('0.0', res_str, 'center') # теперь используем этот тег

    btn_generate_code = ctk.CTkButton(app, text='generate code', font=ctk.CTkFont(size=25),
                        width=200, height=40,
                        fg_color=color_btn_normal,
                        command=generate_code)


    btn_exit = functions.exit_btn(app, color_btn_normal)
    btn_back = ctk.CTkButton(app, text='back',
                            font=ctk.CTkFont(size=25),
                            width=20, height=10,
                            fg_color=color_btn_normal,
                            command=open_main)

    btn_play_stop_music = functions.sound(app, sound_path,
                                          color_btn_normal, color_btn_select)


    btn_back.place(x=10, y=10)
    btn_exit.place(relx=0.5, y=420, anchor="center")
    btn_generate_code.place(relx=0.5, y=250, anchor="center")
    btn_play_stop_music.place(relx=0.5, y=480, anchor="center")

    functions.animated_gif(app, gif_path)

    app.mainloop()
