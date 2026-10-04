# 🛒 Bazaar360 - Grocery SaaS & POS System

Amader Grocery SaaS & POS project-er shob kajer simple roadmap ebong current status.

---

## 📌 Project Roadmap & Status

### Phase 1: Core Setup
- [x] Django project (`GrocerySaaS`) setup ebong Git repository link [DONE]
- [x] Custom User model setup (`accounts.User`) [DONE]
- [x] Multi-tenant `Shop` model setup (`shops.Shop`) [DONE]
- [x] `Category` ebong `Product` model setup (`products` app) [DONE]
- [x] Migration error ebong Circular import issue fix [DONE]
- [x] Admin Panel-e Shop, Category ebong Product test done [DONE]

---

### Phase 2: Stock & Inventory Management
- [ ] Product stock quantity ebong price management
- [ ] Low Stock Alert system (stock kome gele notification)
- [ ] Stock adjustment log (maal asha ebong noshto hobar হিসাব)

---

### Phase 3: Login & Security
- [ ] Custom Login, Logout ebong User authentication
- [ ] Shop wise data isolation (ek shop-er data onno shop dekhbe na)
- [ ] Role setup (Owner, Manager, Cashier permission)

---

### Phase 4: POS & Billing System
- [ ] Cashier-er jonno fast POS billing screen
- [ ] Barcode scanner support
- [ ] Cart system, discount, VAT ebong auto stock minus
- [ ] Customer slip/receipt print (PDF/Thermal)

---

### Phase 5: Customer & Vendor Management
- [ ] Customer record ebong baki/due tracking
- [ ] Supplier/Vendor list ebong stock kharidari entry

---

### Phase 6: Reports & Analytics
- [ ] Daily, weekly, monthly sales ebong profit report
- [ ] Customer baki ebong supplier payables report

---

### Phase 7: Deployment & SaaS Launch
- [ ] PostgreSQL production database setup
- [ ] Render/VPS server-e live deployment ebong SSL setup

---

## 🛠️ Tech Stack
- **Backend:** Python / Django
- **Database:** PostgreSQL / SQLite
- **Version Control:** Git & GitHub