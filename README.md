# 🏟️ Venture North Admin Suite

A fully integrated, AI-powered operations platform for managing all aspects of your sports complex.

## ✅ Features by Category

### 📊 Central Dashboard
- Revenue, contract, and usage snapshot
- AI suggestions to improve efficiency

### 👥 Memberships
- Member profiles and tiers
- Credit tracking and AI-driven upsells
- Market comparison to peer facilities

### 🏟️ Dome Usage
- Usage logger for all courts and turf
- Revenue heatmaps and optimizer
- Visual layout and AI-driven scheduling

### 💼 Sponsorship
- Sponsor CRM and contract generation (PandaDoc-ready)
- AI pricing calculator and ROI tracker

### 📑 Contracts & Orgs
- Contract tracking and AI renewal logic
- Usage monitoring per organization
- Market benchmarking against similar complexes

### 🏛️ Governance
- Board dashboard, mentorship, student committees
- Scholarship eligibility logic

### 🤝 Personnel
- Volunteers, referees, leagues, teams

### 📢 NIL & AI Tools
- NIL tracker, AI matchmaker, AI scheduler

---

## 🔐 Login System
- Email/password authentication with roles
- Role-based visibility across all tools
- Stored in `users.json`

---

## 🚀 Deployment Instructions

1. Unzip all files
2. Push to GitHub using the script below
3. Set `main_app.py` as the entrypoint in Streamlit Cloud
4. Add secrets to `.streamlit/secrets.toml` as needed

---

## 🔁 Weekly Report Automation (Optional)
Schedule a weekly run of:
- Revenue summary
- Tool usage reports
- Contract renewals due
- Sponsor ROI tracking

Requires simple task scheduler + email API (SendGrid-compatible)

---

## 📁 File Map

- `main_app.py` — Entry point
- `auth.py`, `users.json` — Login system
- `*.py` — Module tools (each tool has a `run()` method)