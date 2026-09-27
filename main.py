from pyscript import document, display

def create_order(e):
    document.getElementById("output1").innerHTML = "" # Clears previous result

    prod1=document.getElementById("item1") # Gets the id of all items
    prod2=document.getElementById("item2")
    prod3=document.getElementById("item3")
    prod4=document.getElementById("item4")

    # Calculates selected items
    subtotal = (float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked) # Variable for subtotal

    vat_rate = 0.12 * subtotal # Variable for tax rate
    grandtotal = subtotal + vat_rate # Variable for the grandtotal

    document.getElementById("output1").innerHTML = f'''
    Subtotal: {subtotal} <br>
    Tax: {vat_rate} <br>
    Total: {grandtotal} <br>
    Thank you for purchasing from CUPPA MATCHA!<br>
    Enjoy! =]'''

def display_char(e):
    document.getElementById("output2").innerHTML = ""

    get_word = document.getElementById("word").value

    display(get_word[:3], target="output2") # Get the first 3 letters of the word
