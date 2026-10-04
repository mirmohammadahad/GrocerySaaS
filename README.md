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



সার্ভার চালু করুন (Terminal-এ)
প্রথমে আপনার VS Code-এর Terminal-এ GrocerySaaS ফোল্ডারে থাকা নিশ্চিত হয়ে সার্ভারটি রান করুন:

PowerShell
python manage.py runserver
ধাপ ২: ব্রাউজারে গিয়ে চেক করুন
সার্ভার চালু হলে ব্রাউজার (Chrome/Edge) খুলুন এবং [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) লিংকে যান।

আপনার Superuser একাউন্টের Username এবং Password দিয়ে লগইন করার পর ড্যাশবোর্ডে আপনি নিচের ৪টি বিষয় সরাসরি দেখতে পাবেন:

কাস্টম ইউজার দেখতে:

ড্যাশবোর্ডের ACCOUNTS সেকশনে থাকা Users-এ ক্লিক করুন। এখানে আপনার তৈরি কাস্টম ইউজার মডেল ও ইউজারদের লিস্ট দেখতে পাবেন।

মাল্টি-টেন্যান্ট শপ দেখতে:

ড্যাশবোর্ডের SHOPS সেকশনে থাকা Shops-এ ক্লিক করুন। এখানে আপনার তৈরি করা দোকান (Bazaar360 Main Store) দেখতে পাবেন।

ক্যাটাগরি দেখতে:

PRODUCTS সেকশনে থাকা Categories-এ ক্লিক করুন। এখানে শপের সাথে যুক্ত ক্যাটাগরিগুলো দেখতে পাবেন।

প্রোডাক্ট লিস্ট দেখতে:

PRODUCTS সেকশনে থাকা Products-এ ক্লিক করুন। এখানে শপ ও ক্যাটাগরির সাথে লিঙ্ক করা প্রোডাক্ট দেখতে পাবেন।

💡 সরাসরি দেখার লিংকসমূহ:
লগইন অবস্থায় ব্রাউজারের অ্যাড্রেস বারে নিচের লিংকগুলো সরাসরি পেস্ট করেও চেক করতে পারেন:

Users: [http://127.0.0.1:8000/admin/accounts/user/](http://127.0.0.1:8000/admin/accounts/user/)

Shops: [http://127.0.0.1:8000/admin/shops/shop/](http://127.0.0.1:8000/admin/shops/shop/)

Categories: [http://127.0.0.1:8000/admin/products/category/](http://127.0.0.1:8000/admin/products/category/)

Products: [http://127.0.0.1:8000/admin/products/product/](http://127.0.0.1:8000/admin/products/product/)