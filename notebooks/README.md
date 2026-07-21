Here is a comprehensive and professionally tailored README.md draft for your GitHub portfolio. It is structured to instantly signal to hiring managers that you possess both rigorous statistical knowledge and practical bioprocess engineering insight.

**Bioprocess Optimization via Response Surface Methodology (RSM) & Multi-Objective Constrained Optimization**

**📌 Project Overview**

This repository showcases an end-to-end data science and statistical engineering workflow for optimizing an upstream cell culture bioprocess. Operating within a simulated Quality by Design (QbD) framework, this project applies a 3-factor Box-Behnken Design (BBD) to model and maximize critical quality attributes (CQAs) while strictly adhering to biological constraints.

The entire workflow is documented and executable within the core Jupyter notebook: Box_Behnken_DoE_example.ipynb.

**🛠️ Key Technical Highlights**

- **Design of Experiments (DoE):** Leverages a 3-factor, 3-level Box-Behnken design matrix to efficiently profile quadratic response surfaces with minimal experimental runs.
- **Information Criteria Model Selection:** Avoids automated underfitting by using Akaike Information Criterion (AIC) and Adjusted rather than strict, arbitrary -value cutoffs to identify true parsimonious models.
- **Constrained Multi-Objective Optimization:** Implements a Sequential Least Squares Programming (**SLSQP**) algorithm to maximize product yields under strict biological thresholds.
- **Advanced Response Surface Slicing:** Utilizes 2D contours and 3D surface mapping dynamically sliced through optimal coordinate planes to isolate and highlight high-impact process variables.

**🚀 The Optimization Pipeline**

**1\. Data Ingestion & Phenomenological Simulation**

The workflow starts by ingesting an experimental matrix template (BBD_synthetic_data_example.csv). In-silico data generation simulates true cell culture responses based on biological behaviors:

- **Volumetric Titer ():** Governed by a parabolic curve peaking near mid-to-high feed concentrations.
- **Viable Cell Density (VCD, ):** Penalized by high booster accumulation.
- **Viability (%):** Simulates a threshold-based metabolic toxicity penalty when the booster concentration exceeds a critical ceiling.

**2\. Statistical Pre-processing & Stepwise Reduction**

Prior to modeling, the design space isolates orthogonal BBD runs from control groups. Normality is statistically validated via Shapiro-Wilk testing () across all CQAs.

An automated backward stepwise elimination algorithm (RSM_reduction_optimizer) filters out non-significant interaction and quadratic terms.

💡 **Data Science Insight:** Rather than allowing the automated algorithm to reduce the model purely based on a standard cutoff, the model is manually finalized at **Iteration 3** for VCD and Viability. This intentional intervention captures the global minimum for **AIC** and global maximum for **Adjusted** , preventing underfitting and retaining valuable explanatory variance.

**3\. Multi-Objective Optimization via SLSQP**

To transition from a statistical surface to an engineering reality, a multi-objective optimization problem is solved using the **SLSQP (Sequential Least Squares Programming)** optimizer. SLSQP is ideal for bioprocess engineering because it handles non-linear quadratic target functions while honoring multi-variant inequality constraints.

The system successfully resolves the trade-off, establishing the exact natural coordinate parameters required for peak yield:

- **Optimal Feed Component 1 ():**
- **Optimal Feed Component 2 ():**
- **Optimal Booster ():**

**📊 Data Visualization & Response Slices**

To clearly convey the multi-dimensional design space, visualizations are explicitly sliced across axes that maximize the visual impact of the dominant variables:

- **Titer Surface ( vs. ):** Slices through the optimal booster concentration ( ) to cleanly display the sweet spot where the two heavy quadratic penalties interact.
- **VCD Growth Curve ( vs. ):** Captures the biological truth that growth is primarily governed by booster penalties and feed constraints, isolating the plot from noise components.
- **Viability Cliff ( vs. ):** Distinctly displays the flat plateau of high cell viability that drops off sharply as the toxic booster threshold ( ) is approached.

_Example of the output generated in_ Box_Behnken_DoE_example.ipynb:

**💻 Environment & Dependencies**

The script is designed for Python 3.8+ environments. Core libraries utilized include:

- numpy & pandas - Data structures and vector manipulation.
- statsmodels - Ordinary Least Squares (OLS) and regression metrics.
- scipy.optimize - Non-linear sequential quadratic programming (SLSQP).
- matplotlib & seaborn - 2D and 3D response surface graphics.

To run this notebook locally, ensure all files are in the same working directory and execute:

Bash

pip install numpy pandas statsmodels scipy matplotlib seaborn jupyterlab

jupyter lab Box_Behnken_DoE_example.ipynb