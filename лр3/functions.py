from PIL import Image, ImageSequence # фото
import customtkinter as ctk
import pygame  # музыка
pygame.mixer.init()   # включает аудиосистему. выполняется один раз при импорте файла


def animated_gif(app, gif_path):
    imgs = [ctk.CTkImage(light_image=f.copy(), size=(150, 150)) # все кадры гифки
              for f in ImageSequence.Iterator(Image.open(gif_path))]

    img_box = ctk.CTkLabel(app, image=imgs[0], text="")  # где будут картинки
    img_box.place(x=120, y=520)

    def next_frame(n=0):
        img_box.configure(image=imgs[n])  # меняем текущую картинку на следующую из imgs
        app.after(80, next_frame, (n + 1) % len(imgs))  # через каждые 80мс закускаем функцию снова.
        # (n + 1) % len(imgs) за счет остатка от деления мы получаем вечный механизм получения картинок

    next_frame()
    return img_box


def sound(app, sound_path, btn_color_normal, btn_color_select): # сама кнопка
    def is_playing(): # что делает кнопка
        if pygame.mixer.music.get_busy():  # играет ли что-то?
            pygame.mixer.music.stop()
            btn_play_stop.configure(text='play music') # переписать
        else:
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play(loops=-1)  # -1 бесконечная игра
            btn_play_stop.configure(text='stop music')

    btn_play_stop = ctk.CTkButton(app, text='play music',
                                  font=ctk.CTkFont(size=25),
                                  width=200, height=50,
                                  fg_color=btn_color_normal,
                                  command=is_playing)
    return btn_play_stop


def error_destroy(app): # разрушаем экран не забывая про очистку журнала очереди
    try:
        app.destroy()  # удаляем окно
    finally:
        for job in list(app.tk.call("after", "info")):  # удаляем очередь
            try:
                app.after_cancel(job)
            except Exception:
                pass


def exit_btn(app, btn_color_normal): # кнопка выхода
    def exit_app():
        error_destroy(app) # удаляем окно
        pygame.mixer.music.stop() # стоп музыки
    btn_exit = ctk.CTkButton(app, text='Exit',
                                  font=ctk.CTkFont(size=25),
                                  width=200, height=50,
                                  fg_color=btn_color_normal,
                                  command=exit_app)
    return btn_exit