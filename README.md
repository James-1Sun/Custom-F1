# Custom-F1
This is a package for custom weighted F1 calculation

Function:
    custom_f1_score(y_true, y_pred, weights=None)
    
Args:
    y_true (list or array): True labels.
    y_pred (list or array): Predicted labels.
    weights (dict): Optional. Class weights {class_label: weight}.

Returns:
    float: Weighted F1 score.

# Installation

Clone the repo and install locally:
bash
git clone https://github.com/James-1Sun/Custom-F1.git
cd Custom-F1
pip install .
