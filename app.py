from flask import request, render_template  # khong co s
from flask import Flask
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def ketquaxs():
    list_id = [
        "rs_0_0",
        "rs_1_0",
        "rs_2_0",
        "rs_2_1",
        "rs_3_0",
        "rs_3_1",
        "rs_3_2",
        "rs_3_3",
        "rs_3_4",
        "rs_3_5",
        "rs_4_0",
        "rs_4_1",
        "rs_4_2",
        "rs_4_3",
        "rs_5_0",
        "rs_5_1",
        "rs_5_2",
        "rs_5_3",
        "rs_5_4",
        "rs_5_5",
        "rs_6_0",
        "rs_6_1",
        "rs_6_2",
        "rs_7_0",
        "rs_7_1",
        "rs_7_2",
        "rs_7_3",
    ]
    ses = requests.Session()
    r = ses.get("http://ketqua.net")
    result = 'xin lỗi bạn đã tạch lo'
    tree = BeautifulSoup(markup=r.text)

    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form.get("fname")
        for id_reward in list_id:
            node = tree.find(attrs={"id": id_reward})
            num = node.text
            if name == num[-2:]:
                if id_reward == "rs_0_0":
                    result = "bạn trúng lô với số {} giải đặc biệt".format(
                        num[-2:])
                    return render_template("index.html", result=result)
                else:
                    result = "bạn trúng lô với số {} là giải {}".format(
                        num[-2:], id_reward[3]
                    )
                    return render_template("index.html", result=result)
        return render_template("index.html", result=result)


# @app.route("/api")


if __name__ == "__main__":
    app.run(debug=True)
