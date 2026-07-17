import os
import glob

html_files = glob.glob('*.html')

nav_old = '<a href="contact.html">Aloqa</a>'
nav_new = '<a href="contact.html">Aloqa</a>\n      <a href="#" id="openOrdersBtn">Buyurtmalarim</a>'

script_old = '<script src="router.js"></script>'
script_new = '''  <!-- Orders Modal -->
  <div id="ordersModal" class="orders-modal">
    <div class="orders-modal-content">
      <div class="orders-modal-header">
        <h2>Mening buyurtmalarim</h2>
        <button id="closeOrdersBtn" class="close-btn">&times;</button>
      </div>
      <div class="orders-list">
        <div class="order-item">
          <div class="order-summary" onclick="this.parentElement.classList.toggle('active')">
            <div>
              <strong>Buyurtma #1024</strong>
              <span class="order-date">13-Iyul, 2026</span>
            </div>
            <div class="order-status-price">
              <span class="status delivered">Yetkazib berilgan</span>
              <strong>$129.98</strong>
              <span class="toggle-icon">▼</span>
            </div>
          </div>
          <div class="order-details">
            <div class="order-product">
              <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=150" alt="Smart Watch Pro">
              <div>
                <h4>Smart Watch Pro</h4>
                <p>Miqdor: 1 x $49.99</p>
              </div>
            </div>
            <div class="order-product">
              <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=150" alt="Sport Shoes">
              <div>
                <h4>Sport Shoes</h4>
                <p>Miqdor: 1 x $79.99</p>
              </div>
            </div>
            <div class="order-total">Jami to'lov: <span>$129.98</span></div>
          </div>
        </div>
        <div class="order-item">
          <div class="order-summary" onclick="this.parentElement.classList.toggle('active')">
            <div>
              <strong>Buyurtma #1025</strong>
              <span class="order-date">15-Iyul, 2026</span>
            </div>
            <div class="order-status-price">
              <span class="status processing">Jarayonda</span>
              <strong>$39.99</strong>
              <span class="toggle-icon">▼</span>
            </div>
          </div>
          <div class="order-details">
            <div class="order-product">
              <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=150" alt="Wireless Headphones">
              <div>
                <h4>Wireless Headphones</h4>
                <p>Miqdor: 1 x $39.99</p>
              </div>
            </div>
            <div class="order-total">Jami to'lov: <span>$39.99</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script src="router.js"></script>
  <script src="orders.js"></script>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if nav_old in content and 'id="openOrdersBtn"' not in content:
        content = content.replace(nav_old, nav_new)
    
    if script_old in content and 'id="ordersModal"' not in content:
        content = content.replace(script_old, script_new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
