import argparse
import csv
import json
import os
from src.RevivalNet import score_features
from src.TimefoldNet import infer_epoch

def load_master_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_feedback(feedback_path):
    if not feedback_path or not os.path.exists(feedback_path):
        return {}
    with open(feedback_path, 'r', encoding='utf-8') as f:
        feedback_list = json.load(f)
    feedback_map = {}
    for entry in feedback_list:
        aoi = entry.get('AOI_ID')
        feedback_map.setdefault(aoi, []).append(entry.get('notes'))
    return feedback_map

def score_aoi_record(aoi, feedback_map):
    # Extract feature values
    features = {
        'elev_mean': float(aoi.get('elev_mean', 0)),
        'slope': float(aoi.get('slope', 0)),
        'pattern_score': float(aoi.get('pattern_score', 0)),
        'flora_flag': aoi.get('flora_flag', 'False') == 'True',
        'trail_link': float(aoi.get('trail_link', 0)),
    }
    base_score = score_features(features)
    # Incorporate feedback: if any notes exist, boost score by 0.05 per note
    notes = feedback_map.get(aoi['AOI_ID'], [])
    score = base_score + 0.05 * len(notes)
    # Clip to max 1.0
    score = min(score, 1.0)
    epoch = infer_epoch(aoi)
    return score, epoch, notes

def main(args):
    # Load master AOI list
    aoi_list = load_master_csv(args.input)
    # Load feedback notes if provided
    feedback_map = load_feedback(args.feedback)
    # Score and annotate AOIs
    results = []
    for aoi in aoi_list:
        score, epoch, notes = score_aoi_record(aoi, feedback_map)
        aoi['Score'] = score
        aoi['Epoch'] = epoch
        aoi['FeedbackNotes'] = "; ".join(notes) if notes else ""
        results.append(aoi)
    # Write AOI index
    with open(args.output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"Wrote {len(results)} AOIs with scores to {args.output}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run AOI scoring pipeline')
    parser.add_argument('--input', default='data/Archaeology_master.csv', help='Path to master AOI CSV')
    parser.add_argument('--feedback', default=None, help='Path to feedback JSON')
    parser.add_argument('--output', default='results/AOI_index.csv', help='Path for scored output')
    parser.add_argument('--refresh-data', action='store_true', help='Refresh datasets before scoring (not implemented)')
    args = parser.parse_args()
    main(args)
