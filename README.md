## (Ex 1) Benchmark des solutions d’Inpainting

### Méthodes évaluées

Les méthodes suivantes ont été sélectionnées pour leur disponibilité open-source ou leur compatibilité avec des pipelines comme ComfyUI :

-   **SDXL Inpainting** : modèle SDXL spécialisé pour l’inpainting
-   **AlbedoXL + Foocus** : adaptation patch-based pour l’inpainting
-   **AlbedoXL + BrushNet** : architecture dual-branch pour l’inpainting
-   **Flux-Fill Dev** : variante Flux Dev spécialisée pour l’inpainting
-   **Flux-Fill Pro** : variante Flux Pro spécialisée pour l’inpainting

---

### Cas de test

Pour comparer ces approches, deux cas d’usage ont été utilisés :

-   Générer un shiba inu sur un tapis dans un salon
-   Ajouter un plaid rouge sur un canapé

Pour chaque cas :

-   Attention portée à la qualité de l’objet généré
-   Cohérence de l’image (motifs du tapis, lumière, ombres)

Chaque méthode a été testée avec deux stratégies :

-   **Inpainting global** : sur l’image entière
-   **Inpainting localisé** : sur une région recadrée et upscalée autour du masque

---

### Critères de comparaison

-   Temps d’inférence (tous < 30s sur hardware standard)
-   Capacité d’intégration (ex : facilité d’utilisation dans ComfyUI)
-   Adaptabilité (finetuning, LoRA, compatibilité workflows)
-   Modèle de tarification
-   Qualité d’image (détaillée plus loin)

---

### Tableau comparatif

| Nom                 | Intégration | Adaptabilité | Note   |
| ------------------- | ----------- | ------------ | ------ |
| SDXL inpainting     | Open-Source | Comfy        | Medium |
| AlbedoXL + Foocus   | Open-Source | Comfy        | Good   |
| AlbedoXL + Brushnet | Open-Source | Comfy        | Good   |
| Flux-fill dev       | Licence +   | Comfy        | Medium |
| Flux-fill pro       | API ++      | API          | Bad    |

---

### Résumé des solutions

-   **ComfyUI** offre flexibilité et contrôle sur la génération.
-   **Foocus** et **BrushNet** sont compatibles avec tout modèle SDXL standard.
-   **SDXL Inpainting** et **Flux-Fill Dev** nécessitent des modèles dédiés mais sont extensibles via LoRA.
-   **Flux-Fill Pro** fonctionne uniquement via API, avec peu de contrôle.

#### Coût :

-   **Flux-Fill Pro** : le plus cher, accès API externe requis.
-   **Flux-Fill Dev** : nécessite une licence.
-   Les autres : open-source et gratuits.

---

### Résultats par cas d’usage

#### 1. Shiba Inu sur un tapis

-   **Flux** : meilleure intégration du shiba, respect du motif du tapis.
-   **SDXL** : positionnement correct, mais qualité inférieure.
-   **Inpainting global** : meilleure cohérence d’échelle et de lumière.

#### 2. Plaid rouge sur un canapé

-   **SDXL Inpaint** et **BrushNet** : difficulté à intégrer le plaid naturellement.
-   **Foocus** : bonne prise en compte du prompt, mais qualité variable.
-   **Flux Fill Pro** : bonne qualité d’image, prompt respecté.
-   **Flux Fill Dev** : meilleure intégration et qualité, mais prompt moins respecté (plaid toujours plié).

---

### Conclusion

-   Les modèles SDXL sont moins bons pour l’intégration à l’environnement, qualité inégale.
-   Les modèles Flux sont meilleurs pour l’intégration et la qualité des objets.
-   **Flux Fill Pro** : meilleure prise en compte du prompt.
-   **Flux Fill Dev** : le plus adaptable, améliorable par finetuning, bon candidat pour la production.

---

### Pour aller plus loin

-   Évaluation plus large possible avec :
    -   Plus de générations
    -   Métriques quantitatives : CLIP Score, LPIPS, NIQE
    -   A/B testing humain

#### Améliorations possibles :

-   Tester des modèles avancés (in-context inpainting, InstructPix2Pix)
-   Améliorer la qualité via relighting et upscaling
-   Pour garder le fond original :
    1. Segmenter l’objet généré
    2. Le replacer sur l’image d’origine
    3. Appliquer un relighting pour l’intégration

---

Cette version améliore la lisibilité et la structure de ton README pour une meilleure compréhension et comparaison des solutions d’inpainting.
