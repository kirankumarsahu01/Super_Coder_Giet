class table:
    def _init_(self) -> None:
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None

dining_table=table()
back_table=table()
front_table=back_table
back_table=dining_table
print(dining_table," ",back_table," ",front_table)
print("the id of dinning_table :",id(dining_table))
print("the id of front_table :",id(front_table))
print("the id of back_table :",id(front_table))




