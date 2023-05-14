# Questions about Machine Learning Papers

## What are some common use cases for machine learning in practical applications or research prototypes?

Kostakos et al. mention several common use cases for machine learning.( wearable computing) It is stated that a popular use for machine learning techniques in HCI is to model human behavior, for example activity recognition.
Another use case in HCI is to develop novel user-interface techniques. Kostakos et al. mention reaction to user input(e.g. gesture recognition), smartphone battery conservation (idle time for auto shut off can be shortened) and intelligent mobile notifications (group notifications regarding apps and social relationship between sender and receiver --> learning the most opportune moment for the delivery of a notification carrying a specific type of information). 
The prediction of future users' activities and interaction is described as another area of interest (Das Ziel ist die Entwicklung vollwertiger Systeme für vorausschauendes Rechnen).

D. Scully mentions that machine learning can be used to detect which headlines are being clicked and based on this data recommend similar headlines to the users.

## Which problems of machine learning do the authors of the papers identify?

Kostakos et al. mention several problems of machine learning. Although some machine learning methods provide insight into interpretation, the same cannot be said of all of them. Some state of the art algorithms, such as deep learning techniques provide limited information about the inner workings of the models. These techniques leave researchers without control of the inner workings and don’t provide them with a form of language to construct and test hypotheses, like older hypothesis-testing approaches did.

Another problem Kastos et al. mention, ist that most results of machine learning algorithms provide insight about association relationships and not causality relationships. Therefore researchers should be more careful, since results may be based on correlation and not causality.

Additionally they mention that classifiers with accuracy of 80% are considered as "good enough", but you can't tell whether it's good or not, since the accuracy does not include the complexity of the machine learning task.

D. Scully et al. mention technical debt as a problem. Since mostly the goal is to develop fast rather than good, the maintenance, documentation and improvement of the code and quality will have long-term consequences. They mention the CACE-principle: Change anything - change everything. Meaning that even little changes in the machine learning code will alter the way things will get processed and predicted. Mostly unknown and/or unstable dependencies gather technical dept.

For example when the output of a model is also again the input of the same model, especially when the output is processed over a longer period of time it can prevent the model to do up-to-date predictions (hidden feedback loop). Furthermore input from a different system will be a problem as soon as this input changes its data structure or even stops delivering the signal (unstable data dependency). Some models may have code/functions that bring little value for accuracy and at same time bring a complex overhead process with it. Processing correlated data without checking causation, doing manual thresholds and having too much glue-code are also adding up the technical dept. So delivering a first model is simple, but improving it continuously with technical debt “in” the code is difficult. 

## What are the credentials of the authors with regard to machine learning? Have they published research on machine learning (or using machine-learning techniques) previously?

Vassilis Kostakos is a computer engineering professor. His research interests are: ubiquitous computing, human-computer interaction, and social computing. He has a Ph.D. in computer science from the University of Bath.
Worked with ML before, but not too much. Is not in his field of interest. Nevertheless, he has published several papers with machine learning in the context of mobile devices.

Mirco Musolesi is a reader in data science at UCL and Faculty Fellow at the Alan Turing
Institute. His research interests lie at the intersection of ubiquitous computing, mobile sensing, large-scale data mining, and network science. He has a Ph.D. in computer science
from University College London. He has published lots of stuff about deep learning, reinforcement learning and machine learning.

D Scully is currently the CEO of Kaggle, a platform for data science, was the director of Google Brain and doing research about Machine Learning and Artificial Intelligence. 

Daniel Golovin has also published some machine learning papers in the past, works for Google Brain (leadership position in Pittsburgh) and founded Vizier, a optimization tool used at Google for machine learning models.

Eugene Davydov has done a lot of research in the bio-informatics topic, mostly about computational biology.Gary Holt and Todd Phillips have only published two papers in the ML-research field. To the other authors (Dietmar Ebner, Vinay Chaudhary, Michael Young) we could only find this paper. 

