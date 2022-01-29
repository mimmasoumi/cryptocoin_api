from flask import Flask, Blueprint, request

from api.crawler import coin_detail

main = Blueprint("main", __name__)


@main.route("/coin", methods=["POST"])
def get_coin():
    res = request.get_json()
    coin_name = res["coin_name"]
    return {"detail": coin_detail(coin_name)}