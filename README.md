# 🧬 In Silico Bioprocess Optimization: From DoE to Deep Learning

## 📌 Project Overview
This repository contains a comprehensive computational framework for modeling, training, solving, and optimizing biological processes—specifically focusing on the manufacture of monoclonal antibodies (mAbs) using CHO cell cultures.

The project bridges the gap between empirical statistics (Black Box), mechanistic biological kinetics (White Box), and modern machine learning optimization techniques (Grey Box). It serves as a training ground and sandbox for applying Python-based data science to bioprocess engineering.

## 🚀 Key Methodologies Explored

1. **Empirical Surrogate Modeling (Design of Experiments)**
   * Transitioning from OFAT to sequential DoE (Screening & Optimization).
   * Fitting First-Order and Second-Order (Quadratic) polynomial response surfaces using `scikit-learn`.
   * Visualizing high-dimensional biological manifolds and interacting features.
2. **Mechanistic Modeling (ODEs)**
   * Translating biological laws into Ordinary Differential Equations (ODEs).
   * Modeling cell growth using **Monod kinetics**.
   * Modeling mAb secretion using the **Luedeking-Piret equation**.
   * Simulating dynamic 14-day batch cell cultures using `scipy.integrate.odeint`.
3. **Physics-Informed Neural Networks (PINNs) / Hybrid Models**
   * A classic **PINN** in PyTorch that recovers the kinetic constants ($\mu_{max}$, $\beta$) within 5% from 15 noisy samples, using `torch.autograd` to enforce the ODEs in the loss.
   * A **hybrid "grey box" model**: a neural network predicts $\mu_{max}$ and $\beta$ from temperature and pH, and a differentiable RK4 solver turns them into 14-day curves. It predicts unseen conditions within ~4% near the optimum.
   * Bayesian optimization on the learned model reaches 97.5% of the true maximum titer.
4. **In Silico Optimization (Active Learning)**
   * Using **Bayesian Optimization** (`scikit-optimize`) to intelligently navigate the biological manifold.
   * Balancing exploration and exploitation to find peak mAb titers with minimal experimental runs.

## 📂 Repository Structure
* `notebooks/`
  * `1_DoE_Bioprocess_Simulation.ipynb`
  * `2_Ordinary_Diferential_Equations_Integrations.ipynb`
  * `3_Physics-Informed Neural Networks.ipynb`
  * `4_In_Silico_Optimization.ipynb`
  * `5_ODE-Constrained Bayesian Optimizer.ipynb`
  * `Box_Behnken_DoE_example.ipynb` (15-run Box-Behnken design: recovers 99.8% of the true optimal titer)
* `src/` - Helper Python functions for true manifold generation and visualization.
  * `RSM_reduction_optimizer.py`
  * `Synthetic_bioreactor.py`

## ▶️ Getting Started

```bash
git clone https://github.com/Efrazar/in-silico-bioprocess-optimization.git
cd in-silico-bioprocess-optimization
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Open the notebooks in `notebooks/` in numerical order. Package versions are pinned in `requirements.txt` (tested on Python 3.13). Conda users can run `conda env create -f environment.yml` instead.

PyTorch is only needed for notebook 3. The default Linux install also downloads GPU libraries (several GB). To install the smaller CPU-only build first, run `pip install torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu`.

## 🛠️ Tech Stack
* **Python 3.x**
* `numpy` & `pandas` (Data manipulation)
* `scikit-learn` (Polynomial feature expansion, Linear Regression, Scaling)
* `scipy` (ODE integration, Mathematical solvers)
* `matplotlib` (3D Manifold and Time-Series Visualization)
* `scikit-optimize` / `skopt` (Gaussian Processes and Bayesian Optimization)
* `torch` / PyTorch (PINN and hybrid model, CPU is enough)

## 🎯 Objective
To apply advanced Machine Learning and Deep Learning techniques to solve real-world R&D bottlenecks in the biotechnology CRO space, minimizing physical bioreactor runs while maximizing product yield.

---
*Created by [Efrazar](https://github.com/Efrazar). Released under the [MIT License](LICENSE).*
