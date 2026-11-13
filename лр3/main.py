import customtkinter as ctk
from PIL import Image
import generate
import functions

def main():
    app = ctk.CTk()
    app.geometry('400x500+0+0') # позиция у левого верхнего угла
    app.title('Игры HoYoverse')
    app.resizable(False, False) # нельзя поменять размер
    ctk.set_appearance_mode("Dark")

    def open_game(game_name: str, # открываем второй экран
                  img_path: str,gif_path: str, sound_path: str,
                  color_btn_normal: str,
                  color_btn_select: str):
        functions.error_destroy(app) # разрушаем экран
        generate.generate_screen(game_name,  # открываем 2 экран
                                 img_path, gif_path, sound_path,
                                 color_btn_normal,color_btn_select)
    def game(name: str, # само окна с играми
             img_path: str, gif_path: str, sound_path: str,
             top_place_img: int,
             color_btn_normal: str, color_btn_select: str):

        img = ctk.CTkLabel(app, image=ctk.CTkImage(dark_image=Image.open(img_path),
                                                   size=(150, 150)), text='')

        btn = ctk.CTkButton(app, text=name,
                            font=ctk.CTkFont(size=25),
                            width=200, height=150,
                            fg_color=color_btn_normal, hover_color=color_btn_select,
                            command=lambda: open_game(name, img_path, gif_path, sound_path,
                                                      color_btn_normal, color_btn_select))

        img.place(x=20, y=top_place_img + 20)
        btn.place(x=190, y=top_place_img + 20)

    game('Genshin Impact',
         'genshin.png', 'genshin_gif.gif', 'genshin_music.mp3',
         0,
         '#008B8B',
         '#40E0D0')
    game('Honkai: Star Rail',
         'hsr.png', 'hsr_gif.gif', 'hsr_misic.mp3',
         170,
         '#DDA0DD', '#DA70D6')

    btn_exit = functions.exit_btn(app, '#1E90FF')
    btn_exit.place(relx=0.5, y=420, anchor='center')

    app.mainloop()


if __name__ == "__main__":  # мы импортировали main или нет
    main()
