from flask import *
import os
import random
import sqlite3

app = Flask(__name__)

tech = ['Абсцисса,', 'Аддитивность,', 'Логистическая регрессия,', 'Линейная регрессия,', 'Аксонометрия,', 'Асимптота,', 'Бином,', 'Деференты,', 'Дистрибутивность,', 'Дифференциал,', 'Скаляр,', 'Итерация,', 'Логарифм,', 'Мультипликативность,Нормаль,', 'Нормальное распределение,', 'Рекуррентный,', 'Квантовая механика,', 'Нейтрон,', 'Спектр,', 'Фаза,', 'Фотон,', 'Векторный потенциал,', 'Пассивная инертность,', 'Производная,']
gum = ['Антитеза,', 'Хронотоп,', 'Аспект,', 'Дескрипция,', 'Эпитет,', 'Метафора,', 'Гиперболa,', 'Лингвистика,', 'Морфология,', ',Риторика,', 'Просвещение,', 'Романтизм,', 'Борроко,', 'Возрождение,', 'аллод,', 'оммаж,', 'социализация,', 'индустриализация,', 'геронтократия,', 'нуменклатура,']

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        try:
            type = request.form['tg']
            cmt1 = request.form['cmt1']
            cmt2 = request.form['cmt2']
        except:
            return render_template("main.html", error="Вы не ответили на все вопросы", tech=random.choice(tech)[:-1], gum=random.choice(gum)[:-1])
        cnn = sqlite3.connect("data")
        cur = cnn.cursor()
        cur.execute("INSERT INTO Data (Type, Cmt1, Cmt2) VALUES ('{0}', '{1}', '{2}')".format(type, cmt1, cmt2))
        cnn.commit()
        return render_template("thanks.html")
    return render_template("main.html", tech=random.choice(tech)[:-1], gum=random.choice(gum)[:-1])

app.secret_key = os.urandom(24)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)