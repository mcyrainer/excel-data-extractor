# Multi-Source Excel Data Extraction Tool 📊

### Developed by: Rainer Mou
**Final Year Student, BSc (Hons) in Data Science and Analytics** **The Hong Kong Polytechnic University**

---

## 📌 Project Overview
In many business environments in Hong Kong, data is often scattered across multiple Excel workbooks (monthly reports, invoices, or inventory logs). Manually merging these is time-consuming and prone to human error.

This project is a **Python-based ETL (Extract, Transform, Load) tool** designed to:
1.  **Recursively Search:** Automatically find all `.xlsx` and `.xls` files within a root folder and its subfolders.
2.  **Consolidate Data:** Extract data from multiple sheets and merge them into a single Master DataFrame using `pandas`.
3.  **Data Tracking:** Automatically add metadata (source filename and processing date) to every row for auditability.
4.  **Export:** Generate a clean, consolidated Excel report ready for analysis or visualization in Tableau/PowerBI.

---

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Key Libraries:** * `Pandas`: For high-performance data manipulation.
    * `Openpyxl`: For engine-level Excel reading.
    * `OS`: For navigating the local file system.

---

## 🚀 How to Use
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[mcyrainer]/excel-data-extractor.git
