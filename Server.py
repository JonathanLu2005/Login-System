from flask import Flask, redirect, url_for, render_template, request, session
import random
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secretkey"
 
database = {
    "TESTING123" : {"Pincode" : "1111", "Password" : "discoideology"},
    "TESTING456" : {"Pincode" : "3636", "Password" : "clearance456"},
    "TESTING789" : {"Pincode" : "4545", "Password" : "notebookprice"}
    }

UserIDattempts = 3
PincodeAttempt = 1
PasswordAttempt = 3

@app.route("/", methods=["POST", "GET"])
def Welcome():
    global UserIDattempts
    global PincodeAttempt
    global PasswordAttempt

    UserIDattempts = 3
    PincodeAttempt = 1
    PasswordAttempt = 3
    
    return render_template("Welcome.html")

@app.route("/UserID", methods=["POST", "GET"])
def UserID():
    if request.method == "POST":
        UserID = request.form["UserID"]
        
        try:
            global x
            global name
            x = database[UserID]
            name = UserID

            return redirect(url_for("Pincode"))


        except:
            global UserIDattempts


            characterCount = len(UserID)

            if characterCount == 0:
                return render_template("UserID.html", message="That doesn't satisfy the characters required")
                

            UserIDattempts -= 1

            if UserIDattempts == 0:
                return redirect(url_for("MaxAttempts"))

            else:
                return render_template("UserID.html", error="Incorrect ID - Access denied")

    return render_template("UserID.html")

@app.route("/Pincode", methods=["POST", "GET"])
def Pincode():
    if request.method == "POST":
        global x
        y = x["Pincode"]
        Pincode = request.form["Pincode"]
        pincodeCount = len(Pincode)

        if pincodeCount == 0:
            return render_template("Pincode.html", message="That doesn't satisfy the digits required")
        
        if Pincode in y:
            return redirect(url_for("Password"))

        else:
            return redirect(url_for("MaxAttempts"))           

        
    return render_template("Pincode.html")

def NumGen():
    global x

    try:
      global z
      z = x["Password"]

    except:
      z = z

    global number1
    global number2
    global number3
    number1 = random.randint(1, len(z))
    number2 = random.randint(1, len(z))
    number3 = random.randint(1, len(z))

    global num1
    global num2
    global num3

    num1 = number1
    num2 = number2
    num3 = number3

    numbers = []
    numbers.extend([number1, number2, number3])

    duplication = []

    for i in numbers:
        if i not in duplication:
            duplication.append(i)

        else:
            NumGen()

@app.route("/Password", methods=["POST", "GET"])
def Password():
  try:
    global x
    global z
    
    z = x["Password"]

  except:
    z = z

  if request.method == "POST":
    character1 = request.form["Character1"]
    character2 = request.form["Character2"]
    character3 = request.form["Character3"]

    characters = []

    characters.extend([character1, character2, character3])

    try:
      for x in characters:
        if x == "" or x == " ":
          characters.remove(x)

    except:
      pass

    passwordCount = len(characters)

    if passwordCount != 3:
      NumGen()

      return render_template("Password.html", message="Please enter a character into all 3 boxes", number1=num1, number2=num2, number3=num3)

    count = 0

    global number1
    global number2
    global number3

    number1 -= 1
    number2 -= 1
    number3 -= 1

    print(number1)

    actualCharacter1 = z[number1]
    actualCharacter2 = z[number2]
    actualCharacter3 = z[number3]

    print(actualCharacter1)

    if character1 == actualCharacter1:
      count += 1

    if character2 == actualCharacter2:
      count += 1
      
    else:
      pass

    if character3 == actualCharacter3:
      count += 1
      
    else:
      pass

    if count == 3:
      return redirect(url_for("Account"))
      
    else:
      global PasswordAttempt

      PasswordAttempt -= 1

      if PasswordAttempt == 0:
        return redirect(url_for("MaxAttempts"))

      else:
        NumGen()

        return render_template("Password.html", error="Incorrect password characters - Access denied", number1=num1, number2=num2, number3=num3)

  else:
    NumGen()

    return render_template("Password.html", number1=num1, number2=num2, number3=num3)



@app.route("/Account", methods=["POST", "GET"])
def Account():
    global name
    global UserIDattempts
    global PincodeAttempt
    global PasswordAttempt

    UserIDattempts = 3
    PincodeAttempt = 1
    PasswordAttempt = 3
    
    return render_template("Account.html", name=name)

