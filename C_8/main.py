import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

url = "./iris.csv"
df = pd.read_csv(url)
print(df.head(10))

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

kfold = KFold(n_splits=5, random_state=2023, shuffle=True)
scores = cross_val_score(knn, X_train, y_train, cv=kfold, scoring="accuracy")

print("Wyniki sprawdzianu krzyżowego:")
print(scores)
print(f"Średnia dokładność: {scores.mean()}")

param_grid = {
    'n_neighbors': list(range(1, 21)),  # liczba sąsiadów od 1 do 20
    'metric': ['euclidean', 'manhattan']
}
grid_search = GridSearchCV(knn, param_grid, cv=KFold(n_splits=5, random_state=2023, shuffle=True))
grid_search.fit(X_train, y_train)
results = pd.DataFrame(grid_search.cv_results_)
print(results)
results.to_csv("results.csv")

print(results["mean_test_score"])

print("Najlepsze parametry: ", grid_search.best_params_)
print("Najlepszy wynik: ", grid_search.best_score_)
best_model = grid_search.best_estimator_

best_predict_train = best_model.predict(X_train)
print("Dokładność na zbiorze treningowym: ", accuracy_score(y_train, best_predict_train))

best_predict = best_model.predict(X_test)
print("Dokładność na zbiorze testowym: ", accuracy_score(y_test, best_predict))

cm_train = confusion_matrix(y_train, best_predict_train)
print("Macierz pomyłek dla zbioru treningowego:")
print(cm_train)

report = classification_report(y_train, best_predict_train)
print(report)


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_report(results, code):
    pdf_filename = "report.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Adding results table to PDF
    results_table = results.to_string()
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, "Results:")
    c.setFont("Courier", 10)
    lines = results_table.split("\n")
    y = 680
    for line in lines:
        c.drawString(50, y, line)
        y -= 12

    # Adding code to PDF
    c.setFont("Helvetica", 12)
    c.drawString(50, y - 20, "Code:")
    c.setFont("Courier", 10)
    code_lines = code.split("\n")
    y -= 40
    for line in code_lines:
        c.drawString(50, y, line)
        y -= 12

    c.save()
    print("PDF report generated successfully.")

create_pdf_report(results, create_pdf_report.__code__.co_source)

