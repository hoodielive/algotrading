n_features = 1
window_size = "N"
Input = 
LSTM =

input_layer = Input(shape=(window_size, n_features), name="Returns")

ltsm = LSTM(units=1, input_shape=(window_size, n_features),
            name="LTSM",
            return_sequences=False)(input_layer)

rnn = Mode1(inputs=input_layer, outputs=lstm)
