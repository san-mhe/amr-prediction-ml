WORK STILL IN PROGRESS

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/san-mhe/amr-prediction-ml/main?urlpath=lab)


Biological Insights

Top SHAP genes: See results/top_20_shap_genes_filtered.csv for the 20 features most influential in resistance predictions.

Entrez summaries: Fetched via Biopython in results/gene_annotations_filtered.csv.


## CARD Ontology Usage

This project uses the **Antibiotic Resistance Ontology (ARO)** from the
[Comprehensive Antibiotic Resistance Database (CARD)](https://card.mcmaster.ca), 
which is available under a [Creative Commons CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

- Source ARO JSON download: `data/aro.json`
- Parsed annotations: `results/gene_annotations_card.csv`

**Attribution:**  
> Zhang, X. et al. Comprehensive Antibiotic Resistance Database (CARD): a resource for bacterial resistome analysis. *Nucleic Acids Research* 45, D566–D573 (2017).  
> Ontology available under CC-BY 4.0 from McMaster University.


---

## Deployment

### Run with Docker:

```bash
docker build -t amr-dashboard .
docker run -p 8050:8050 amr-dashboard
```

### Run in the cloud (Binder):

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/san-mhe/amr-prediction-ml/main?urlpath=lab)

### Pull image from Docker Hub:

```bash
docker pull sanmhe/amr-dashboard
```

### CI Status:

![Docker Build & Push](https://github.com/san-mhe/amr-prediction-ml/actions/workflows/docker.yml/badge.svg)

