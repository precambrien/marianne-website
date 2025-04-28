// Simple script to toggle the "extra" text when clicking the "+"
document.querySelectorAll('.plus').forEach(button => {
  button.addEventListener('click', () => {
    const extra = button.nextElementSibling;
    if (extra.style.display === 'block') {
      extra.style.display = 'none';
      button.textContent = '+';
    } else {
      extra.style.display = 'block';
      button.textContent = '−'; // change + to − when expanded
    }
  });
});
