from eda import run_eda
from model import train_model
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

# Load dataset
X, y = run_eda()

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train models (reusing my  function)
dt_model, rf_model = train_model(X, y)

# Predictions
dt_pred = dt_model.predict(X_test)
rf_pred = rf_model.predict(X_test)

# DECISION TREE CONFUSION MATRIX
dt_cm = confusion_matrix(y_test, dt_pred)

plt.figure()
sns.heatmap(dt_cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Decision Tree Confusion Matrix")
plt.savefig("dt_confusion_matrix.png", dpi=400)

# RANDOM FOREST CONFUSION MATRIX
rf_cm = confusion_matrix(y_test, rf_pred)

plt.figure()
sns.heatmap(rf_cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Random Forest Confusion Matrix")
plt.savefig("rf_confusion_matrix.png", dpi=400)

# ACCURACY COMPARISON
dt_acc = accuracy_score(y_test, dt_pred)
rf_acc = accuracy_score(y_test, rf_pred)

models = ['Decision Tree', 'Random Forest']
accuracies = [dt_acc, rf_acc]

plt.figure()
plt.bar(models, accuracies)
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Model Comparison")
plt.savefig("accuracy_comparison.png", dpi=400)

plt.show()