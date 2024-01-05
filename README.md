# Flaskeleton

<img src="./assets/flaskeleton_1.png" alt="Flaskeleton" style="height: 150px; width:150px;"/>

## Usage

There are many ways to use Flaskeleton, below you can choose the one you like best.

### Flaskeleton CLI

See about [Flaskeleton CLI](https://github.com/WilliamSampaio/flaskeleton-cli).

```bash
pip install flaskeleton-cli
# flaskeleton create --help
flaskeleton create --path /path/of/projects project_name
```

### Bash Script

#### Using CURL

```bash
# curl -s https://raw.githubusercontent.com/WilliamSampaio/flaskeleton/develop/create | bash
bash <(curl -s https://raw.githubusercontent.com/WilliamSampaio/flaskeleton/develop/create) -p /path/of/projects -f project_name
```

#### Using Wget

```bash
# wget -qO - https://raw.githubusercontent.com/WilliamSampaio/flaskeleton/develop/create | bash
bash <(wget -qO - https://raw.githubusercontent.com/WilliamSampaio/flaskeleton/develop/create) -p /path/of/projects -f project_name
```

### Git

```bash
git clone https://github.com/WilliamSampaio/flaskeleton.git project_name
```
