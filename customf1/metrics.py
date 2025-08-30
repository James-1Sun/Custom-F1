def custom_f1_score(y_true, y_pred, weights=None):
    """
    Args:
        y_true (list or array): True labels.
        y_pred (list or array): Predicted labels.
        weights (dict): Optional. Class weights {class_label: weight}.

    Returns:
        float: Weighted F1 score.
    """

    # Unique classes
    classes = set(y_true) | set(y_pred)
    if weights is None:
        weights = {cls: 1.0 for cls in classes}

    f1_scores = {}
    for cls in classes:
        tp = sum((yt == cls) and (yp == cls) for yt, yp in zip(y_true, y_pred))
        fp = sum((yt != cls) and (yp == cls) for yt, yp in zip(y_true, y_pred))
        fn = sum((yt == cls) and (yp != cls) for yt, yp in zip(y_true, y_pred))

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        f1_scores[cls] = f1

    # Weighted average
    total_weight = sum(weights[cls] for cls in classes)
    weighted_f1 = sum(f1_scores[cls] * weights[cls] for cls in classes) / total_weight if total_weight > 0 else 0.0
    return weighted_f1

'''
#Example usage:
ai_actual = [0, 1, 1, 0, 2]
ai_pred = [0, 0, 1, 1, 2]
w = [1.0, 2.0, 0.5]
f1 = custom_f1_score(ai_actual, ai_pred, w)
print(f"Custom Weighted F1 Score: {f1}")
'''
