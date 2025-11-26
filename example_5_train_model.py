import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

df = pd.read_csv("features_dataset.csv")
print(f"📄 Loaded dataset with {len(df)} samples")

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("\n🔹 Training samples:", len(X_train))
print("🔹 Testing samples:", len(X_test))

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print("\n🌲 RandomForest Accuracy:", round(rf_acc * 100, 2), "%")

svm = SVC(kernel="rbf", gamma="scale", probability=True)
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)
svm_acc = accuracy_score(y_test, svm_pred)
print("⚙️  SVM Accuracy:", round(svm_acc * 100, 2), "%")

best_model = rf if rf_acc >= svm_acc else svm
best_name = "RandomForest" if rf_acc >= svm_acc else "SVM"

print(f"\n✅ Best Model: {best_name}")
y_pred = best_model.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

joblib.dump(best_model, "stego_model.pkl")
print(f"\n💾 Saved best model as 'stego_model.pkl'")
