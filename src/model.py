from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import joblib

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split( X,y, test_size=0.2,random_state=42)

    #Decision Tree Classifier Model Training and Testing.
    dt_model = DecisionTreeClassifier()
    dt_model.fit(X_train, y_train)
    dt_pred = dt_model.predict(X_test)
    dt_acc  = accuracy_score(y_test, dt_pred)
    dt_CM = confusion_matrix(y_test, dt_pred)
    print(" \nDecision Tree Accuracy:", dt_acc)
    print(" Decision Tree Confusion_Matrix:\n",dt_CM)

    #Random Forest Classifier Model Training and Testing.
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test , rf_pred)
    rf_CM = confusion_matrix(y_test, rf_pred)
    print("\nRandom Forest Accuracy:",rf_acc)
    print("Random Forest Confusion_Matrix:\n",rf_CM)
    
    #Save the Random Forest Model because it has better accuracy.
    joblib.dump(rf_model,'phishing_model.pkl')
    print("Model Saved Successfully")
    
    
    
    return dt_model , rf_model