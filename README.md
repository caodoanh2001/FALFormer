## FALFormer: Feature-aware Landmarks self-attention for Whole-slide Image Classification

Implementation of FALFormer (accepted in MICCAI2024)

**Abstract:** *Slide-level classification for whole-slide images (WSIs) has been widely recognized as a crucial problem in digital and computational pathology. Current approaches commonly consider WSIs as a bag of cropped patches and process them via multiple instance learning due to the large number of patches, which cannot fully explore the relationship among patches; in other words, the global information cannot be fully incorporated into decision making. Herein, we propose an efficient and effective slide-level classification model, named as FALFormer, that can process a WSI as a whole so as to fully exploit the relationship among the entire patches and to improve the classification performance. FALFormer is built based upon Transformers and self-attention mechanism. To lessen the computational burden of the original self-attention mechanism and to process the entire patches together in a WSI, FALFormer employs Nystr\"om self-attention which approximates the computation by using a smaller number of tokens or landmarks. For effective learning, FALFormer introduces feature-aware landmarks to enhance the representation power of the landmarks and the quality of the approximation. We systematically evaluate the performance of FALFormer using two public datasets, including CAMELYON16 and TCGA-BRCA. The experimental results demonstrate that FALFormer achieves superior performance on both datasets, outperforming the state-of-the-art methods for the slide-level classification. This suggests that FALFormer can facilitate an accurate and precise analysis of WSIs, potentially leading to improved diagnosis and prognosis on WSIs.*

## To-do list

- [ ] Step 1. Patch sampling & Feature extraction
- [x] Step 2. Process of Feature-based clustering to obtain landmark
- [ ] Pre-processed datasets ready for use
- [ ] Implementation of FALFormer & checkpoints
- [ ] Training & Validation document

## Process of Feature-based clustering to obtain landmarks

We implement the clustering part in `feature_based_clustering.py`.

After obtaining patch coordinates (stored in `/path/h5_files/`), use `feature_based_clustering.py` to do clustering and get cluster ids for patches in WSIs:

```
python feature_based_clustering.py --h5_path=/path/h5_files/ --save_path=/path/clusters/
```
