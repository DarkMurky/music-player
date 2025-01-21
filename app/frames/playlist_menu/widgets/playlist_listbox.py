import tkinter as tk
from tkinter import ttk


class PlaylistListBoxWidget(ttk.Treeview):
    columns = ('song_name',)

    def __init__(self, container):
        super().__init__(container, columns=self.columns,
                         show='headings', height=8)
        self.heading('song_name', text='Song Name')

        self.grid(row=0, column=0, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(
            container, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
