css_to_append = """
/* --- PREMIUM SEARCH PANEL --- */
.search-panel {
  display: flex;
  flex-direction: column;
  gap: 16px;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 24px;
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  margin-bottom: 32px;
  border: 1px solid rgba(229, 231, 235, 0.5);
  position: relative;
  overflow: hidden;
}

.search-panel::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, var(--primary), var(--primary-dark), #a855f7);
}

.search-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 16px;
  color: var(--muted);
}

.search-input-wrapper input {
  width: 100%;
  padding: 16px 48px;
  font-size: 16px;
  border: 2px solid var(--border);
  border-radius: var(--radius-sm);
  transition: var(--transition);
  background: var(--white);
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
}

.search-input-wrapper input:focus {
  background: var(--white);
  border-color: var(--primary);
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15);
}

.clear-search-btn {
  position: absolute;
  right: 16px;
  background: transparent;
  color: var(--muted);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4px;
  border-radius: 50%;
  transition: var(--transition);
  border: none;
}

.clear-search-btn:hover {
  background: var(--border);
  color: var(--danger);
  transform: scale(1.1);
}

.search-filters {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 8px 16px;
  border-radius: 50px;
  background: var(--white);
  color: var(--muted);
  font-size: 14px;
  font-weight: 600;
  border: 1px solid var(--border);
  transition: var(--transition);
  cursor: pointer;
}

.filter-btn:hover {
  border-color: var(--primary);
  color: var(--primary);
  transform: translateY(-1px);
}

.filter-btn.active {
  background: var(--primary);
  color: var(--white);
  border-color: var(--primary);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.search-status {
  font-size: 14px;
  color: var(--muted);
  font-weight: 500;
  margin-top: 8px;
}

/* --- PREMIUM DASHBOARD --- */
.dashboard-heading {
  margin-bottom: 40px;
}

.account-dashboard {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 32px;
  align-items: start;
}

@media (max-width: 900px) {
  .account-dashboard {
    grid-template-columns: 1fr;
  }
}

.dashboard-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  position: relative;
  transition: var(--transition);
  border: 1px solid rgba(229, 231, 235, 0.5);
}

.dashboard-card:hover {
  box-shadow: var(--shadow);
  transform: translateY(-2px);
}

.profile-main-card {
  text-align: center;
}

.profile-header-bg {
  height: 120px;
  background: linear-gradient(135deg, var(--primary), #8b5cf6, #ec4899);
  background-size: 200% 200%;
  animation: gradientBG 5s ease infinite;
}

@keyframes gradientBG {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.avatar-wrapper {
  position: relative;
  width: 88px;
  height: 88px;
  margin: -44px auto 16px;
}

.avatar-circle.premium-glow {
  width: 100%;
  height: 100%;
  background: var(--white);
  border: 4px solid var(--white);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary);
  box-shadow: 0 8px 24px rgba(37, 99, 235, 0.25);
  font-size: 24px;
}

.status-badge.online {
  position: absolute;
  bottom: 4px;
  right: 4px;
  width: 18px;
  height: 18px;
  background: var(--success);
  border: 3px solid var(--white);
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.profile-info h2 {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
}

.premium-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: rgba(139, 92, 246, 0.1);
  color: #8b5cf6;
  padding: 4px 12px;
  border-radius: 50px;
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 24px;
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.profile-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: var(--border);
  margin-bottom: 24px;
}

.stat-box {
  background: var(--white);
  padding: 16px 8px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: background 0.3s ease;
}

.stat-box:hover {
  background: var(--light);
}

.stat-value {
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
}

.stat-label {
  font-size: 12px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.dashboard-nav {
  display: flex;
  flex-direction: column;
  padding: 0 16px 16px;
  gap: 4px;
}

.dashboard-nav a {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: var(--radius-sm);
  color: var(--muted);
  font-weight: 500;
  transition: var(--transition);
}

.dashboard-nav a:hover {
  background: var(--light);
  color: var(--primary);
  transform: translateX(4px);
}

.dashboard-nav a.active {
  background: rgba(37, 99, 235, 0.1);
  color: var(--primary);
  font-weight: 600;
}

.dashboard-nav a.logout-link {
  color: var(--danger);
  margin-top: 16px;
}

.dashboard-nav a.logout-link:hover {
  background: rgba(220, 38, 38, 0.1);
  transform: translateX(4px);
}

.dashboard-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.completion-card {
  padding: 24px;
  background: linear-gradient(to right, #ffffff, #f8fafc);
}

.completion-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.completion-header h3 {
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.completion-header span {
  font-weight: 700;
  color: var(--primary);
  background: rgba(37, 99, 235, 0.1);
  padding: 4px 10px;
  border-radius: 50px;
  font-size: 14px;
}

.progress-bar-bg {
  height: 10px;
  background: var(--border);
  border-radius: 5px;
  overflow: hidden;
  margin-bottom: 12px;
  box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
}

.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary), #60a5fa, #34d399);
  border-radius: 5px;
  transition: width 1s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 2px 4px rgba(59, 130, 246, 0.3);
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

@media (max-width: 1100px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}

.details-card, .activity-card {
  padding: 24px;
}

.card-header-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.card-header-flex h3, .activity-card h3 {
  font-size: 18px;
  margin-bottom: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.activity-card h3 {
  margin-bottom: 24px;
}

.detail-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.detail-list li {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding-bottom: 16px;
  border-bottom: 1px dashed var(--border);
}

.detail-list li:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.detail-icon {
  font-size: 20px;
  width: 44px;
  height: 44px;
  background: var(--light);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary);
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.detail-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.detail-text .label {
  font-size: 13px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.detail-text strong {
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
  line-height: 1.4;
}

.timeline {
  display: flex;
  flex-direction: column;
  gap: 24px;
  position: relative;
}

.timeline::before {
  content: '';
  position: absolute;
  top: 8px;
  left: 7px;
  bottom: 0;
  width: 2px;
  background: var(--border);
}

.timeline-item {
  position: relative;
  display: flex;
  gap: 20px;
  transition: var(--transition);
}

.timeline-item:hover {
  transform: translateX(4px);
}

.timeline-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--white);
  border: 4px solid var(--muted);
  position: relative;
  z-index: 1;
  margin-top: 4px;
  box-shadow: 0 0 0 4px var(--white);
}

.timeline-dot.success { border-color: var(--success); }
.timeline-dot.primary { border-color: var(--primary); }
.timeline-dot.warning { border-color: var(--warning); }

.timeline-content {
  display: flex;
  flex-direction: column;
  gap: 4px;
  background: var(--light);
  padding: 16px;
  border-radius: var(--radius-sm);
  flex: 1;
}

.timeline-content h4 {
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
}

.timeline-content p {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.5;
}

.timeline-content .time {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 8px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.timeline-content .time::before {
  content: '🕒';
  font-size: 10px;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.user-icon {
  color: var(--text);
}

.user-icon:hover {
  color: var(--primary);
}
"""

with open('/home/jasurbek/Desktop/ShopZone/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_to_append)
