document.addEventListener('DOMContentLoaded', () => {
  const openBtn = document.getElementById('openOrdersBtn');
  const closeBtn = document.getElementById('closeOrdersBtn');
  const modal = document.getElementById('ordersModal');

  if (openBtn && closeBtn && modal) {
    openBtn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.add('active');
    });

    closeBtn.addEventListener('click', () => {
      modal.classList.remove('active');
    });

    // Close when clicking outside of modal content
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('active');
      }
    });
  }
});
