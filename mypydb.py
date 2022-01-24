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


''' Payments Table '''
id_col = IdColumn()
customer_id_col = IntColumn('customer_id')
payment_type_col = VarcharColumn('payment_type', length=45, nullable=False)
details_col = TextColumn('details')
created_by_id_col = CreatedByIdColumn()
created_at_col = CreatedAtColumn()
updated_at_col = UpdatedAtColumn()

table = Table('payments')
payments_columns = [id_col, customer_id_col, payment_type_col, details_col, created_by_id_col, created_at_col, updated_at_col]
table.set_columns(payments_columns)
payments_table_sql = table.get_create_table_sql()

print(payments_table_sql)