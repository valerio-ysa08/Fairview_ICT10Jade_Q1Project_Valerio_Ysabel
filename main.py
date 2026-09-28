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
    # Clear previous output
    document.getElementById("output2").innerHTML = "" 

    # Get values using the correct HTML element IDs
    category_var = document.getElementById("category").value
    product_var = document.getElementById("product").value
    stockqty_var = document.getElementById("stock_qty").value
 
    # Check if fields are selected/filled out to prevent errors
    if not category_var and not product_var:
        document.getElementById("output2").innerHTML = "Please select a drink or product!"
        return

    # Use whichever one has a value selected
    chosen_item = category_var if category_var else product_var
    prefix_source = category_var if category_var else product_var

    # Build the SKU variable
    cuppa_m_sku = f"{category_var[:4].upper()}-{product_var[:3].upper()}-{stockqty_var}"

    # Display the SKU in the HTML output div
    document.getElementById("output2").innerHTML = f"SKU: {cuppa_m_sku}"
