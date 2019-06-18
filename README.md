# HAR-bayesian-network

> The project consists in creating a bayesian network model in order to predict the action of a person, basing on the given training set which consists in 3D acceleration vectors for each sensor analyzed in the the project [Wearable computing: Accelerometers' data classication of body postures and movements](http://groupware.les.inf.puc-rio.br/har)

## Dependencies

You can install [pgmpy](https://pypi.org/project/pgmpy/) and [tqdm](https://pypi.org/project/tqdm/) using pip:

```bash
pip install pgmpy
pip install tqdm
```

## Execution allowed

Generate the skeleton of the Bn

```bash
python skeleton.py
```

Calculate the CPDs from the given skeleton

```bash
python cpds.py
```

Stimating the performance of the given model (skeleton + cpd)

```bash
python test.py
```

Make custom inference from the given model (skeleton + cpd)

```bash
python cpds.py
```

## Authors

**Mattia Artifoni 807466**

- [github/m-artifoni](https://github.com/m-artifoni)

**Luca Brena 808216**

- [github/lbrena2](https://github.com/lbrena2)

**Federico Bottoni 806944**

- [github/FedericoBottoni](https://github.com/federicobottoni)

## License

HAR-bayesian-network source code is licensed under the [MIT License](https://github.com/FedericoBottoni/HAR-bayesian-network/blob/master/LICENSE).
