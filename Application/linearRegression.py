import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

learning_rate=0.01
epochs=10
my_batch_size=12


my_model = build_model(learning_rate)
trained_weight, trained_bias, epochs, rmse = train_model(my_model, my_feature, 
                                                         my_label, epochs,
                                                         my_batch_size)
plot_the_model(trained_weight, trained_bias, my_feature, my_label)
plot_the_loss_curve(epochs, rmse)