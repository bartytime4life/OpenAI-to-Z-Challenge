import optuna
from sklearn.model_selection import GroupKFold
from sklearn.ensemble import RandomForestClassifier
from model_training.utils import load_training_data

def objective(trial):
    X, y, groups = load_training_data()
    n_estimators = trial.suggest_int("n_estimators", 100, 500)
    max_depth    = trial.suggest_int("max_depth", 5, 50)
    clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, n_jobs=-1)
    cv = GroupKFold(n_splits=5)
    scores = []
    for train_idx, test_idx in cv.split(X, y, groups):
        clf.fit(X.iloc[train_idx], y.iloc[train_idx])
        scores.append(clf.score(X.iloc[test_idx], y.iloc[test_idx]))
    return sum(scores)/len(scores)

if __name__=="__main__":
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=50)
    print(study.best_params)
