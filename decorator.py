from datetime import date, datetime
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt

def log(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)

        username = os.getlogin()
        func_name = func.__name__
        formatted_date = date.today().strftime("%d-%m-%Y")
        formatted_time = datetime.datetime.now()
        
        if os.path.exists("logs.csv"):
            file_df = pd.read_csv('logs.csv')
            new_id = len(file_df)
            new_row = pd.DataFrame({
                'id': [new_id],
                'pc_username': [username],
                'function_name': [func_name],
                'Date in date.month.year': [formatted_date],
                'Time': [formatted_time]
            })
            new_row.to_csv('logs.csv', mode='a', header=False, index=False)
        else:
            df = pd.DataFrame({
                'id': [0],
                'pc_username': [username],
                'function_name': [func_name],
                'Date in date.month.year': [formatted_date],
                'Time': [formatted_time]
            })
            df.to_csv('logs.csv', index=False)

        return original_result
    return wrapper




class Price():
    def __init__(self):
        self.avocado = pd.read_csv('avocado.csv')
    @log
    def main(self):
        x = self.avocado['date'].tolist()
        y = self.avocado['price'].tolist()
        fig, ax = plt.subplots()
        ax.set_facecolor('#B3DCFD')
        plt.plot(x, y, label='Avocado', marker = 'o', color = 'white')
        plt.xlabel('Дата')
        plt.xticks(rotation = 'vertical')
        plt.ylabel('Стоимость')
        plt.title('Стоимость')
        plt.show()
    
    def __del__(self): 
        print("del done")
        
def main():
    price =Price()
    price.main()
if __name__ == "__main__":
    main()