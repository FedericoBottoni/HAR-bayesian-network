# HAR-bayesian-network

> The project consists in creating a bayesian network model in order to predict the action of a person, basing on the given training set which consists in 3D acceleration vectors for each sensor analyzed in the the project [Wearable computing: Accelerometers' data classication of body postures and movements](http://groupware.les.inf.puc-rio.br/har)

## Dependencies

You can install the dependencies using pip:

```bash
pip install -r dependencies.txt
```

## Inference

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

## Generate the model

Generate dynamically the model of the Bayesian Network (skeleton and CPDs)

```bash
python skeleton.py
```

## Get accuracy

Stimating the accuracy of the given model (based on 10% of the dataset)

```bash
python test.py
```

## Authors
<a href="https://github.com/FedericoBottoni/HAR-bayesian-network/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=FedericoBottoni/HAR-bayesian-network" />
</a>

* **Federico Bottoni** - [FedericoBottoni](https://github.com/federicobottoni)

* **Mattia Artifoni** - [m-artifoni](https://github.com/m-artifoni)

* **Luca Brena** - [lbrena2](https://github.com/lbrena2)

## License

HAR-bayesian-network source code is licensed under the [MIT License](https://github.com/FedericoBottoni/HAR-bayesian-network/blob/master/LICENSE).