@app.route("/MaxAttempts", methods=["POST", "GET"])
def MaxAttempts():
    global UserIDattempts
    global PincodeAttempt
    global PasswordAttempt

    UserIDattempts = 3
    PincodeAttempt = 1
    PasswordAttempt = 3

    
    return render_template("MaxAttempts.html", message="Incorrect login details - Access denied")

@app.route("/SignUp", methods=["POST", "GET"])
def SignUp():
    global UserIDattempts
    global PincodeAttempt
    global PasswordAttempt

    UserIDattempts = 3
    PincodeAttempt = 1
    PasswordAttempt = 3

    if request.method == "POST":
        
        NewUserID = request.form["NewUserID"]
        NewPincode = request.form["NewPincode"]
        NewPassword = request.form["NewPassword"]

        NewPincode = str(NewPincode)

        checkBoxes = []
        checkBoxes.extend([NewUserID, NewPincode, NewPassword])

        
        for x in checkBoxes:
          if x == "" or x == " ":
            checkBoxes.remove(x)
          else:
            pass
        
    

        checkBoxesLength = len(checkBoxes)

        if checkBoxesLength == 3:
          pass

        else:
          return render_template("SignUp.html", message="Please fill in all of the boxes")

        try:
          for x in NewUserID:
            if x == "" or x == " ":

              return render_template("SignUp.html", useridMSG="No spaces are allowed within the UserID")
        except:
          pass

        global database

        try:
          checkingID = database[NewUserID]
          return render_template("SignUp.html", useridMSG="This UserID has already been done, please enter another one")
        except:
          pass
        
        NewUserIDlength = len(NewUserID)
        if NewUserIDlength == 10:
          pass
        else:
          return render_template("SignUp.html", useridMSG="Please enter an UserID that's 10 characters long")

        try:
          for x in NewPincode:
            if x == "" or x == " ":

              return render_template("SignUp.html", pincodeMSG="No spaces are allowed within the Pincode")
        except:
          pass

        DigitsCheck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        
        for x in NewPincode:
          if x in DigitsCheck:
            pass
          else:
            return render_template("SignUp.html", pincodeMSG="Pincode must solely be digits only")

        try:
          for x in NewPassword:
            if x == "" or x == " ":
              return render_template("SignUp.html", passwordMSG="No spaces are allowed within the Password")
        except:
          pass

        passwordLength = len(NewPassword)

        if passwordLength >= 8 and passwordLength <= 15:
          pass
        else:
          return render_template("SignUp.html", passwordMSG="Password must be between 8 and 15 characters long")

        database.update({NewUserID : {"Pincode" : NewPincode, "Password" : NewPassword}})

        return render_template("SignUp.html", message="Sign up was successful")

    return render_template("SignUp.html")

@app.route("/AdminLogin", methods=["POST", "GET"])
def AdminLogin():
  global UserIDattempts
  global PincodeAttempt
  global PasswordAttempt

  UserIDattempts = 3
  PincodeAttempt = 1
  PasswordAttempt = 3

  if request.method == "POST":

    ActualAdminName = "Admin"
    ActualAdminPassword = "Admin!"

    global AdminName

    AdminName = request.form["AdminName"]
    AdminPassword = request.form["AdminPassword"]

    adminDetails = []
    adminDetails.extend([AdminName, AdminPassword])

    try:
      for x in adminDetails:
        if x == "" or x == " ":
          adminDetails.remove(x)

    except:
      pass

    detailsCount = len(adminDetails)

    if detailsCount != 2:
      return render_template("AdminLogin.html", message="Please fill out all of the boxes available")

    if AdminName != ActualAdminName:
      return render_template("AdminLogin.html", AdName="Incorrect admin name")
    else:
      if AdminPassword != ActualAdminPassword:
        return render_template("AdminLogin.html", AdPassword="Incorrect admin password")
      else:
        return redirect(url_for("AdminAccount"))

  return render_template("AdminLogin.html")

@app.route("/AdminAccount", methods=["POST", "GET"])
def AdminAccount():
    global UserIDattempts
    global PincodeAttempt
    global PasswordAttempt
    global AdminName
    global database

    UserIDattempts = 3
    PincodeAttempt = 1
    PasswordAttempt = 3

    return render_template("AdminAccount.html", AdminName=AdminName, Database=database)

if __name__ == "__main__":
    app.run(debug=True)




