@app.route("/predict", methods = ['POST', 'GET'])
# def predictPage():
#     try:
#         if request.method == 'POST':
#             to_predict_dict = request.form.to_dict()

#             for key, value in to_predict_dict.items():
#                 try:
#                     to_predict_dict[key] = int(value)
#                 except ValueError:
#                     to_predict_dict[key] = float(value)

#             to_predict_list = list(map(float, list(to_predict_dict.values())))
#             pred = predict(to_predict_list, to_predict_dict)
#     except:
#         message = "Please enter valid data"
#         return render_template("home.html", message=message)

#     return render_template('predict.html', pred=pred)



# import logging

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)
