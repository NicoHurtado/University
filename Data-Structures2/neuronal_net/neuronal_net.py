from keras.models import Sequential
from keras.layers import Dense


def Red_Neuronal1(Xs,Ys):
    
    model = Sequential()
    
    model.add(Dense(12, input_dim=5, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', 
                optimizer='adam', 
                metrics=['accuracy'])
    
    X = Xs
    Y = Ys
    
    model.fit(X, Y, epochs=150, batch_size=10, verbose=False)
    
    scores = model.evaluate(X, Y)
    print(f'Accuracy: {scores[1]*100:.2f}%')
    
    result = model.predict(X)
    
    print(f'Average Prediction: {result.mean():.2f}')
    return result.mean()


def Red_Neuronal2(Xs,Ys):
    
    model = Sequential()
   
    model.add(Dense(6, input_dim=5, activation='tanh'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', 
                optimizer='adam', 
                metrics=['accuracy'])
    
    X = Xs
    Y = Ys
    
    model.fit(X, Y, epochs=50, batch_size=32, verbose=False)
    
    scores = model.evaluate(X, Y)
    print(f'Accuracy: {scores[1]*100:.2f}%')
    
    result = model.predict(X)
    
    print(f'Average Prediction: {result.mean():.2f}')
    return result.mean()
