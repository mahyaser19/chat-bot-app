# Vehicle Maintenance Chatbot

## Demo (https://youtu.be/o8BI-6gtOSs)

[![](https://github.com/MuneebAnsari/vehicle-maintenance-chatbot/assets/22268574/63bc55aa-bbb0-4a3a-8732-9922a88c1d2c)](https://github.com/MuneebAnsari/vehicle-maintenance-chatbot/assets/22268574/443e16c6-f71f-44df-a198-d73589b5fbf0)

The Vehicle Maintenance Chatbot App is an application that enables users to upload their vehicle's owner/service manual in PDF format and ask questions related to their vehicle's maintenance, operation and health. The app leverages OpenAI GPT-3.5 language model, OpenAI embeddings and Approximate Neighbor Search (ANN) algorithm to predict accurate and relevant responses to the user's queries. Additionally, the app finds a relevant instructional video based on the user's query using Youtube Data API and extracts important procedure steps from the video's transcript, displaying each instructional step to the user along with the video segment for reference.


## Features

- **Upload PDF Manual:** Users can upload their vehicle's owner/service manual in PDF format

- **Recognize Vehicle** Recognizes the vehicle's make, model and year from the manual

- **Ask Questions:** Users can ask various questions related to their vehicle, such as how to change a tire, how to perform maintenance tasks, troubleshooting tips, and more.

- **Retrieve Answers from Manual:** The app understands the user queries and finds relevant answers within the manual.

- **Displays a Video Guide For Maintenance Tasks:** In addition to the answers from the service manual, an instructional video guide is provided for the user to follow along. The app extracts essential instructional steps from a video's transcript, ensuring that users receive detailed step-by-step instructions.
  All the extracted steps are displayed to the user along with the corresponding video segment, allowing users to follow the instructions more effectively.
