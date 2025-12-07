import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text(value="История приветствий:")

    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            for line in f:
                greeting_history.append(line.strip())
    except:
        pass

    history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
   

    favorite_names = []
    favorites_text = ft.Text(value="Любимые имена:")

    def save_history_to_file(text):
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")

    # greeting_text.value = 'Привет'
    # greeting_text.color = ft.Colors.GREEN
    
    def on_button_click(_):
        # print(name_input.value)
        name = name_input.value.strip()
        
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None

            record = f"{timestamp} - {name}"
            greeting_history.append(record)

            save_history_to_file(record)

            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

        # print(greeting_text)
        page.update()

    def add_to_favorites(_):
        if greeting_history:
            last_name = greeting_history[-1].split(" - ")[-1]
            favorite_names.append(last_name)
            favorites_text.value = "Любимые имена:\n" + "\n".join(favorite_names)
            page.update

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    button_text = ft.TextButton(text='send', on_click=on_button_click)
    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        print(greeting_history)
        greeting_history.clear()
        history_text.value = 'История приветствий:'

    def sort_history(_):
        greeting_history.sort(key=lambda x: x.split(" - ")[-1].lower())

        history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        page.update()





        open("history.txt", "w").close()

        page.update()
        print(greeting_history)
    
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    favorite_button = ft.ElevatedButton(text='⭐ В избранное', on_click=add_to_favorites)

    sort_button = ft.ElevatedButton(text="Сортировать по алфавиту", on_click=sort_history)

    # page.add(greeting_text, name_input, button_text, history_text )

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        view_greeting_text,
        ft.Row([name_input, button_elevated, clear_button]),
        history_text,
        favorite_button,
        sort_button,
        favorites_text
    )


ft.app(target=main)