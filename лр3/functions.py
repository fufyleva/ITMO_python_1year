from PIL import Image, ImageSequence # фото
import customtkinter as ctk
import pygame  # музыка
pygame.mixer.init()   # включает аудиосистему. выполняется один раз при импорте файла


def animated_gif(app, gif_path):
    frames = [ctk.CTkImage(light_image=f.copy(), size=(150, 150)) # все кадры гифки
              for f in ImageSequence.Iterator(Image.open(gif_path))]

    label = ctk.CTkLabel(app, image=frames[0], text="")  # где будут картинки
    label.place(x=120, y=520)

    def next_frame(n=0):
        label.configure(image=frames[n])  # меняем текущую картинку на следующую из frames
        app.after(80, next_frame, (n + 1) % len(frames))  # через каждые 80мс закускаем функцию снова.
        # (n + 1) % len(frames) за счет остатка от деления мы получаем вечный механизм получения картинок

    next_frame()
    return label


def sound(app, sound_path, btn_color_normal, btn_color_select):
    def is_playing():
        if pygame.mixer.music.get_busy():  # играет ли что-то?
            pygame.mixer.music.stop()
            btn_play_stop.configure(text='play') # переписать
        else:
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play(loops=-1)  # -1 бесконечная игра
            btn_play_stop.configure(text='stop')

    btn_play_stop = ctk.CTkButton(app, text='play',
                                  font=ctk.CTkFont(size=25),
                                  width=200, height=50,
                                  fg_color=btn_color_normal,
                                  command=is_playing)
    return btn_play_stop


def stop_music_exit():
    pygame.mixer.music.stop()   # для стопа музыки при выхода из приложения

def error_destroy(app):
    try:
        app.destroy()  # 1. окно умирает само — все команды виджетов удаляются корректно
    finally:
        for job in list(app.tk.call("after", "info")):  # 2. добить очередь заданий мёртвого окна
            try:
                app.after_cancel(job)
            except Exception:
                pass
