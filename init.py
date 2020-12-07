from flask import Flask, render_template, request, redirect
from backtrack_victory import get_victory_percentage
import time
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html")


@app.route("/click")
def clickMode():
    return render_template("main-click.html")


@app.route("/postCard", methods=['POST'])
def post():
    result = []
    for key, value in request.form.items():
        # print(key, value)  # 입력받은 값들 확인
        result.append(value)
    print(result)
    if " " in result:
        return redirect("/")
    else:
        start=time.time()
        #result=['9H', '9S', '5S', '5H', '8C', '7S', '8H', '8D', '3H', '3D', '3S', 'AS', '7D', 'QS', 'JD']
        vp = float("%.2f"%(get_victory_percentage(result)*100))
        print(vp)
        print(time.time()-start)
        return render_template("result.html", vp=vp, cl=result)


if __name__ == "__main__":
    app.run(debug=True)
