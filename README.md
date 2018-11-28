## NLP applied to Event Driven Investing Profit Warning Prediction
Applying NLP (Natural Language Processing) techniques to predict profit warnings using conference call transcripts

## Data
- Scrappy and Selenium used to scrappe conference call transcripts data.
- The two key websites used to obtain the data were: i) RTT News (www.rttnews.com , data about US profit warnings) and Seeking Alpha (seekingalpha.com, publicly available conference call transcripts).
- 93 conference call transcripts scrapped containing 42 transcripts from future profit warning stocks and 51 transcripts from healthy stocks.
- Coverage considered: only US companies within the Industrial sector, mainly capital goods companies, for the period 4Q16 and 1Q17

## Feature Engineering: 
- More than 90 features were created out from the whole conference call transcripts and its MD and Q&A parts. 
- Python NLP-related libraries used in this analysis were textstat, NLTK, VADER, pySentiment, spaCy and Gensim. 
- Several NLP dimensions were measured in order to generate reliable and significant predictor categories related to text physical properties (size, number of words, number of syllables etc), text complexity (readability indices like Smog Index, padding), lexicon complexity (number of difficult words, Brown Dictionary), semantic and syntactic sentiment indices.

## Notes:
- Read the powerpoint attached or the NYCDSA blog post in order to get familiar with the data and the different sources of information https://nycdatascience.com/blog/student-works/predicting-profit-warnings-nlp-applied-conference-call-transcripts-analysis/
- Different warned me as of 2018 about problems to scrapp seeking alpha's website using my scrappy crawler program. Seeking Alpa has apparently changed its website since I last crawled the data in 2017.
- If you need to obtain more conference call data from sa's wesbite, I recommend you to tweak my crawler or also check some good tips in https://stackoverflow.com/questions/48756326/web-scraping-results-in-403-forbidden-error. Best advice is to try to obtain, if possible, the conference call transcripts from a subscription-based data provider (Factset, Bloomberg, etc) on a user-friendly format in order to save the web crapping pain.

## Pending:
Future work in this project will be focused on:
- Inclusion of other sectors and industries. 
- Extension of the time span to at least five years.
- Tagging and standalone analysis of management team different members (CEO, CFO, COO, etc) and analysts 
- Addition of more complex modeling methods such as neural networks.
