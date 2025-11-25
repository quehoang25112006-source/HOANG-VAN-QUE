print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
###################################
class Bank:
    """Class mô phỏng tài khoản ngân hàng và các chức năng ATM cơ bản."""
    def __init__(self, name, account_Number, balance=0):
        """Phương thức khởi tạo."""
        self.name = name
        self.account_Number = account_Number
        self.balance = balance
        self.account_type = "Savings"
        self.location = "Guntur"
    def deposit(self):
        """Phương thức nạp tiền."""
        # Nhận số tiền nạp từ người dùng (ép kiểu sang float)
        amount = float(input("Please Enter Desired Amount to Deposit: ")) 
        self.balance += amount
        print("Your transaction is successful!")
        print(f"Current Balance: {self.balance}")
    def withdraw(self):
        """Phương thức rút tiền."""
        # Nhận số tiền rút từ người dùng (ép kiểu sang float)
        amount = float(input("Please Enter Desired Amount to Withdraw: "))
        # Kiểm tra số dư
        if amount > self.balance:
            print("Your transaction is cancelled due to insufficient amount in account!")
        else:
            self.balance -= amount
            print("Your transaction is successful!")
            print(f"Current Balance: {self.balance}")
    def balance_inquiry(self):
        """Phương thức kiểm tra số dư."""
        print(f"Current Balance for account {self.account_Number}: {self.balance}")       
    def __repr__(self):
        """Phương thức in thông tin đối tượng."""
        return f"Account Name: {self.name}, Account Number: {self.account_Number}, Balance: {self.balance}"
# 1. Khởi tạo tài khoản
t1 = Bank("HOANG VAN QUE ", 245752021610045, 5000)
# In thông tin ban đầu của tài khoản
print("\n--- Ban đầu ---")
print(t1) # Gọi tự động __repr__
# 2. Ví dụ giao dịch:
# Nạp tiền
t1.deposit() 
# Rút tiền
t1.withdraw() 
# Kiểm tra số dư
t1.balance_inquiry() 
# In số dư cuối cùng (gọi __repr__)
print(f"Current Balance for account {t1.account_Number}: {t1.balance}")
