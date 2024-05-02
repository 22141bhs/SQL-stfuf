import sqlite3

def print_all_cars():
    speed = input()
    db = sqlite3.connect('cars.db')
    cursor = db.cursor()
    sql = "SELECT * FROM car;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for car in results:
        print(f"Car: {car[1]} | Top Speed: {car[2]} mph")
    db.close()

if __name__ == "__main__": 
    print_all_cars()
    print("Hello")