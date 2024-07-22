import flet as ft
import random as rnd


def main(page: ft.Page):

    page.window.width = 1240
    page.window.height = 905
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

    with open('1994-2023.txt', 'r') as wadlist:
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
            list_row.controls.append(ft.TextButton('D'))
            list_column.controls.append(list_row)
            list_pure.append(i[1][:-5])

    Command_Column = ft.Column(
        [generate_button, random_number, random_year, random_title, random_url],
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
