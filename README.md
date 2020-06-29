# Ensembler
 Ensembling on Deep Neural Networks

## Dependencies
- numpy

### Documentation

[I] Ensembler.py<br>
- weighted_avg_ensemble(x, weights, models) : Takes in arguments as x = input_data, weights = a list of weights, models = a list of deep learning models for classification.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a weighted average of the predictions made by the list of models.

- accuracy(predicted_values, y_truths) : Takes in arguments as predicted_value = predictions, y_truths = actual labels.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return accuracy of a model. Preferred to use for checking the performance of ensembler.
<br>
<br>
<i>Examples:</i>
<br>
1. 
<pre>
<code>
    models = [model_1, model_2, model_3] #list of model objects
    w = [0.4,0.5,0.7] #list of weights for the three models
    print(ensemble(x_test,w,models)) #prints the weighted average for a single set of features
</code>
</pre>
2.
<pre>
<code>
    models = [model_1, model_2, model_3] #list of model objects
    w = [0.4,0.5,0.7] #list of weights for the three models
    #let x_test, y_test be feature data array and test labels respectively
    predictions = []
    for i in range(len(x_test)):
        pred = ensemble(x_test[i],w,models)
        predictions.append(pred) #appending the prediction for each test data
    print(accuracy(predictions,y_test)) #prints the accuracy of the ensemble
</code>
</pre>
<br>
<br>
[II] ensemble_weight_generator.py<br><br>
gen_weights(x_test, y_test, models) : Takes in arguments as x_test = input_data, y_test = actual labels (ground truth), models = a list of deep learning models for classification.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a list of weights to be assigned to the predictions made by each of the models.

<i>Example:</i>
<br>
<pre>
<code>
    models = [model_1, model_2, model_3] #list of model objects
    w = gen_weights(x_test, y_test, models) #returns the list of weights for all the models
</code>
</pre>
    


