# TODO Найдите количество книг, которое можно разместить на дискете
disk_capacity_mb = 1.44
pages_in_book = 100
lines = 50
chars = 25
bytes_per_char = 4
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024
book_size = pages_in_book * lines * chars * bytes_per_char
books_fit = disk_capacity_bytes // book_size
print("Количество книг, помещающихся на дискету:", int(books_fit))
