from pyscript import document, display

    #function to compute total of selected items
def _get_selected_items_and_total():
    """
    Helper to gather selected items and compute total.
    Returns (items_list, total_float).
    """
    checkboxes = document.querySelectorAll("input[type=checkbox][name=food]")
    items = []
    total = 0.0

    for box in checkboxes:
        if box.checked:
            raw_price = box.getAttribute("data-price")
            try:
                price = float(raw_price)
            except Exception as e:
                raise ValueError(f"Invalid price for item (data-price='{raw_price}').") from e

            label_text = box.parentElement.textContent.strip()
            items.append(label_text)
            total += price

    return items, total

    #function to update inline total when checkboxes change
def update_inline_total(event=None):
    """
    Update the inline Order Total (the <span id="orderTotal">).
    Called on checkbox change events.
    """
    try:
        items, total = _get_selected_items_and_total()
        order_total_span = document.getElementById("orderTotal")
        if order_total_span is None:
            display("⚠️ Missing orderTotal element in page.", target="info_display")
            return
        order_total_span.innerText = f"{total:.2f}"
    except Exception as err:
        display(f"⚠️ Error updating total: {err}", target="info_display")


    #function to compute total and display order summary on form submission
def compute_total(event=None):
    """
    Called when the user submits the form (py-click). Validates inputs,
    builds order summary, updates the inline total, and displays the result.
    """
    if event is not None:
        try:
            event.preventDefault()
        except Exception:
            pass

    try:
        name = document.getElementById("name").value.strip()
        address = document.getElementById("address").value.strip()
        contact = document.getElementById("contact").value.strip()

        if not name or not address or not contact:
            display("HEY! Please fill out Name, Address, and Contact Number.", target="info_display")
            return

        items, total = _get_selected_items_and_total()

        if not items:
            display("HEY! Please select at least one pizza.", target="info_display")
            return

    #to display my message/receipt
        message = f"""
    <div class='result'>Order Receipt:</div>
    Name: {name}<br>
    Address: {address}<br>
    Contact Number: {contact}
    <div class='result-title notes-title'>order form</div>
    <span class='notes'>{name}'s order to {address}, contact me at {contact}</span>
    """

        document.getElementById("order_output").innerHTML = message
    
    # Update the inline total as well
        order_total_span = document.getElementById("orderTotal")
        if order_total_span is not None:
            order_total_span.innerText = f"{total:.2f}"
    except Exception as err:
        display(f"HEY! Unexpected error: {err}", target="info_display")