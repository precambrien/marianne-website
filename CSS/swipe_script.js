<script>
  let touchStartX = 0;
  let touchEndX = 0;

  function handleGesture() {
    if (touchEndX < touchStartX - 50) {
      // swipe left : go forward
      const right = document.querySelector('.arrow.right');
      if (right) right.click();
    }
    if (touchEndX > touchStartX + 50) {
      // swipe right : go back
      const left = document.querySelector('.arrow.left');
      if (left) left.click();
    }
  }

  document.addEventListener('touchstart', e => {
    touchStartX = e.changedTouches[0].screenX;
  });

  document.addEventListener('touchend', e => {
    touchEndX = e.changedTouches[0].screenX;
    handleGesture();
  });
</script>
