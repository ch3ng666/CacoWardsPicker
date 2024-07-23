import flet as ft
import random as rnd
import re


def main(page: ft.Page):

    page.window.width = 1240
    page.window.height = 905
    page.bgcolor = 'black'
    page.window.resizable = False
    page.window.maximizable = False
    title = ft.Text('Random CACOWARD Picker',
                    weight='bold',
                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE))

    def randomize(e):
        rnd_number = rnd.randint(1, len(list_column.controls))
        random_number.value = str(rnd_number)
        random_year.value = list_pure[rnd_number - 1][:4]
        index = list_pure[rnd_number - 1].index('http')
        random_title.value = list_pure[rnd_number - 1][7:index-2]
        random_url.value = list_pure[rnd_number - 1][index:]
        random_url.visible = True
        random_number.update()
        random_year.update()
        random_title.update()
        random_url.update()

    random_number = ft.Text(weight='bold')
    random_year = ft.Text()
    random_title = ft.Text()
    random_url = ft.TextButton('Download',
                               on_click=lambda e: page.launch_url(
                                   random_url.value),
                               visible=False)

    generate_button_text = ft.Text('Randomize', color='white', weight='bold')
    generate_button = ft.OutlinedButton(content=generate_button_text,
                                        width=320,
                                        style=ft.ButtonStyle(
                                            side=ft.BorderSide(1,
                                                               'white'),
                                            shape=ft.RoundedRectangleBorder(0)),
                                        on_click=randomize
                                        )

    list_column = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=825, spacing=1)

    def checkbox_change(e):
        with open('1994-2023.txt', 'r', encoding='utf-8') as played:
            read_played = played.readlines()
            label = e.control.label
            indexl = label.index(' - ')
            if e.control.value:
                read_played[int(label[:indexl])-1] = f'{label[indexl+3:]} - 1\n'  # nopep8
                e.control.label_style = ft.TextStyle(color='indigo', size=12)
                e.control.update()
            else:
                read_played[int(label[:indexl])-1] = f'{label[indexl+3:]} - 0\n'  # nopep8.
                e.control.label_style = ft.TextStyle(color='white', size=12)
                e.control.update()

        with open('1994-2023.txt', 'w', encoding='utf-8') as played:
            played.writelines(read_played)

    def generator(e):
        list_column.controls.clear()
        with open('1994-2023.txt', 'r') as wadlist:
            global list_pure
            list_pure = []
            for i in enumerate(wadlist):
                list_row = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=880)
                condition = True if i[1][-2] == '1' else False
                color = 'indigo' if condition else 'white'
                list_row.controls.append(
                    ft.Checkbox(
                        label=f'{len(list_column.controls)+1} - {i[1][:-5]}',  # nopep8
                        active_color='indigo',
                        label_style=ft.TextStyle(color=color, size=12),
                        on_change=checkbox_change,
                        value=condition

                    )

                )
                index = i[1].index('http')

                list_row.controls.append(ft.TextButton(
                    url=i[1][index: -5], text='D'))
                list_column.controls.append(list_row)
                list_pure.append(i[1][:-5])

    generator(e=None)

    def search_constructor(e, value):
        with open('1994-2023.txt', 'r') as wadlist:
            search_list_column.controls.clear()
            for i in enumerate(wadlist):
                if value not in i[1].lower():
                    continue
                search_list_row = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=880)
                condition = True if i[1][-2] == '1' else False
                color = 'indigo' if condition else 'white'
                search_list_row.controls.append(
                    ft.Checkbox(
                        label=f'{i[0]+1} - {i[1][:-5]}',  # nopep8
                        active_color='indigo',
                        label_style=ft.TextStyle(color=color, size=12),
                        on_change=checkbox_change,
                        value=condition
                    )
                )
                index = i[1].index('http')

                search_list_row.controls.append(ft.TextButton(
                    url=i[1][index: -5], text='D'))
                search_list_column.controls.append(search_list_row)
        page.update()

    def search(e):
        if search_stack not in page.overlay:
            page.overlay.append(search_stack)

        search_constructor(e, search_field.value)
        page.update()

    def search_close(e):
        page.overlay.remove(search_stack)
        generator(e=None)
        page.update()

    search_list_column = ft.Column(
        scroll=ft.ScrollMode.ALWAYS, spacing=1)

    search_stack = ft.Stack(controls=[
        ft.Container(
            search_list_column,
            blend_mode=ft.BlendMode.SRC,
            bgcolor='#ff151515',
            alignment=ft.alignment.top_center,
            width=880,
            height=825,
        ),
        ft.TextButton('CLOSE SEARCH', icon=ft.icons.CLOSE,
                      on_click=search_close, bottom=820)
    ],
        alignment=ft.alignment.bottom_right,
        right=4,
        bottom=1,
        height=870
    )

    search_box = ft.Row(
        [
            search_field := ft.TextField(hint_text='Search',
                                         width=270,
                                         border_color='white',
                                         height=35),
            ft.IconButton(icon=ft.icons.SEARCH,
                          on_click=search)
        ]

    )

    Command_Column = ft.Column(
        [search_box, generate_button,
            random_number, random_year, random_title, random_url],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    page.add(
        ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [
                Command_Column, list_column
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=10),
    )


ft.app(target=main)
