from torch.distributions import MultivariateNormal, Categorical
import torch
class torch_gmm():
    def __init__(self,gmm):
        super().__init__()
        self.dists = []
        for i in range(gmm.means_.shape[0]):
            mean = gmm.means_[i]
            cov = gmm.covariances_[i]
            self.dists.append(MultivariateNormal(loc=torch.Tensor(mean),covariance_matrix=torch.Tensor(cov)))
        self.cat = Categorical(torch.tensor([1/len(self.dists) for i in range(len(self.dists))]))
    def sample(self,n_samples=1):
        ind = self.cat.sample()
        return self.dists[ind.item()].sample_n(n_samples)