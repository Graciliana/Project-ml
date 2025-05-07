# Lista de Verificação do Projeto de Aprendizado de Máquina

Esta lista de verificação pode guiá-lo em seus projetos de Aprendizado de Máquina.
São oito passos principais:

1. Foque no problema e olhe para o Quadro Geral;
2. Obtenha os dados;
3. Explore os dados para obter insights;
4. Prepare os dados para melhor expor os padrões de dados subjacentes aos algoritmos do Aprendizado de Máquina;
5. Explore vários diferentes modelos e liste os melhores;
6. Ajuste seus modelos e combine-os em uma ótima solução;
7. Apresente sua solução;
8. Lance, monitore e faça a manutenção de seu sistema.

## Foque o Problema e Olhe para o Quadro Geral

1. Defina o objetivo em termos de negócios;
2. Como sua solução será usada?
3. Quais são as soluções atuais/soluções alternativas (se houver)?
4. Como você deve enquadrar esse problema (supervisionado/não supervisionado, online/offline, etc.)?
5. Como o desempenho deve ser medido?
6. A medida de desempenho está alinhada com o objetivo de negócios?
7. Qual seria o desempenho mínimo necessário para atingir o objetivo dos negócios?
8. Quais são os problemas comparáveis? Você pode reutilizar experiências ou ferramentas?
9. A perícia humana está disponível?
10. Como você resolveria o problema manualmente?
11. Liste as suposições que você (ou outros) fizer(am) até agora;
12. Verifique as suposições, se possível.

## Obtenha os Dados

Obs: para que você possa obter facilmente novos dados, automatize o máximo possível.

1. Liste os dados que você precisa e quanto você precisa;
2. Encontre e documente onde você pode obtê-los;
3. Verifique quanto espaço ocupará;
4. Verifique as obrigações legais e obtenha autorização, se necessário;
5. Obtenha autorizações de acesso;
6. Crie um espaço de trabalho (com espaço de armazenamento suficiente);
7. Obtenha os dados;
8. Converta os dados para um formato que você possa manipular facilmente (sem alterá-los em si);
9. Garanta que informações confidenciais sejam excluídas ou protegidas (por exemplo, anonimato);
10. Verifique o tamanho e o tipo de dados (séries cronológicas, amostra, geográfica,etc.);
11. Experimente um conjunto de teste, coloque-o de lado e nunca olhe para ele (sem bisbilhotar dados!).

## Explore os Dados

Obs: tente obter insights de um especialista do setor para essas etapas.

1. Crie uma cópia dos dados para exploração (amostre até um tamanho gerenciável, se necessário);
2. Crie um notebook Jupyter para manter um registro da sua exploração de dados;
3. Estude cada atributo e suas características:
    • Nome;
    • Tipo (categórico, int/float, limitado/ilimitado, texto, estruturado, etc.);
    • Porcentagem dos valores ausentes;
    • Ruídos e tipos de ruído (estocásticos, anomalias, erros de arredondamento, etc.);
    • Possivelmente útil para a tarefa?
    • Tipo de distribuição (Gaussiana, uniforme, logarítmica, etc.).
4. Para tarefas de Aprendizado supervisionadas, identifique o atributo alvo;
5. Visualize os dados;
6. Estude as correlações entre atributos;
7. Estude como você resolveria o problema manualmente;
8. Identifique as transformações promissoras que você pode querer aplicar;
9. Identifique dados extras que seriam úteis (volte a “Obtenha os Dados” na página anterior);
10. Documente o que aprendeu.

## Prepare os Dados

Observações:
    • Trabalhe em cópias dos dados (mantenha o conjunto de dados original intacto);
    • Escreva funções para todas as transformações que você venha a aplicar nos dados, por cinco razões:
        - Para que você possa preparar facilmente os dados na próxima vez que obtiver novos conjuntos de dados;
        — Para que você possa aplicar essas transformações em projetos futuro;
        — Para limpar e preparar o conjunto de teste;
        — Para limpar e preparar novas instâncias de dados se sua solução for ao vivo;
        — Para facilitar o tratamento de suas opções de preparação como hiperparâmetros.

1. Limpeza de dados:
    • Conserte ou remova os outliers (opcional);
    • Preencha os valores ausentes (por exemplo, com zero, média, mediana... ) ou descarte suas linhas (ou colunas).
2. Seleção de características (opcional):
    • Descarte os atributos que fornecem informações inúteis para a tarefa.
