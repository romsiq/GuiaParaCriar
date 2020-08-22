# BIBLIOTECAS NECESSARIAS

library(readr)       # O objetivo do 'readr' é fornecer uma maneira rápida e amigável de ler dados retangulares (como 'csv', 'tsv' e 'fwf'). 
library(data.table)  # Agregação rápida de grandes dados.
library(dplyr)       # Manipulação de Dados como Adicionar, Selecionar, Filtrar, Somar e alterar ordem dos dados. 

# LEITURA DOS DADOS
carros <- read.csv("/Users/romsiq/Downloads/autos.csv", sep = ";")  # Faz a leitura dos dados do arquivo csv e aloca em uma variável.

# CONHECER OS DADOS
nrow(carros)   # Verifica numero de registros
ncol(carros)   # Verifica numero de colunas
str(carros)    # Apresenta estrutura dos dados
head(carros)   # Lista os primeiros registros
tail(carros)   # Lista os ultimos registros
# SELECIONANDO DADOS
head(select(carros, c(6:7, 1)))   # seleciona as colunas 6 e 7 e a coluna 1
table(carros$make)        # Apresenta os valores da coluna selecionada em formato tabela.
table(carros$fuel.type)   # Apresenta os valores da coluna selecionada em formato tabela.

# VERIFICANDO E TRATANDO DADOS NULOS (SE HOUVER)
is.na(carros)            # Verifica Valores Nulo
sum(is.na(carros$make))  # Soma valores Nulos de uma variável 
colSums(is.na(carros))   # Verifica e Soma valores nulos das variáveis
# E se precisarmos substituir valores nulo por zero?
is.na_replace_0 <- carros$price   # Poderia duplicar a coluna price da base de dados carros.
is.na_replace_0[is.na(is.na_replace_0)] <- 0    # Alterar pelo valor 0
# Ou aplicar a média: 
is.na_replace_mean <- carros$price 
price_mean <- mean(is.na_replace_mean, na.rm = TRUE)        # Calcula a média
is.na_replace_mean[is.na(is.na_replace_mean)] <- price_mean # Alterar o valor pela média

# FILTRAR, SELECIONAR DADOS
filter(carros, make == "audi") %>% select(horsepower, price)  # Filtra os dados iguais a variável "Audi" selecionando os dados das variáveis "horsepower" e "price" 

# MEDIDAS
summary(carros)         # Apresenta as medidas estatísticas 
quantile(carros$price)  # Podemos conhecer um pouco mais a distribuição dos dados nos decís.

# AGRUPAMENTO, RESUMO, ORDENAR
# Vamos agrupar os fabricantes de carros pelo estilo do carro, tirar a média de preço e apresentar os TOP 10. 
ranking <- group_by(carros, make, body.style) %>% summarize(carros = mean(price)) %>% as.data.frame %>% arrange(desc(carros))
head(ranking, 10)   # Apresentando os 10 primeiros.
tail(ranking, 10)   # # Apresentando os 10 ultimos.


# VISUALIZAÇÃO DE DADOS
# BOXPLOT
boxplot(carros$price, col = "blue")
boxplot(price ~ num.cylinders, data = carros, col = "red")
# HISTOGRAMA
hist(carros$price, col = "green")
rug(carros$price)  # Obter um pouco mais de detalhes no histograma. 
# DISPERSÃO
#scatter sobre as variaveis horsepower e engine.size
with(carros, plot(horsepower, engine.size))



