# Purdah and Patriarchy: Evaluating and Mitigating South Asian Biases in Open-Ended Multilingual LLM Generations

## Introduction

Large Language Models (LLMs) are critical in AI systems, yet their deployment in culturally diverse contexts, such as South Asia, poses unique challenges. South Asian societies are deeply shaped by gender roles, religious norms, marital expectations, childbearing pressures, and practices like *purdah* and patriarchy.

Biases reflecting these cultural norms are often embedded in the training data of LLMs, posing risks of reinforcing harmful stereotypes and marginalizing vulnerable identities. Existing work on bias in LLMs lacks coverage of South Asian intersectionality across languages, culture, and real-world applications.

This project contains the code and data for model generations, evaluations, bias lexicons, and more.

## Paper
📖 [View Paper from TrustNLP @ ACL 2026](https://aclanthology.org/2026.trustnlp-main.18/)

🖼️ [View Poster from TrustNLP @ ACL 2026](./TRUSTNLP%20Poster%20Purdah%20and%20patriarchy.pdf)

Research paper has been accepted in the Proceedings of the 6th Workshop on Trustworthy Natural Language Processing (TrustNLP 2026), published by Association for Computational Linguistics (ACL).

## Repository Structure

- 📂 [Code Folder](./CODE): Contains scripts for model experiments, generation, bias scoring (including Bias TF-IDF), prompt formatting, and evaluation metrics.
- 📂 [Data Folder](./data): Includes curated identity templates, translated prompts, generated outputs, the cultural bias lexicon, and calculated metrics.
  - Includes [Bias_Scores_and_Top_Terms_by_Language.pdf](./data/lexicon_analysis/tfidf/tfidf_values/allTerms/Bias_Scores_and_Top_Terms_by_Language.pdf) which provides a detailed writeup by language of top biased terms, bias scores, frequent overall terms, and compares bias scores by identity, methods, applications, and languages.


## Citation

Please cite this work if you find it useful in your own research:

```bibtex
@inproceedings{rinki-etal-2026-purdah,
    title = "Purdah and Patriarchy: Evaluating and Mitigating {S}outh {A}sian Biases in Open-Ended Multilingual {LLM} Generations",
    author = "Rinki, Mamnuya  and
      Raj, Chahat  and
      Mukherjee, Anjishnu  and
      Zhu, Ziwei",
    editor = "Chang, Kai-Wei  and
      Mehrabi, Ninareh  and
      Krishna, Satyapriya  and
      Das, Anubrata  and
      Dhamala, Jwala  and
      Cao, Yang Trista  and
      Kumarage, Tharindu  and
      Ramakrishna, Anil  and
      Christodoulopoulos, Christos  and
      Wan, Yixin  and
      Galystan, Aram  and
      Kumar, Anoop  and
      Gupta, Rahul",
    booktitle = "Proceedings of the 6th Workshop on Trustworthy {NLP} ({T}rust{NLP} 2026)",
    month = jul,
    year = "2026",
    address = "San Diego, California",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.trustnlp-main.18/",
    doi = "10.18653/v1/2026.trustnlp-main.18",
    pages = "295--315",
    ISBN = "979-8-89176-418-7",
    abstract = "Evaluations of Large Language Models (LLMs) often overlook intersectional and culturally specific biases, particularly in underrepresented multilingual regions like South Asia. This work addresses these gaps by conducting a multilingual and intersectional analysis of LLM outputs across 10 Indo-Aryan and Dravidian languages, identifying how cultural stigmas influenced by purdah and patriarchy are reinforced in generative tasks. We construct a culturally grounded bias lexicon capturing previously unexplored intersectional dimensions including gender, religion, marital status, and number of children. We use our lexicon to quantify intersectional bias and the effectiveness of self-debiasing in open-ended generations (e.g., storytelling, hobbies, and to-do lists), where bias manifests subtly and remains largely unexamined in multilingual contexts. Finally, we evaluate two self-debiasing strategies (simple and complex prompts) to measure their effectiveness in reducing culturally specific bias in Indo-Aryan and Dravidian languages. Our approach offers a nuanced lens into cultural bias by introducing a novel bias lexicon and evaluation framework that extends beyond Eurocentric or small-scale multilingual settings."
}