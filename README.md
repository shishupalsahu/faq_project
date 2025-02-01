# Django FAQ Management System

## Objective
This project is a **Django-based FAQ Management System** that supports multilingual translations using **Google Translate API (`googletrans`)**. It provides a **REST API** to manage FAQs with language selection, caching, and a user-friendly admin panel.

The objective of this project is to evaluate the ability to:
- Design and implement Django models with WYSIWYG editor support.
- Store and manage FAQs with multi-language translation.
- Follow **PEP8 conventions** and best practices.
- Write a clear and detailed **README**.
- Use proper **Git commit messages**.

---

## 🚀 Features

✔ **Model-Based FAQ Storage**: Uses Django models for structured FAQ management.  
✔ **WYSIWYG Editor Support**: Integrates `django-ckeditor` for rich text editing.  
✔ **REST API**: Exposes endpoints for fetching FAQs dynamically with language selection.  
✔ **Caching Mechanism**: Uses Redis for optimized translation storage.  
✔ **Automated Translations**: Supports **Hindi & Bengali** translations using Google Translate.  
✔ **Admin Panel**: Provides an intuitive admin interface to manage FAQs.  
✔ **Unit Testing & Code Quality**: Uses `pytest` for testing and enforces **PEP8** standards.  
✔ **Git Version Control**: Follows **conventional commits** for better collaboration.  
✔ **Docker & Deployment Support (Bonus)**: Supports Docker for containerized execution.  

---

## 📌 Task Requirements

### 1️⃣ Model Design
- **FAQ Model**:
  - `question` (TextField)
  - `answer` (RichTextField with `django-ckeditor`)
  - `question_hi`, `question_bn` (for translated versions)
- Model method to **retrieve translated text dynamically**.

### 2️⃣ WYSIWYG Editor Integration
- Uses **`django-ckeditor`** for a rich text editor.
- Ensures multilingual content formatting.

### 3️⃣ API Development
- Implements a **REST API** with endpoints:
  - `GET /api/faqs/` → Fetch FAQs (default language: English)
  - `GET /api/faqs/?lang=hi` → Fetch FAQs in **Hindi**
  - `GET /api/faqs/?lang=bn` → Fetch FAQs in **Bengali**
  - `POST /api/faqs/` → Create FAQ
  - `PUT /api/faqs/{id}/` → Update FAQ
  - `DELETE /api/faqs/{id}/` → Delete FAQ
- Uses **pre-translation** to ensure fast responses.

### 4️⃣ Caching Mechanism
- Uses **Django cache framework** with **Redis**.
- Caches translations for **1 hour** to reduce API calls.

### 5️⃣ Multi-language Translation Support
- Uses **Google Translate API (`googletrans`)**.
- **Automatically translates** questions upon creation.
- Fallback to **English** if translation fails.

### 6️⃣ Admin Panel
- Registers **FAQ model** in Django Admin.
- Provides a **user-friendly UI** for managing FAQs.

### 7️⃣ Unit Tests & Code Quality
- Implements unit tests using **pytest**.
- Tests include:
  - **Model Methods** (translation retrieval)
  - **API Responses** (CRUD operations)
- Uses **flake8** for PEP8 compliance.

### 8️⃣ Documentation
- This README includes:
  - 📌 **Installation steps**
  - 🌍 **API usage examples**
  - 🚀 **Contribution guidelines**
- Ensures **clear structure & readability**.

### 9️⃣ Git & Version Control
- Uses **Git** for version control.
- Follows **conventional commit messages**:
  ```sh
  feat: Add multilingual FAQ model
  fix: Improve translation caching
  docs: Update README with API examples
