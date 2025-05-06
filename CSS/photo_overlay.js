document.querySelectorAll('.photo').forEach(photo => {
  photo.addEventListener('click', () => {
    const overlay = document.getElementById('photoOverlay');
    const overlayImg = document.getElementById('overlayImg');
    overlayImg.src = photo.src;
    overlay.style.display = 'flex';
  });
});

document.getElementById('photoOverlay').addEventListener('click', () => {
  document.getElementById('photoOverlay').style.display = 'none';
});
