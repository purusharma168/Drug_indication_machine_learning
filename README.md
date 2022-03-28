# Drug_indication_machine_learning

# Problem Statement:-
To build a classification model to predict drug name information with the help of this data set which consists of Drugs and their physical and chemical properties.

# Data information:
## Content
The opportunity is equally compelling in drug discovery, particularly in areas of high unmet need such as rare and hard-to-treat cancers and neurodegenerative conditions. Artificial intelligence can ingest and reason over information from the scientific literature and databases, as well as patient-level data, to identify potential approaches to treat diseases by proposing a drug target, designing a molecule, and defining patients in which to test that molecule to drive greater clinical success.
Here in this data set consists of physical and chemical properties of drugs with their names .This dataset is a lightly cleaned-up version of the non-proprietary version of the Drug Information Database . Some duplicate rows were removed, and column headers were renamed for brevity.
Column Description and Abbreviations

## Data link:-  https://drive.google.com/drive/folders/1DZGMk55aLpsU4zZ3qGpvCOkNzq-3PD_A?usp=sharing


# Approch:-

Export Data from database to CSV for Training : Here we will be exporting all batches of data from database into one csv file for training.

# Data Splitting :
We filter the columns for splitting the data for train and test for further uses

# Data Preprocessing :
We will be exploring our data set here and do EDA if required and perform data preprocessing depending on the data set. We first explore our data set in Jupyter Notebook and decide what pre-processing and Validation we have to do such as imputation of null values, etc and then we have to write separate modules according to our analysis, so that we can implement that for training as well as prediction data.

# Data Training : 
We trained a RandomForestClassifier model in our notebook and was good on it. We trained with our processed data.

# Model Evaluation :
Model evaluation done by classification and report was saved to .pkl file

# Model Saving :
we will save our models so that we can use them for prediction purpose.

# Cloud Setup : 
Here We will do cloud setup for model deployment. Here we also create our flask app and user interface and integrate our model with flask app and UI

# Push app to cloud :
After doing cloud setup and checking app locally, we will push our app to cloud to start the application.


# Demo:-


