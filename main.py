from flask import Flask,
render_template

app = flask('app')

@app.route('/')
def index():
  return
  render_template("index.html")


@app.route('/')
def index():
  return
  render_template("delivery.html")


@app.route('/')
def index():
  return
  render_template("feedbacks.html")

@app.route('/')
def index():
  return
  render_template("locations.html")


@app.route('/')
def index():
  return
  render_template("products.html")