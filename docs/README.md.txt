# 📊 Profitability Analysis by Category

## Strategic Analysis Project Oriented to Decision Making

### Overview

This project aims to analyze the real profitability of a global sales dataset, considering not only revenue but also discounts, logistics costs (shipping), and effective margin.

The analysis is structured to answer real executive questions, focusing on decision-making rather than just data visualization.

---

### 🎯 Central Question

> “Which products and categories should be prioritized, adjusted, or eliminated to improve profit, without relying solely on revenue growth?”

---

### 🧠 Analytical Approach

The project follows a structured methodology divided into stages, with strong emphasis on:

- Clarity of hypotheses  
- Pre-definition of metrics  
- Separation between product issues and operations  
- Data governance before any visual analysis  

---

### 📂 Documentation Structure

```

docs/
├── README.md
├── 01_executive_briefing_and_decision_map.md
├── 02_case_context_and_objective.md
├── 03_metrics_and_analytical_logic.md
└── 04_case_rules_and_assumptions.md

```

**File descriptions:**

- **01_executive_briefing_and_decision_map.md**  
  Contains the business strategic questions and the executive decision map.

- **02_case_context_and_objective.md**  
  Presents the client context, business problem, and analysis objectives.

- **03_metrics_and_analytical_logic.md**  
  Defines the project’s official metrics, unit of analysis, and how each hypothesis will be addressed.

- **04_case_rules_and_assumptions.md**  
  Documents data treatment rules, financial validations, and exclusion criteria.

---

### 📐 Key Metrics Used

- Total Revenue (`Sales`)  
- Quantity Sold (`Quantity`)  
- Total Shipping Cost (`Shipping Cost`)  
- Real Profit (`Profit − Shipping Cost`)  
- Real Margin (%)  
- Volume-weighted Average Discount  

*The profit considered for decision-making is exclusively the profit after shipping costs.*

---

### 🟢🟡🔴 Strategic Classification

Categories and products are classified as:

- 🟢 **Prioritize** — positive profit, healthy margin, low discount dependency  
- 🟡 **Adjust** — low margin, high sensitivity to discount or shipping  
- 🔴 **Eliminate** — recurring loss or logistical infeasibility  

---

### 🛠️ Tools

- Python  
- Pandas  
- Streamlit (analytical interface)  

*Tools are used as a means, not an end.*  
*The project focus is on analytical thinking and business decision-making.*

---

### 📌 Final Note

This project simulates a real consulting and strategic analysis scenario, prioritizing clarity, governance, and data-driven decision making.

---

### 👤 Author

Project developed by **Robinson Matheus**  
Area: Data Analysis | Strategy | Decision Making
```