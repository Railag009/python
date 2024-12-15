class Client:
    def __init__(self, client_code, fio, deposit_date, deposit_amount, interest_rate):
        self.client_code = client_code
        self.fio = fio
        self.deposit_date = deposit_date
        self.deposit_amount = deposit_amount
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Клиент {self.fio}, код: {self.client_code}\nДата открытия: {self.deposit_date}\nРазмер вклада: {self.deposit_amount}\nПроцент по вкладу: {self.interest_rate}%"

  bank = Bank()




# Добавляем клиентов в банк
client1 = Client("C001", "Иван Иванов", "2023-01-01", 10000, 5)
client2 = Client("C002", "Мария Петрова", "2023-02-15", 15000, 6)
client3 = Client("C003", "Анна Сидорова", "2023-03-20", 8000, 4)

bank.add_client(client1)
bank.add_client(client2)
bank.add_client(client3)

# Показываем клиентов с вкладом больше 10000
bank.show_by_money(10000)

# Показываем информацию о клиенте с кодом C002
bank.show_by_code("C002")

# Показываем клиентов с процентом по вкладу больше 5%
bank.show_by_proc(5)
