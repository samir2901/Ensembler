def gen_weights(x_test, y_test, models):
    '''
    returns a list of weights\n
    x_test -> test images\n
    y_test -> test labels\n
    models -> a list of models\n
    '''
    weights = []
    for model in models:        
        loss = model.evaluate(x_test, y_test)[0]
        weights.append(1/loss)
        
    return weights
