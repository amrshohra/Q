from flet import Page, AppBar, Text, Column, colors, alignment, app, run

def main(page: Page):
    page.title = "الشهرة لتوصيل الإعلانات"
    page.appbar = AppBar(title=Text("الشهرة لتوصيل الإعلانات", color=colors.BLACK), bgcolor=colors.BLUE)
    page.add(
        Column(
            [
                Text(
                    "لنشر إعلانك أبعِت رسالة على رقم\n01001954254",
                    size=28,
                    color=colors.BLACK,
                    weight="w600",
                    text_align="center",
                )
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True,
        )
    )
