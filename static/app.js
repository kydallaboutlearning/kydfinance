const menu = document.querySelector("#mobile-menu");
const menulinks = document.querySelector(".navbar__menu");

menu.addEventListener("click", function () {
  menu.classList.toggle("is-active");
  menulinks.classList.toggle("active");
});

// Adding javascrippt to clone the logo
const logos = document.querySelector(".rotating-logos__track").cloneNode(true);
document.querySelector(".rotating-logos__container").appendChild(logos);


function SwitchPricing() {
  // Getting the checkbox element by its correct ID
  const checkbox = document.getElementById("pricing-toggle-checkbox");

  // Selecting elements for monthly and yearly prices, and yearly discount
  const monthlyprices = document.querySelectorAll(".monthly-price");
  const yearlyprices = document.querySelectorAll(".yearly-price");
  const yearlyDiscounts = document.querySelectorAll(".percentage-saved");

  // Adding the if statement
  if (checkbox.checked) {
    // Hide monthly prices and show yearly prices
    monthlyprices.forEach((price) => price.classList.add("hidden"));
    yearlyprices.forEach((price) => price.classList.remove("hidden"));

    // Show yearly discount
    yearlyDiscounts.forEach((discount) => (discount.style.display = "inline"));
  } else {
    // Show monthly prices and hide yearly prices
    monthlyprices.forEach((price) => price.classList.remove("hidden"));
    yearlyprices.forEach((price) => price.classList.add("hidden"));

    // Hide yearly discount
    yearlyDiscounts.forEach((discount) => (discount.style.display = "none"));
  }

  // Debugging log
  console.log("SwitchPricing function executed successfully");
}


window.addEventListener("load",() => {
  // Selecting the checkbox element by its correct ID
  const Yearchanger = document.getElementById("year");
  const currentYear = new Date().getFullYear();
  Yearchanger.textContent = currentYear;
});