import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import re

class RSMModelEvaluator:
    """
    Author: Efrain Zarazua Arvizu
    Automates the generation of reduced Response Surface Methodology (RSM) 
    models via backward elimination while enforcing the Principle of Marginality.
    Retains all models iteratively for manual expert selection.
    """
    
    def __init__(self, data, target_col, initial_terms, alpha=0.05):
        self.data = data
        self.target_col = target_col
        self.active_terms = list(initial_terms)
        self.alpha = alpha
        self.history = []
        self.models = {} # Dictionary to store the model object for each iteration

    def _get_protected_main_effects(self):
        """Identifies main effects that are protected by active higher-order terms."""
        protected = set()
        for term in self.active_terms:
            if ':' in term:  
                parts = term.split(':')
                protected.update(parts)
            elif 'I(' in term and '**2' in term.replace(" ", ""):  
                match = re.search(r'I\((.*?)\*\*\s*2\)', term.replace(" ", ""))
                if match:
                    protected.add(match.group(1))
        return protected

    def _remove_term(self, term_to_remove):
        """Safely removes a term, handling statsmodels string formatting differences."""
        if term_to_remove in self.active_terms:
            self.active_terms.remove(term_to_remove)
            return term_to_remove
        
        term_no_spaces = term_to_remove.replace(" ", "")
        for t in self.active_terms:
            if t.replace(" ", "") == term_no_spaces:
                self.active_terms.remove(t)
                return t
        
        if ':' in term_to_remove:
            target_set = set(term_no_spaces.split(':'))
            for t in self.active_terms:
                if set(t.replace(" ", "").split(':')) == target_set:
                    self.active_terms.remove(t)
                    return t
                    
        return None

    def fit_stepwise(self):
        """Fits models iteratively and builds the statistical tracking table."""
        iteration = 0
        removed_term_name = "None (Full Model)"
        
        while True:
            # 1. Fit the current active terms
            formula = f"{self.target_col} ~ " + " + ".join(self.active_terms)
            model = smf.ols(formula, data=self.data).fit()
            pvals = model.pvalues.drop('Intercept', errors='ignore')
            
            # 2. Archive the current model object and its statistics
            self.models[iteration] = model
            self.history.append({
                'Iteration': iteration,
                'Removed_Term': removed_term_name,
                'R_squared': round(model.rsquared, 4),
                'Adj_R_squared': round(model.rsquared_adj, 4),
                'AIC': round(model.aic, 2),
                'BIC': round(model.bic, 2),
                'Max_P_Value': round(pvals.max(), 4) if not pvals.empty else None
            })
            
            if pvals.empty:
                break
            
            # 3. Determine the next term to remove
            protected_effects = self._get_protected_main_effects()
            removal_candidates = pvals.copy()
            for term in pvals.index:
                if term in protected_effects:
                    removal_candidates.drop(term, inplace=True)
            
            if not removal_candidates.empty:
                max_pval = removal_candidates.max()
                if max_pval > self.alpha:
                    term_to_remove = removal_candidates.idxmax()
                    actual_removed = self._remove_term(term_to_remove)
                    
                    if actual_removed:
                        removed_term_name = actual_removed
                        iteration += 1
                    else:
                        print(f"Warning: Could not match {term_to_remove} for removal.")
                        break 
                else:
                    break
            else:
                break
                
        self.summary_df = pd.DataFrame(self.history)
        return self.summary_df

    def get_model(self, iteration_index):
        """Retrieves the fitted statsmodels OLS object for a specific manual iteration."""
        if iteration_index in self.models:
            return self.models[iteration_index]
        else:
            raise ValueError(f"Iteration {iteration_index} not found. Available iterations: {list(self.models.keys())}")
