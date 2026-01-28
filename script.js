let cart = [];

function addToCart(name, price) {
  cart.push({name, price});
  alert(name + " added to cart");
}

function submitPayment() {
  alert("Payment Submitted. Admin will verify.");
}
