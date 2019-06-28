# HAR-bayesian-network

> The project consists in creating a bayesian network model in order to predict the action of a person, basing on the given training set which consists in 3D acceleration vectors for each sensor analyzed in the the project [Wearable computing: Accelerometers' data classication of body postures and movements](http://groupware.les.inf.puc-rio.br/har)

## Dependencies

You can install [pomegranate_v0.11.0](https://pypi.org/project/pomegranate/) and [scikit-learn_v0.21.2](https://pypi.org/project/scikit-learn/) using pip:

```bash
pip install pomegranate
pip install scikit-learn
```

## Execution allowed

Generate dynamically the model of the Bayesian Network (skeleton and CPDs)

```bash
python skeleton.py
```

Stimating the accuracy of the given model (based on 10% of the dataset)

```bash
python test.py
```

Make a sequence of inferences writing them in the input path as array of strings. Results will be printed in the output path (configurable in configs/Config.py). Following default paths:  
input: inference/in.txt  
output: inference/out.txt

```bash
python inference.py
```

Make a single custom inference from the given model and return the class-action, for example

```bash
python inference.py "x1=-1;y1=100;z1=-97;x2=4;y2=85;z2=-123;x3=24;y3=98;z3=-94;x4=-210;y4=-87;z4=-162"
```

## Authors

**Mattia Artifoni**

- [github/m-artifoni](https://github.com/m-artifoni)

**Luca Brena**

- [github/lbrena2](https://github.com/lbrena2)

**Federico Bottoni**

- [github/FedericoBottoni](https://github.com/federicobottoni)

## License

HAR-bayesian-network source code is licensed under the [MIT License](https://github.com/FedericoBottoni/HAR-bayesian-network/blob/master/LICENSE).
