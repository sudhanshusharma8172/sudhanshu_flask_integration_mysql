// ✅ Form validation
function validateForm() {
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();

    if (name === "") {
        alert("Name cannot be empty!");
        return false;
    }

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        alert("Please enter a valid email address!");
        return false;
    }

    return true; // allow form submission
}

// ✅ Home page slider
let images = [
  "https://images.unsplash.com/photo-1518770660439-4636190af475",
  "https://images.unsplash.com/photo-1521737604893-d14cc237f11d",
  "https://images.unsplash.com/photo-1522199710521-72d69614c702"
];
let index = 0;

function changeImage() {
  index = (index + 1) % images.length;
  document.getElementById("slider").src = images[index];
}

setInterval(changeImage, 3000);