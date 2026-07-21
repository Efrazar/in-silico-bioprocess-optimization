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
   * Simulating dynamic 14-day fed-batch cell cultures using `scipy.integrate.odeint`.
3. **Physics-Informed Neural Networks (PINNs) / Hybrid Models**
   * Conceptualizing "Grey Box" architectures where Deep Learning predicts kinetic parameters ($\mu_{max}$, $\beta$) based on environmental inputs (Temperature, pH).
   * Constraining neural networks with biological mass-balance laws.
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
  * `Box-Behnken example with synthetic data.ipynb`
* `src/` - Helper Python functions for true manifold generation and visualization.
  * `RSM_reduction_optimizer.py`
  * `Synthetic_bioreactor.py`

## 🛠️ Tech Stack
* **Python 3.x**
* `numpy` & `pandas` (Data manipulation)
* `scikit-learn` (Polynomial feature expansion, Linear Regression, Scaling)
* `scipy` (ODE integration, Mathematical solvers)
* `matplotlib` (3D Manifold and Time-Series Visualization)
* `scikit-optimize` / `skopt` (Gaussian Processes and Bayesian Optimization)

## 🎯 Objective
To apply advanced Machine Learning and Deep Learning techniques to solve real-world R&D bottlenecks in the biotechnology CRO space, minimizing physical bioreactor runs while maximizing product yield.

---
*Created by [Efrazar](https://github.com/Efrazar)*
