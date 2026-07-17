# evaluate.py - Evaluation metrics for gear defect detection

def compute_metrics(results):
    """
    Compute evaluation metrics from a list of (actual, predicted) tuples.
    Labels: 'defective' = Positive, 'normal' = Negative.
    Returns a dictionary with all metrics.
    """
    tp = 0  # True Positive: actually defective, predicted defective
    tn = 0  # True Negative: actually normal, predicted normal
    fp = 0  # False Positive: actually normal, predicted defective
    fn = 0  # False Negative: actually defective, predicted normal

    for actual, predicted in results:
        if actual == "defective" and predicted == "defective":
            tp += 1
        elif actual == "normal" and predicted == "normal":
            tn += 1
        elif actual == "normal" and predicted == "defective":
            fp += 1
        elif actual == "defective" and predicted == "normal":
            fn += 1

    total = tp + tn + fp + fn

    # Accuracy
    accuracy = (tp + tn) / total if total > 0 else 0

    # Precision
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0

    # Recall
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0

    # F1 Score
    if precision + recall > 0:
        f1 = 2 * (precision * recall) / (precision + recall)
    else:
        f1 = 0

    metrics = {
        "total": total,
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

    return metrics


def print_metrics(metrics):
    """Print evaluation metrics in a nice format."""
    print("\n" + "=" * 50)
    print("   Evaluation Metrics")
    print("=" * 50)

    print(f"  Total Images : {metrics['total']}")
    print(f"  Accuracy     : {metrics['accuracy'] * 100:.2f}%")
    print(f"  Precision    : {metrics['precision'] * 100:.2f}%")
    print(f"  Recall       : {metrics['recall'] * 100:.2f}%")
    print(f"  F1 Score     : {metrics['f1'] * 100:.2f}%")

    print("\n  Confusion Matrix:")
    print("                  Predicted")
    print("                DEFECTIVE  NORMAL")
    print(f"  Actual DEF      {metrics['tp']:>5}     {metrics['fn']:>5}")
    print(f"  Actual NOR      {metrics['fp']:>5}     {metrics['tn']:>5}")

    print("=" * 50)


def save_metrics(metrics, output_path):
    """Save evaluation metrics to a text file."""
    import os

    folder = os.path.dirname(output_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    with open(output_path, "w") as f:
        f.write("Gear Defect Detection - Evaluation Metrics\n")
        f.write("=" * 45 + "\n\n")

        f.write(f"Total Images : {metrics['total']}\n")
        f.write(f"Accuracy     : {metrics['accuracy'] * 100:.2f}%\n")
        f.write(f"Precision    : {metrics['precision'] * 100:.2f}%\n")
        f.write(f"Recall       : {metrics['recall'] * 100:.2f}%\n")
        f.write(f"F1 Score     : {metrics['f1'] * 100:.2f}%\n\n")

        f.write("Confusion Matrix:\n")
        f.write("                  Predicted\n")
        f.write("                DEFECTIVE  NORMAL\n")
        f.write(f"  Actual DEF      {metrics['tp']:>5}     {metrics['fn']:>5}\n")
        f.write(f"  Actual NOR      {metrics['fp']:>5}     {metrics['tn']:>5}\n\n")

        f.write("Labels:\n")
        f.write("  TP = True Positive  (defective gear correctly detected)\n")
        f.write("  TN = True Negative  (normal gear correctly passed)\n")
        f.write("  FP = False Positive (normal gear wrongly flagged)\n")
        f.write("  FN = False Negative (defective gear missed)\n")

    print(f"  Metrics saved to {output_path}")
