# PokeGAN-2.0
Using GANs to generate pokemons again.

## Dataset
About 80,000 images of various Pokemon are downloaded from the Danbooru-2019 dataset<sup>[1](#dbftnote)</sup> and DuckDuckGo image search.

## Method
I tried to make the training easier with a modified approach to GAN training. The idea is to pre-train the generator to be moderately good at generating images, before starting the GAN training. Since GAN training is slow and unpredictable, using the adversarial training to fine-tune the pre-trained generator instead of completely training it from scratch should speed up convergence.

* <ins>Step-1</ins>: Train a Resnet-34 classifier to classify the 799 types of Pokemon images in the dataset. Note that if classification is not possible for a dataset, any other pre-text task (like [Rotnet]()) should also work. 

* <ins>Step-2</ins>: Freeze the trained Resnet-34 classifier and use it to encode images to 512d latent vectors. Train a generator to reconstruct the images from the encoded vectors. 

* <ins>Step-3</ins>: Use the pre-trained generator for normal GAN training.


<a name="dbftnote">1</a>: [Danbooru Dataset Maker](https://github.com/Atom-101/Danbooru-Dataset-Maker)
