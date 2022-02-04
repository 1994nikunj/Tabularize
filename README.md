# tabularize

Tabularize is a Python library for generating simple tables. It was inspired by the [PrettyTable](https://pypi.org/project/prettytable/) library in python. We can control many aspects of a table, such as the width of the column padding, the alignment of text, or the table border.
It's a trimmed-down version of PrettyTable with even simpler implementation and lightness in terms of library resources.

#### _SAMPLE INPUT CODE:_
    import tabularize

    cols = ('Id', 'Name', 'Age', 'Occupation', 'DateCreated (epoch)')
    table = Tabularize(column_names=cols, right_padding=1, title="Title: Sample Table")
    table.add_row(row=[1, 'Mr. A', 27, 'IT, Software Developer', time.time()])
    table.add_row(row=[2, 'Ms. B', 23, 'Human Resource, Recruiting', time.time()])
    table.add_row(row=[3, 'Mr. C', 23, 'Banking, International Business', time.time()])
    table.add_row(row=[4, 'Mrs. D', 18, 'Student, College', time.time()])
    table.add_row(row=[5, 'Ms. E', 17, 'Student, College', time.time()])
    table.add_row(row=[6, 'Mrs. F', 12, 'Student, School', time.time()])

    table.generate_table()
    
#### _SAMPLE OUTPUT:_
    +---------------------------------------------------------------------------+
    | Title: Sample Table                                                       |
    +----+--------+-----+---------------------------------+---------------------+
    | Id | Name   | Age | Occupation                      | DateCreated (epoch) |
    +----+--------+-----+---------------------------------+---------------------+
    | 1  | Mr. A  | 27  | IT, Software Developer          | 1643943461.0770793  |
    | 2  | Ms. B  | 23  | Human Resource, Recruiting      | 1643943461.0770793  |
    | 3  | Mr. C  | 23  | Banking, International Business | 1643943461.0770793  |
    | 4  | Mrs. D | 18  | Student, College                | 1643943461.0770793  |
    | 5  | Ms. E  | 17  | Student, College                | 1643943461.0770793  |
    | 6  | Mrs. F | 12  | Student, School                 | 1643943461.0770793  |
    +----+--------+-----+---------------------------------+---------------------+