import numpy as np
from scipy import stats

class KMeans():

    '''
        Class KMeans:
        Attr:
            n_cluster - Number of cluster for kmeans clustering (Int)
            max_iter - maximum updates for kmeans clustering (Int) 
            e - error tolerance (Float)
    '''

    def __init__(self, n_cluster, max_iter=100, e=0.0001):
        self.n_cluster = n_cluster
        self.max_iter = max_iter
        self.e = e

    def fit(self, x):
        '''
            Finds n_cluster in the data x
            params:
                x - N X D numpy array
            returns:
                A tuple
                (centroids a n_cluster X D numpy array, y a size (N,) numpy array where cell i is the ith sample's assigned cluster, number_of_updates an Int)
            Note: Number of iterations is the number of time you update the assignment
        ''' 
        assert len(x.shape) == 2, "fit function takes 2-D numpy arrays as input"
        np.random.seed(42)
        N, D = x.shape

        # TODO:
        # - comment/remove the exception.
        # - Initialize means by picking self.n_cluster from N data points
        # - Update means and membership until convergence or until you have made self.max_iter updates.
        # - return (means, membership, number_of_updates)
        initIndex = np.random.choice(N,self.n_cluster)
        centroids = x[initIndex]
        numOfIter = 0
        j = 10000000000
        y = np.zeros(N)
        while numOfIter < self.max_iter:
            numOfIter += 1
            x_ = np.repeat(x, self.n_cluster, axis=0)
            centroids_ = np.tile(centroids, (N,1))
            distance = np.linalg.norm(x_-centroids_, axis=1, keepdims=True).reshape(N, self.n_cluster)
            jNew = np.sum(np.min(distance, axis=1)) / N
            if np.abs(jNew - j) <= self.e:
                break
            j = jNew
            y = np.argmin(distance, axis = 1)
            for i in range(self.n_cluster):
                if i in y:
                    centroids[i] = np.average(x[y == i], axis=0)
        
        return (centroids, y.reshape(N,), numOfIter)

        # DONOT CHANGE CODE ABOVE THIS LINE
        #raise Exception(
            #'Implement fit function in KMeans class (filename: kmeans.py)')
        # DONOT CHANGE CODE BELOW THIS LINE

class KMeansClassifier():

    '''
        Class KMeansClassifier:
        Attr:
            n_cluster - Number of cluster for kmeans clustering (Int)
            max_iter - maximum updates for kmeans clustering (Int) 
            e - error tolerance (Float) 
    '''

    def __init__(self, n_cluster, max_iter=100, e=1e-6):
        self.n_cluster = n_cluster
        self.max_iter = max_iter
        self.e = e

    def fit(self, x, y):
        '''
            Train the classifier
            params:
                x - N X D size  numpy array
                y - (N,) size numpy array of labels
            returns:
                None
            Stores following attributes:
                self.centroids : centroids obtained by kmeans clustering (n_cluster X D numpy array)
                self.centroid_labels : labels of each centroid obtained by 
                    majority voting ((N,) numpy array) 
        '''

        assert len(x.shape) == 2, "x should be a 2-D numpy array"
        assert len(y.shape) == 1, "y should be a 1-D numpy array"
        assert y.shape[0] == x.shape[0], "y and x should have same rows"

        np.random.seed(42)
        N, D = x.shape
        # TODO:
        # - comment/remove the exception.
        # - Implement the classifier
        # - assign means to centroids
        # - assign labels to centroid_labels
        kms = KMeans(n_cluster=self.n_cluster, max_iter=self.max_iter, e=self.e)
        tuple1 = kms.fit(x)
        centroids = tuple1[0]
        labels = tuple1[1]
        centroid_labels = np.zeros(self.n_cluster)
        for i in range(self.n_cluster):
            centroid_labels[i] = stats.mode(y[labels == i])[0][0]

        # DONOT CHANGE CODE ABOVE THIS LINE
        #raise Exception(
            #'Implement fit function in KMeansClassifier class (filename: kmeans.py)')

        # DONOT CHANGE CODE BELOW THIS LINE

        self.centroid_labels = centroid_labels
        self.centroids = centroids

        assert self.centroid_labels.shape == (self.n_cluster,), 'centroid_labels should be a numpy array of shape ({},)'.format(
            self.n_cluster)

        assert self.centroids.shape == (self.n_cluster, D), 'centroid should be a numpy array of shape {} X {}'.format(
            self.n_cluster, D)

    def predict(self, x):
        '''
            Predict function

            params:
                x - N X D size  numpy array
            returns:
                predicted labels - numpy array of size (N,)
        '''

        assert len(x.shape) == 2, "x should be a 2-D numpy array"

        np.random.seed(42)
        N, D = x.shape
        # TODO:
        # - comment/remove the exception.
        # - Implement the prediction algorithm
        # - return labels
        x_ = np.repeat(x, self.n_cluster, axis=0)
        centroids_ = np.tile(self.centroids , (N,1))
        distance = np.linalg.norm(x_-centroids_, axis=1, keepdims=True).reshape(N, self.n_cluster)
        y = np.argmin(distance, axis = 1)
        labels = self.centroid_labels[y]

        # DONOT CHANGE CODE ABOVE THIS LINE
        #raise Exception(
            #'Implement predict function in KMeansClassifier class (filename: kmeans.py)')
        # DONOT CHANGE CODE BELOW THIS LINE
        return labels.reshape(N,)

