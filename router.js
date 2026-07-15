(function () {
  const knownPages = [
    'index.html',
    'products.html',
    'product-detail.html',
    'categories.html',
    'about.html',
    'contact.html',
    'faq.html',
    'wishlist.html',
    'cart.html',
    'login.html',
    'register.html',
    'checkout.html',
    'account.html',
    'orders.html',
    '404.html'
  ];

  const path = window.location.pathname || '';
  const currentFile = path.split('/').filter(Boolean).pop() || 'index.html';
  const normalized = currentFile.includes('.') ? currentFile : `${currentFile}.html`;
  const isStaticAsset = /\.(css|js|png|jpg|jpeg|gif|svg|webp|ico|pdf|json)(\?.*)?$/i.test(path);

  if (document.body && document.body.dataset.page === '404') {
    return;
  }

  if (!isStaticAsset && !knownPages.includes(normalized)) {
    window.location.replace('./404.html');
  }
})();
