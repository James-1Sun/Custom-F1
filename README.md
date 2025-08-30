# Custom-F1
This is a package for custom weighted F1 calculation

Function:
    cf1(y_true, y_pred, weights=None)
    
Args:
    y_true (list or array): True labels.
    y_pred (list or array): Predicted labels.
    weights (dict): Optional. Class weights {class_label: weight}.

Returns:
    float: Weighted F1 score.
