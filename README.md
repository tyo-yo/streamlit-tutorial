# streamlit-tutorial

StremlitをWebで遊ぶチュートリアル。poetryで管理できる。

[今すぐアクセス！！](https://stormy-temple-75644.herokuapp.com)


デプロイ方法
```
# 初回のみ
heroku create
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python

# 変更ごとに
git push heroku master
```
