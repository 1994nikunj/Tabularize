#!/usr/bin/env python
#
# Copyright (c), Nikunj Sharma <1994nikunj@git.com>
# All rights reserved.
# With contribution(s) from: Nikunj Sharma

class Tabularize:
    def __init__(self,
                 field_names: list = None,
                 **kwargs):
        self.encoding = kwargs.get("encoding", "UTF-8")
        self.final_table = []

        # Data
        if field_names:
            self.field_names = field_names
        self.title = False

        # Padding and Spacing
        self.padding_width = 1
        self.left_padding_width = 0
        self.right_padding_width = 0
        self.even_spaced_columns = True

        # Table properties
        self.max_width = 0

        # Table draw characters
        self.vertical_char = "|"
        self.horizontal_char = "-"
        self.junction_char = "+"
        self.blank_space = " "

        # Table borders
        self.table_border_top = ''

    def generate_table(self) -> None:
        self.generate_top_border()
        if self.title:
            self.generate_title_column()
        self.generate_header_column()
        for x in self.final_table:
            print(x)

    def generate_top_border(self) -> None:
        self.max_width = max([len(str(x)) for x in self.field_names])
        _width = self.max_width + len(self.blank_space) * 2
        _table_border_top = self.junction_char.join([self.horizontal_char * _width for _ in self.field_names])
        self.table_border_top = self.junction_char + _table_border_top + self.junction_char
        self.final_table.append(self.table_border_top)

    def generate_title_column(self) -> None:
        # To be implemented in future
        pass

    def generate_header_column(self) -> None:
        temp_column_data = []
        for col in self.field_names:
            padding = self.blank_space * self.padding_width
            if len(col) < self.max_width:
                extra_space = self.blank_space * int(self.max_width - len(col))
                _col = padding + col + extra_space + padding
                temp_column_data.append(_col)
            else:
                _col = self.blank_space + col + self.blank_space
                temp_column_data.append(_col)
        _temp = self.vertical_char + self.vertical_char.join(temp_column_data) + self.vertical_char
        self.final_table.append(_temp)
        self.final_table.append(self.table_border_top)


if __name__ == '__main__':
    columns = ['Index', 'HostIpAddress', 'HostName', 'Timestamp']
    table = Tabularize(field_names=columns)
    table.generate_table()

    """
    +---------------+---------------+---------------+---------------+
    | Index         | HostIpAddress | HostName      | Timestamp     |
    +---------------+---------------+---------------+---------------+
    """
