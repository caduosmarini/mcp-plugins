# Fonte única e contrato mínimo

Use JSON ou estrutura equivalente versionada. Coordenadas sugeridas: X largura, Y altura desde piso, Z profundidade desde parede; milímetros. GLB em metros. Cada peça tem ID imutável, transformação, tamanho XYZ, orientação do retângulo L/D e espessura. Uma lista derivada de cortes não substitui a fonte dos parâmetros.

Registre decisões/proveniência (`fornecida`, `estimada`, `verificada`), referência da medida (face externa/vão livre/piso/parede), tolerância, revisão e status de fabricação. Separe medidas acabadas, substrato bruto, usinagens e ferragens. Preços desconhecidos são `null`, nunca zero implícito.

Contrato do validador: `units: mm`, `revision`, `parts`, `sheets`, `passes`. Uma peça por ID/instância (quantidade física expandida): `finished:[L,D]`, `raw:[L,D]`, `thickness`, `edges:{L0,L1,D0,D1}` em mm de fita (0 sem fita). L0/L1 são extremos do eixo L; D0/D1 extremos de D. `raw.L = finished.L - L0 - L1`; `raw.D = finished.D - D0 - D1`.

Cada chapa: `id`, `size:[L,D]`, `trim`, `kerf`, `placements:[{id,x,y,rotated}]`. Coordenadas desde canto da chapa bruta; `rotated:true` troca L/D. `rotation_allowed:false` impede rotação para padrão/veio. O contrato mínimo verifica afastamento entre retângulos pela serra, não exequibilidade guilhotinada. `passes:[{id,sheet_id,...}]` enumera operações reais; mantenha tipo, posição, peça resultante e sequência também na fonte completa.

Amplie a fonte com ambiente, equipamentos, portas, juntas, ferragens, usinagens, LED, circuitos, sobras e custos. Crie validadores específicos desses campos conforme a solução. O arquivo exemplo é sintético e não deve ser convertido automaticamente em móvel de cliente.

Validação cruzada: mesma revisão nos documentos; mesmos IDs/quantidades no GLB, tabela e PDF; bounding boxes acabadas do GLB contra fonte com tolerância explícita; brutos contra bordas; chapas sem sobreposição; sequência guilhotinada simulada separadamente; subtotais e reservas recalculados; hashes dos arquivos disponibilizados iguais aos gerados. Preserve snapshots para comparar alterações, não para alimentar artefatos novos.
