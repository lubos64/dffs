from pyscript import display, document

def restate(e):
 name = document.getElementById("name").value
 address = document.getElementById("address").value
 contactinfo = document.getElementById("contact").value
 buko = int(document.getElementById("buko").value) if document.getElementById("buko").checked else 0 
 sea = int(document.getElementById("sea").value) if document.getElementById("sea").checked else 0
 palm = int(document.getElementById("palm").value) if document.getElementById("palm").checked else 0
 mango = int(document.getElementById("mango").value) if document.getElementById("mango").checked else 0

 total = (buko + sea + palm + mango)

 mang1 = f"Order for: {name}"  #I asked helped from Rycob and Migi on how to make this part work po
 mang2 = f"Address: {address}" 
 mang3 = f"Contact number: {contactinfo}" 
 mang4 = f"Total: ₱ {total}" 

 display(mang1, target="appear1", append=False)
 display(mang2, target="appear2", append=False)
 display(mang3, target="appear3", append=False)
 display(mang4, target="appear4", append=False)