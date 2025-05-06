// ...existing code...

document.getElementById('profile-link').addEventListener('click', function (event) {
  event.preventDefault();
  window.location.href = '/profile'; // Replace '/profile' with the actual profile page URL
});

// ...existing code...