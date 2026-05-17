# Purdah and Patriarchy: Evaluating and Mitigating South Asian Biases in Open-Ended Multilingual LLM Generations

## Introduction

Large Language Models (LLMs) are critical in AI systems, yet their deployment in culturally diverse contexts, such as South Asia, poses unique challenges. South Asian societies are deeply shaped by gender roles, religious norms, marital expectations, childbearing pressures, and practices like *purdah* and patriarchy.

Biases reflecting these cultural norms are often embedded in the training data of LLMs, posing risks of reinforcing harmful stereotypes and marginalizing vulnerable identities. Existing work on bias in LLMs lacks coverage of South Asian intersectionality across languages, culture, and real-world applications.

This project contains the code and data for model generations, evaluations, bias lexicons, and more.

## Paper
Research paper has been accepted in the Proceedings of the 6th Workshop on Trustworthy Natural Language Processing (TrustNLP 2026), published by Association for Computational Linguistics (ACL)

## Repository Structure

- 📂 [Code Folder](./CODE): Contains scripts for model experiments, generation, bias scoring (including Bias TF-IDF), prompt formatting, and evaluation metrics.
- 📂 [Data Folder](./data): Includes curated identity templates, translated prompts, generated outputs, the cultural bias lexicon, and calculated metrics.
  - Includes [Bias_Scores_and_Top_Terms_by_Language.pdf](./data/lexicon_analysis/tfidf/tfidf_values/allTerms/Bias_Scores_and_Top_Terms_by_Language.pdf) which provides a detailed writeup by language of top biased terms, bias scores, frequent overall terms, and compares bias scores by identity, methods, applications, and languages.


## Citation

Please cite this work if you find it useful in your own research:

```bibtex
@inproceedings{mrinki2026,
  title={Purdah and Patriarchy: Evaluating and Mitigating South Asian Biases in Open-Ended Multilingual LLM Generations},
  author={Rinki, Mamnuya and Raj, Chahat and Mukherjee, Anjishnu and Zhu, Ziwei},
  booktitle={Proceedings of the 6th Workshop on Trustworthy Natural Language Processing (TrustNLP 2026)},
  publisher = "Association for Computational Linguistics",
  year={2026}
}