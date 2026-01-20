# 🇵🇰 Pakistan Drug Index (PDI)

**Pakistan Drug Index (PDI)** is an open, extensible pharmaceutical and clinical intelligence platform designed to organize, explore, and analyze medicines, manufacturers, and (eventually) market data relevant to Pakistan.

The project focuses on **clean data ingestion**, **stable backend architecture**, and a **scalable frontend foundation** that can evolve into a full national-level reference system for clinicians, pharmacists, researchers, and investors.

---

## ✨ Project Vision

Pakistan lacks a unified, structured, and developer-friendly drug reference system that connects:

- Medicines & generics  
- Brands & alternatives  
- Manufacturers  
- Clinical context  
- Market intelligence (PSX – future phase)

PDI aims to fill that gap with a **transparent, file-driven, API-first architecture**.

---

## 🧠 Key Design Principles

- **File-based data source** (JSON-first, Git-friendly)
- **Stateless backend**
- **Auto-discovery of new data**
- **Clear separation of concerns**
- **No database lock-in**
- **Frontend built for data density, not demos**

---

```json
{
pakistandrugindex/
│
├── backend/
│ └── app/
│ ├── main.py # FastAPI entry point
│ ├── routers/
│ │ ├── medicines.py # Medicine APIs
│ │ └── init.py
│ ├── services/
│ │ ├── medicine_loader.py
│ │ ├── medicine_alternatives.py
│ │ └── init.py
│ └── init.py
│
├── data/
│ └── medicines/
│ ├── acetazolamide.json
│ ├── acarbose.json
│ ├── aceclofenac.json
│ └── ...
│
├── frontend/
│ ├── app/
│ │ ├── layout.js # Sidebar-based layout
│ │ ├── page.js # Dashboard
│ │ ├── medicines/
│ │ │ ├── page.js # Medicines table
│ │ │ └── [id]/page.js # Medicine detail + alternatives
│ │ ├── companies/ # (scaffolded)
│ │ └── markets/ # (scaffolded)
│ ├── components/
│ │ └── Sidebar.js
│ └── package.json
│
├── docs/
├── scripts/
└── README.md
}
---

## 💊 Medicine Data Model

Each medicine is stored as **one JSON file**:


### Why this approach?

- Easy version control (clean diffs)
- No migration overhead
- Auto-discovery of new data
- Human-readable
- Scales to thousands of medicines

### Example (simplified):

```json
{
  "name": "Acetazolamide",
  "generic": "Acetazolamide",
  "strength": "250 mg",
  "dosage_form": "Tablet",
  "therapeutic_class": "Carbonic anhydrase inhibitor"
}


## 🗂️ Repository Structure

