import argparse
import pandas as pd
from sklearn.metrics import roc_auc_score, precision_recall_curve, auc

def main(args):
    df = pd.read_csv(args.predictions_csv)
    y_true = df['label']
    y_score = df['prob']
    roc = roc_auc_score(y_true, y_score)
    precision, recall, _ = precision_recall_curve(y_true, y_score)
    pr_auc = auc(recall, precision)
    print(f"ROC AUC: {roc:.3f}")
    print(f"PR AUC: {pr_auc:.3f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions_csv", help="Path to the predictions CSV file")
    args = parser.parse_args()
    main(args)
