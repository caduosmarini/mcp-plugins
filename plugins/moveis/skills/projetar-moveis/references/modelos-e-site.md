# Modelo, ambiente e viewer

Modele cada peça com ID, espessura e dimensões acabadas da fonte. Inclua base, portas e fundos somente quando previstos, além de ferragens/usinagens necessárias à revisão. Guarde o sólido completo e represente furos/rasgos, não somente bounding boxes. Exportar GLB isolado e instalado; evitar duplicar o móvel ao combinar cenas.

Entorno suficiente para testar: piso/rodapé, quinas, ressaltos, teto, janela/persiana, circulação e móveis preservados. “Antes” usa a situação atual; “depois” aplica remoções autorizadas. Escala estimada deve permanecer explícita. Para equipamentos relevantes, procure modelo existente com licença adequada e dimensões verificáveis; senão proxy simplificado identificado, sem distorcer para caber. Confira ventilação e conectores.

Renderize da geometria final, com luz de estúdio, materiais e sombras. Imagens geradas/editadas por IA podem complementar o estudo visual quando solicitadas, mas não substituem render dimensional nem validação de encaixe. Não use fotos privadas como textura pública sem autorização específica.

## Site quando solicitado
- Rotação, zoom, frente, lateral, planta e perspectiva; alternar isolado/ambiente e portas.
- Estúdio com sombras suaves e técnica uniforme; LED independente quando houver.
- Três cinzas de fundo no modo isolado para contraste, sem alterar MDF. Abrir em ambiente/estúdio quando fizer sentido e houver ambiente, respeitando preferências do projeto.
- Grade de todas as peças com IDs, medidas acabadas/brutas e bordas inequívocas.
- Slider interpolando diretamente transformações montadas para grid, inclusive rotações e espaçamento; sem fase intermediária nem salto de câmera. Ferragens e ambiente podem desaparecer progressivamente. Câmera contínua e enquadramento final legível.
- Downloads reais e responsividade celular/desktop; mostrar revisão, medidas estimadas e pendências, não detalhes internos de implementação.

Three.js é uma opção, não requisito universal. Use versões compatíveis de loaders/luzes e distribua dependências com licença; não dependa de CDN se puder empacotar localmente. Diferencie a transformação da peça, GLB em metros e dimensões em mm. Reutilize geometria importada para evitar aparência divergente do download.

Teste no navegador: modelos realmente carregados (não apenas fallback), contagem/IDs, vistas/zoom, portas, fundos, modo ambiente, LED ligado/desligado, slider em 0/intermediário/100 e retorno, sem salto, legibilidade móvel, links de download e estado inicial. Faça inspeção visual além de testes DOM; confira console/rede quando ferramentas permitirem. Na revisão, bust cache dos arquivos modificados sem trocar endereço público.
