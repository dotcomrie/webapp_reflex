import reflex as rx

class UserInfo(rx.model, table=True):
    email: str