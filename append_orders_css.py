css_to_append = """
/* --- ORDERS MODAL (PREMIUM DESIGN) --- */
.orders-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s ease;
}

.orders-modal.active {
  opacity: 1;
  pointer-events: auto;
}

.orders-modal-content {
  background: var(--white, #ffffff);
  width: 90%;
  max-width: 600px;
  max-height: 85vh;
  border-radius: 24px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transform: translateY(30px) scale(0.95);
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.orders-modal.active .orders-modal-content {
  transform: translateY(0) scale(1);
}

.orders-modal-header {
  padding: 24px;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(139, 92, 246, 0.05));
  border-bottom: 1px solid rgba(229, 231, 235, 0.5);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.orders-modal-header h2 {
  margin: 0;
  font-size: 22px;
  font-weight: 700;
  color: var(--text, #1e293b);
}

.close-btn {
  background: transparent;
  border: none;
  font-size: 28px;
  color: var(--muted, #64748b);
  cursor: pointer;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.close-btn:hover {
  background: rgba(226, 232, 240, 0.8);
  color: var(--danger, #ef4444);
  transform: rotate(90deg);
}

.orders-list {
  padding: 24px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
  scrollbar-width: thin;
}

.orders-list::-webkit-scrollbar {
  width: 6px;
}
.orders-list::-webkit-scrollbar-thumb {
  background-color: var(--border, #e5e7eb);
  border-radius: 10px;
}

.order-item {
  border: 1px solid rgba(229, 231, 235, 0.8);
  border-radius: 16px;
  overflow: hidden;
  background: var(--white, #ffffff);
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
}

.order-item:hover {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
  border-color: rgba(37, 99, 235, 0.3);
}

.order-summary {
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  background: linear-gradient(to right, transparent, rgba(248, 250, 252, 0.5));
  transition: background 0.3s ease;
}

.order-item.active .order-summary {
  background: rgba(248, 250, 252, 1);
  border-bottom: 1px solid rgba(229, 231, 235, 0.5);
}

.order-summary strong {
  display: block;
  font-size: 16px;
  color: var(--text, #1e293b);
  margin-bottom: 4px;
}

.order-date {
  font-size: 13px;
  color: var(--muted, #64748b);
}

.order-status-price {
  text-align: right;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.order-status-price strong {
  font-size: 16px;
  margin: 0;
  color: var(--primary, #2563eb);
}

.status {
  font-size: 12px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 50px;
  display: inline-block;
}

.status.delivered {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.status.processing {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
}

.toggle-icon {
  font-size: 10px;
  color: var(--muted, #64748b);
  transition: transform 0.3s ease;
  margin-top: 4px;
}

.order-item.active .toggle-icon {
  transform: rotate(180deg);
}

.order-details {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1), padding 0.4s ease;
  background: rgba(248, 250, 252, 0.5);
}

.order-item.active .order-details {
  max-height: 500px;
  padding: 16px 20px;
}

.order-product {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px dashed rgba(229, 231, 235, 0.8);
}

.order-product:last-child,
.order-product:nth-last-child(2) { /* if total is last child */
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.order-product img {
  width: 60px;
  height: 60px;
  border-radius: 8px;
  object-fit: cover;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.order-product h4 {
  margin: 0 0 4px 0;
  font-size: 14px;
  font-weight: 600;
  color: var(--text, #1e293b);
}

.order-product p {
  margin: 0;
  font-size: 13px;
  color: var(--muted, #64748b);
}

.order-total {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(229, 231, 235, 0.8);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 600;
  font-size: 15px;
  color: var(--text, #1e293b);
}

.order-total span {
  font-size: 18px;
  color: var(--primary, #2563eb);
}
"""

with open('/home/jasurbek/Desktop/ShopZone/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_to_append)
print("CSS appended to styles.css")
