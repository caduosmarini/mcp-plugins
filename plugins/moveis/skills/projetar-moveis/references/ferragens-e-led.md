# Ferragens, suportes e iluminação

## Ferragens e estrutura
Derive quantidades da montagem: dobradiças/calços conforme porta e fabricante, pés e distribuição de carga, conectores/cavilhas por junta, fixações entre módulos, apoios, fechos/puxadores, parafusos e ancoragens. Registre critério, unidade, item/kit e informação ainda a escolher. Comprimento útil de parafuso considera espessura do acessório e MDF remanescente.

Consulte fontes primárias e a ficha completa do modelo ao selecionar ferragem: material/espessura do painel, profundidade permitida, carga, espaçamento, parede, furação e acesso. Compatibilidade com 18 mm não prova compatibilidade com 280 mm de profundidade. Não extrapole carga de catálogo ou presuma que esconder uma mão francesa valida a estrutura.

Ao pedir suporte oculto, substitua a geometria e a solução de montagem, incluindo haste/placa/calço e usinagem. Não apenas esconda o mesh antigo. Recuo da parede pode diminuir embutimento e alterar esforço; resolva essa condição. Se não houver solução verificada, represente conceito claramente pendente de dimensionamento, com custo a cotar e instrução de não executar a usinagem proposta. Não reutilize medidas de um suporte conceitual como projeto estrutural aprovado.

## LED contínuo
Pergunte posição/cor apenas se não inferível da referência; declare premissas. “No fundo dos nichos” significa junto à borda traseira local, correndo pela largura do vão, não da frente para trás. Diferencie fundo do móvel e face da parede com relevo. Perfil superficial ou embutido deve ter seção real, difusor, tampas, fixação e folga; rasgo no MDF requer verificação da seção remanescente.

Uma fita com difusor produz fonte linear: no viewer use luz de área retangular (por exemplo RectAreaLight com bibliotecas compatíveis), não um spotlight único por nicho formando cones. Em Blender, áreas retangulares por trecho; material emissivo sozinho não garante iluminar a parede no renderer escolhido. Representação qualitativa não é cálculo luminotécnico. Preveja interruptor LED independente da iluminação de estúdio/técnica e desaparecimento coerente na desmontagem.

Considere segmentos comerciais/corte permitido da fita, interrupções em divisórias/apoios e pontos de alimentação. Não prometa uma linha fisicamente contínua atravessando obstáculos. Para compra: metros líquidos e reserva, barras/perdas de corte de perfil, difusores, tampas, clips/parafusos, terminais, fonte, dimmer, distribuição, cabos e instalação.

Calcule potência = metros × W/m e corrente = potência/tensão. Fonte com margem documentada e derating do fabricante; confira canais, dimmer e compatibilidade de tensão. Dimensione cabos por corrente, instalação, comprimento ida/volta e queda; declare se metragem é cabo bipolar ou condutores. Dimensionamento elétrico e conexão à rede dependem da especificação/instalador. Fonte acessível e ventilada; cabos protegidos, sem atravessar divisórias maciças sem passagem especificada. Circuitos independentes podem evitar queda em longos trechos. Documente posição da fonte e trajeto, mantendo rede e baixa tensão distinguidas. Preços de componentes não escolhidos permanecem a cotar.