3. Engenharia das caraterísticas, quando apropriado:
    • Discretizar caraterísticas contínuas;
    • Decompor caraterísticas (por exemplo, categórico, data/hora, etc.);
    • Adicionar transformações promissoras de características (por exemplo, log(x),sqrt(x), x2, etc.);
    • Agregar características em novas características promissoras.
4. Escala de características: padronizá-las ou normalizá-las.

## Modelos Promissores em Lista Resumida

Observações:

• Se os dados forem enormes, talvez você queira experimentar conjuntos de treinamento menores para poder treinar vários modelos diferentes em um tempo razoável (esteja ciente de que isso penaliza modelos complexos, como grandes redes neurais ou Florestas Aleatórias);

• Mais uma vez, tente automatizar ao máximo essas etapas.

1. Utilizando parâmetros padrão, treine muitos modelos rápidos de diferentes categorias (por exemplo, lineares, Naive-Bayes, SVM, Florestas Aleatórias, redes neurais, etc.);
2. Meça e compare seu desempenho;
    • Utilize validação cruzada N-fold e calcule a média e o desvio padrão da medida de desempenho nas N dobras para cada modelo.
3. Analise as variáveis mais significantes para cada algoritmo;
4. Analise os tipos de erros que os modelos cometem;
    • Quais dados um humano teria utilizado para preveni-los?
5. Tenha uma rápida rodada de seleção de características e engenharia;
6. Itere rapidamente uma ou duas vezes as cinco etapas anteriores;
7. Faça uma lista resumida dos três ou cinco principais modelos mais promissores,
preferindo modelos que cometam diferentes tipos de erros.

## Ajuste Fino do Sistema

Observações:
    • Utilize o máximo de dados possível para esta etapa, especialmente à medida que você se aproxima do final do ajuste fino;
    • Como sempre, automatize o que puder.

1. Faça um ajuste fino nos hiperparâmetros utilizando a validação cruzada;

    • Trate como hiperparâmetros suas escolhas de transformação de dados, especialmente quando você não tiver certeza sobre elas (por exemplo, devo substituir valores ausentes por zero ou pelo valor mediano? Ou simplesmente descartar as linhas?);

    • A menos que haja poucos valores de hiperparâmetros para explorar, prefira a pesquisa aleatória em relação à grid search. Se o treinamento for muito longo, prefira uma abordagem de otimização de Bayes (por exemplo, utilizando priorizações Gaussianas de processo, como descrito por Jasper Snoek, Hugo Larochelle e Ryan Adams <https://goo.gl/PEFfGr)>).

2. Tente os métodos do ensemble. Combinar frequentemente seus melhores modelos terá melhor desempenho do que executá-los individualmente;
3. Uma vez confiante em seu modelo final, meça seu desempenho no conjunto de testes para estimar o erro de generalização.

### `Não ajuste seu modelo depois de medir o erro de generalização: você apenas começaria a sobreajustar o conjunto de testes.`

## Apresente Sua Solução

1. Documente o que você fez
2. Crie uma boa apresentação;
    • Certifique-se de destacar primeiro o quadro geral.
3. Explique por que sua solução atinge o objetivo comercial;
4. Não se esqueça de apresentar pontos interessantes que você anotou ao longo do caminho;
    • Descreva o que funcionou e o que não funcionou;
    • Liste suas suposições e as limitações do seu sistema.
5. Assegure-se de que suas principais descobertas sejam comunicadas por meio de belas visualizações ou declarações fáceis de lembrar (por exemplo, “a renda média é o principal previsor dos preços imobiliários”).

## Lance!

1. Tenha sua solução pronta para a produção (conecte-se a entradas de dados da produção, escreva testes de unidade, etc.);
2. Escreva código de monitoramento para verificar o desempenho ao vivo em intervalos regulares do seu sistema e acione alertas quando ele cair;
    • Cuidado com a degradação lenta também: os modelos tendem a “apodrecer” à medida que os dados evoluem;
    • A medição do desempenho pode exigir um canal humano (por exemplo, por meio de um serviço de crowdsourcing);
    • Monitore também a qualidade de suas entradas (por exemplo, um sensor com defeito enviando valores aleatórios ou a saída de outra equipe se tornando obsoleta), o que é particularmente importante para sistemas de aprendizado online.
3. Volte a treinar seus modelos em novos dados regularmente (automatize o máximo possível).