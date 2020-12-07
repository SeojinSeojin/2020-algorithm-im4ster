from flask import Flask, render_template, request, redirect
from backtrack_victory import get_victory_percentage
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
        vp = get_victory_percentage(result)
        return render_template("result.html", vp=vp, cl=result)


if __name__ == "__main__":
    app.run(debug=True)
