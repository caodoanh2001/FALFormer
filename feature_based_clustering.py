import os
import h5py
from tqdm import tqdm
import numpy as np
import torch
import numpy as np
from fast_pytorch_kmeans import KMeans
import argparse
from tqdm import tqdm

def feature_based_clustering(wsi_h5, radius=1):
    total_coords, total_features = np.array(wsi_h5['coords']), np.array(wsi_h5['features'])
    assert total_coords.shape[0] == total_features.shape[0]
    N_clusters = 256 # number of clusters

    cuda_coords = torch.from_numpy(total_features).float().cuda()
    kmeans = KMeans(n_clusters=N_clusters, mode='euclidean')
    kmeans.fit(cuda_coords)
    cluster_labels = kmeans.predict(cuda_coords).cpu().detach().numpy()
    cluster_data = dict()

    cluster_data['cluster_labels'] = cluster_labels

    return cluster_data

def createDir_h5_to_pt(h5_path, save_path):
    pbar = tqdm(os.listdir(h5_path))
    for h5_fname in pbar:
        pbar.set_description('%s - Creating Graph' % (h5_fname[:12]))
        save_fname = os.path.join(save_path, h5_fname[:-3] + '.pt')
        try:
            wsi_h5 = h5py.File(os.path.join(h5_path, h5_fname), "r")
            G = feature_based_clustering(wsi_h5)
            torch.save(G, save_fname)
            wsi_h5.close()
        except OSError:
            pbar.set_description('%s - Broken H5' % (h5_fname[:12]))
            print(h5_fname, 'Broken')

parser = argparse.ArgumentParser(description='seg and patch')
parser.add_argument('--h5_path', type = str,
					help='path to folder containing coordinates stored in .h5 files')
parser.add_argument('--save_path', type = str,
					help='path to folder will be used to save clusters')

if __name__ == '__main__': 
    args = parser.parse_args()
    os.makedirs(args.save_path, exist_ok=True)
    createDir_h5_to_pt(args.h5_path, args.save_path)
