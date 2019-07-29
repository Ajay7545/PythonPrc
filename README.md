# PythonPrc
All About python basics

Introduction to Machine Learning¶
What is Machine Learning?
Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task.(Wikipedia)

Kevin P. Murphy :
The goal of machine learning is to develop methods that can automatically detect patterns in data, and then to use the uncovered patterns to predict future data or other outcomes of interest.

Hal Daume III :
Machine learning is about predicting the future based on the past.

Image
Supervised Learning
Supervised learning : It uses data that has labels i.e. the model has a general idea of what the target variable or the output looks like . Example the following dataset has images of fruits(feature set) along with a corresponding label for each image , therefore our training data comprises of both the feature set and target variable.

Image

Now we train this dataset on a suitable model/predictor that uses this information to derive a relationship(model parameters) between the image and its corresponding label.

Image
This derived relationship between features and label is used to make future predictions(label value) for unseen images.

Image

Supervised learning can be futher classified into regression(the target variable is continuous like the stock market) and classification(target variable consists of categories like normal or abnormal for some kind of diagonsis).

Supervised Learning Applications :

-Information extraction
-Object recognition in computer vision
-Optical character recognition
-Spam detection
-Pattern recognition
-Speech recognition
Unsupervised Learning
Unsupervised Learning : It uses data that does not has any labels i.e. the nature or form of output(target variable)is unknown.In Unsupervised learning we provide the model data( that contains only the feature set) and see if it can find some form structure in the data.

For example : If in the above dataset we only use the images and see if our model can identify some kind of structure in the data and use it group similar images together (i.e. form clusters).

Image

Supervised Learning Applications : Information extraction ,Object recognition in computer vision ,Optical character recognition , Spam detection , Pattern recognition and Speech recognition etc.

Unsupervised Learning Applications :

-learn clusters/groups without any label
-customer segmentation (i.e. grouping)
-image compression
-bioinformatics: learn motifs
Reinforcement Learning
Reinforcement learning (RL) is an area of machine learning concerned with how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward.Reinforcement learning differs from the supervised learning in a way that in supervised learning the training data has the answer key with it so the model is trained with the correct answer itself whereas in reinforcement learning, there is no answer but the reinforcement agent decides what to do to perform the given task. In the absence of training dataset, it is bound to learn from its experience.

Example : The problem is as follows: We have an agent and a reward, with many hurdles in between. The agent is supposed to find the best possible path to reach the reward. The following problem explains the problem more easily.

Image

The above image shows agent, star and lightning. The goal of the agent is to get the reward that is the star and avoid the hurdles that is lightning. The agent learns by trying all the possible paths and then choosing the path which gives him the reward with the least hurdles. Each right step will give the agent a reward and each wrong step will subtract the reward of the agent. The total reward will be calculated when it reaches the final reward that is the star.

RL Applications : game theory, control theory, operations research, information theory, simulation-based optimization, multi-agent systems, swarm intelligence, statistics and genetic algorithms etc.

Regression and Classification
Regression : The label (output variable) assumes a continuous range of values . For example :

Image

Applications of Regression :

-Economics/Finance ( Predict the value of a stock)
-Epidemiology
-Car/plane navigation (Angle of the steering wheel, acceleration)
-Temporal trends ( Weather over time)
Classification : The label (output variable) assumes a discrete range of values(i.e. is categorical) . For example :

Image

Classification Applications:

-Face recognition
-Character recognition
-Spam detection
-Medical diagnosis
-Biometrics
