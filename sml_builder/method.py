from os import listdir
from flask import render_template, url_for
from json import loads
from _jsonnet import evaluate_file
from sml_builder import app

status_class = {"Prototype": "pending", "Complete": "success"}


@app.route("/method/<method>")
def display_method(method):
    page_data = loads(evaluate_file(f"./content/methods/{method}.jsonnet"))
    page_data["method_metadata"]["Status"] = statusify(
        page_data["method_metadata"]["Status"]
    )
    return render_template("method.html", page=page_data)


@app.route("/methods")
def display_methods():
    methods = []
    methods_dir = "./content/methods"
    for file in listdir(methods_dir):
        method = loads(evaluate_file(f"{methods_dir}/{file}"))
        methods.append(
            {
                "tds": [
                    {
                        "value": f'<a href="{url_for("display_method", method=file.split(".")[0])}">{method["title"]}</a>'
                    },
                    {"value": method["method_metadata"]["Theme"]},
                    {"value": method["method_metadata"]["Expert group"]},
                    {"value": method["method_metadata"]["Programming language"]},
                    {"value": method["method_metadata"]["Access type"]},
                    {"value": statusify(method["method_metadata"]["Status"])},
                ]
            }
        )
    return render_template("methods.html", page={"rows": methods})


def statusify(status):
    return f'<span class="ons-status ons-status--{status_class.get(status, "info")}">{status}</span>'
