Motor Fault Detection System – Version 1

## 1. Problem - What problem are you trying to solve? 

Industrial motors can develop faults due to abnormal operating conditions such as excessive torque, high rotational speed, temperature changes, and tool wear. Detecting possible failures early can help support predictive maintenance and reduce unexpected equipment downtime.

This project develops a Python-based machine learning system that uses motor operating data to predict whether a motor is likely to experience a failure.

The system is designed as a learning-focused Version 1 prototype. Its prediction is produced by a trained machine learning model rather than by manually coded threshold rules.

## 2. Dataset - Where did the data come from? 
The project uses the **AI4I 2020 Predictive Maintenance Dataset**, which contains **10,000 motor-related records and 14 columns**.

The dataset includes motor operating information such as:
- Product quality/Variant Type (HIGH "H", MODERATE "M", or LOW "L")
- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]
- Machine Failure
- Several failure-mode indicators (TWF, HDF, PWF, OSF, RNF)

During data preparation, missing values were checked and no missing values were found. The dataset also contained no duplicate records during the Week 4 preparation stage.

The failure-mode indicator columns were not used as model input features because they directly describe failure conditions and could cause target leakage when predicting `Machine failure`.

## 3. Features - What information did you give the model? 

The following six features were provided to the machine learning model:
1. `Type`
2. `Air temperature [K]`
3. `Process temperature [K]`
4. `Rotational speed [rpm]`
5. `Torque [Nm]`
6. `Tool wear [min]`

The categorical `Type` feature was converted into numerical one-hot encoded columns (`Type_H`, `Type_L`, and `Type_M`) before training.

## 4. Target - What are you trying to predict?

The target variable is: `Machine failure`

It is a binary target:
- `0` = No machine failure
- `1` = Machine failure

The model therefore performs a *binary classification* task.

## 5. Models - Which models did you test? 

Two classification models were studied and compared during Week 4:
- *Decision Tree Classifier*
- *Random Forest Classifier*

Both models were trained using the same prepared dataset and the same 80/20 train-test split with `random_state=42` and stratification.

For the Version 1 fault-detection objective, the *Decision Tree* was selected because it achieved higher recall and F1-score than the Random Forest in the Day 4 experiment and produced fewer false negatives.

## 6. Results - How did they perform? 

**Day 4 Model Comparison**
|      Model    | Accuracy | Precision | Recall | F1-score |
|---------------|---------:|----------:|-------:|---------:|
| Decision Tree |  97.85%  |  68.66%   | 67.65% |  68.15%  |
| Random Forest |  98.10%  |  89.47%   | 50.00% |  64.15%  |

The Decision Tree produced the following confusion matrix:

```text
[[1911   21]
 [  22   46]]
```

Where:
- **True Negatives (TN): 1911** – healthy motors correctly identified as healthy.
- **False Positives (FP): 21** – healthy motors incorrectly identified as faulty.
- **False Negatives (FN): 22** – faulty motors incorrectly identified as healthy.
- **True Positives (TP): 46** – faulty motors correctly identified as faulty.

**Day 5 Version 1 Evaluation**
The final Day 5 program reproduced the same Decision Tree evaluation results:
- Accuracy: **97.85%**
- Precision: **68.66%**
- Recall: **67.65%**
- F1-score: **68.15%**

The system also accepts new motor sensor readings from the user and passes them through the trained model for prediction.

Example test input:
- Type: `L`
- Air temperature: `300 K`
- Process temperature: `309 K`
- Rotational speed: `2700 rpm`
- Torque: `11 Nm`
- Tool wear: `86 min`

The trained model predicted: `Machine failure = 1`
Therefore, the system reported that the motor is likely to experience a failure.

## 7. Best Model - Which model did you choose? 

The **Decision Tree Classifier** was selected as the best model for Version 1 of this project.

Although the Random Forest achieved slightly higher accuracy and much higher precision, the Decision Tree achieved better recall and F1-score in the Day 4 experiment and detected more of the actual failure cases.

For predictive maintenance, missed failures (false negatives) can be especially important because the system may report a motor as healthy when a failure is actually present. Therefore, recall was given greater importance for this Version 1 objective.

This selection is specific to the current experiment and does not mean that a Decision Tree is always better than a Random Forest.

## 8. Limitations - What could make your model inaccurate? 

Several factors may limit the accuracy and real-world usefulness of the system:
1. The AI4I 2020 dataset is a synthetic predictive-maintenance dataset, so it may not represent all conditions of real industrial motors.
2. The model was evaluated using a single 80/20 train-test split rather than extensive cross-validation.
3. Machine failures are less common than normal operations, so accuracy can appear high even when some failures are missed.
4. The current feature set does not include potentially valuable real-world signals such as vibration and acoustic measurements.
5. Model performance may change on equipment from different manufacturers, environments, operating ranges, or sensor systems.
6. The current Version 1 system is a learning prototype and should not be used as a safety-critical industrial protection system without further validation.
7. User-entered sensor values are not yet comprehensively validated for realistic operating ranges.

## 9. Future Improvements

Future versions could improve the system by:
1. Collecting real industrial motor sensor data.
2. Adding vibration, acoustic, current, and other condition-monitoring signals.
3. Applying cross-validation and systematic hyperparameter tuning.
4. Testing additional models such as optimized Random Forests, Gradient Boosting, and other suitable classifiers.
5. Addressing class imbalance using appropriate techniques where necessary.
6. Adding probability/confidence outputs instead of only a binary prediction.
7. Building a real-time dashboard for monitoring motor condition.
8. Connecting the model to IoT sensors for continuous data acquisition.
9. Exploring edge deployment for real-time motor monitoring.
10. Adding stronger input validation and user-friendly error handling.

## Conclusion

This project combines the Python data-processing, visualization, statistics, and machine-learning skills developed during Weeks 2–4 into a single predictive-maintenance application.

The Version 1 system loads and prepares motor data, trains a Decision Tree classifier, evaluates the model using multiple classification metrics and a confusion matrix, and predicts the failure status of a new motor from user-provided sensor readings.

The project demonstrates the complete basic machine-learning workflow from data preparation to model training, evaluation, and prediction.
