from src.lib.columns import Column, DoubleColumn, IdColumn, IntColumn, TextColumn, VarcharColumn
from src.lib.columns.commons import CreatedAtColumn, CreatedByIdColumn, UpdatedAtColumn
from src.lib.tables import Table
from src.lib.tables.users import UsersTable
from src.lib.tables.brands import BrandsTable
from src.lib.tables.categories import CategoriesTable


''' Brands Column Table '''

brands_table = BrandsTable('brands')
brands_sql = brands_table.get_create_table_sql()
print("\nBrands:", brands_sql)


''' Users Table '''

users_table = UsersTable('users')
users_sql = users_table.get_create_table_sql()
print("\nUsers:", users_sql)


''' Categories Table '''

categories_table = CategoriesTable('categories')
categories_sql = categories_table.get_create_table_sql()
print("\nCategories:", categories_sql)