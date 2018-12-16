# K-Means

	1 Implementing K-means clustering algorithm 
		Note the following:
		• Use numpy.random.choice for the initialization step.
		• If at some iteration, there exists a cluster k with no points assigned to it, then do not update the
		  centroid of this cluster for this round.
		• While assigning a sample to a cluster, if there’s a tie (i.e. the sample is equidistant from two centroids),
		  you should choose the one with smaller index (like what numpy.argmin does).
		After you complete the implementation, execute bash kmeans.sh command to run k-means on toy
	dataset. You should be able to see three images generated in plots folder. In particular, you can see
	toy_dataset_predicted_labels.png and toy_dataset_real_labels.png and compare the clusters
	identified by the algorithm against the real clusters. Your implementation should be able to recover the
	correct clusters sufficiently well. Note that color coding of recovered clusters may not match that of correct 
	clusters. This is due to mis-match in ordering of retrieved clusters and correct clusters (which is fine).

	2 Image compression with K-means
		In the next part, we will look at lossy image compression as an application of clustering. The idea 
	is simply to treat each pixel of an image as a point xi, then perform K-means algorithm to cluster 
	these points, and finally replace each pixel with its centroid. Compress an image with K centroids given. 
	Specifically, complete the function transform_image in the file kmeansTest.py. After your implementation, 
	execute bash kmeans.sh again and you should be able to see an image baboon_compressed.png in the plots folder. 
	You can see that this image is distorted as compared to the original baboon.tiff.

	3 Classification with k-means 
		Another application of clustering is to obtain a faster version of the nearest neighbor algorithm. 
	Recall that nearest neighbor evaluates the distance of a test sample from every training point to 
	predict its class, which can be very slow. Instead, we can compress the entire training set to just 
	the K centroids, where each centroid is now labeled as the majority class of the corresponding cluster. 
	After this compression the prediction time of nearest neighbor is reduced from O(N) to just O(K)

	Note: 
		1) break ties in the same way as in previous problems; 
		2) if some centroid doesn’t contain any point, set the label of this centroid as 0.
		Complete the fit and predict function in KMeansClassifier in file kmeans.py. Once completed,
	run kmeans.sh to evaluate the classifier on a test set. For comparison, the script will also print accuracy of
	a logistic classifier and a nearest neighbor classifier. (Note: a naive K-means classifier may not do well but
	it can be an effective unsupervised method in a classification pipeline)