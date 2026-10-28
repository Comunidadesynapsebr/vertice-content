# VÉRTICE Content — repositório de conteúdo (0.1.0-alpha)

Este pacote é destinado ao repositório GitHub **`vertice-content`**. Ele separa o conteúdo versionado do código do motor: imagens, definições de blocos/biomas/itens, receitas e parâmetros documentados de geração de mundo.

## Conteúdo

- `assets/source_tiles/tiles/`: os 174 PNGs recebidos em `tiles.zip`, preservados nas nove categorias e sem renomear os arquivos de origem.
- `assets/runtime/atlas.png`: atlas inicial de 64 × 64 já usado pela base VÉRTICE Engine 0.1.0-alpha.
- `data/asset_registry.json`: catálogo com caminho, categoria, dimensões e SHA-256 de cada imagem enviada.
- `data/blocks.json`: IDs de bloco estáveis de 16 bits (0 = ar; 1–8 correspondem à base atual).
- `data/biomes.json`: regras declarativas iniciais de tundra, deserto, floresta e planície.
- `data/worldgen.json`: parâmetros documentados do gerador atual, incluindo chunks, relevo, temperatura, umidade, cavernas e árvores.
- `data/items.json`, `data/recipes.json` e `data/loot_tables.json`: estruturas de conteúdo para os sistemas que serão adicionados futuramente.
- `data/textures.json` e `data/texture_aliases.json`: atlas inicial e aliases semânticos de textura.
- `scripts/validate_pack.py`: valida JSON, IDs duplicados, referências básicas e arquivos do catálogo.
- `previews/tile_catalog.png`: visão geral para revisar os assets visualmente.

## Nome sugerido do repositório

**`vertice-content`**

Descrição sugerida: `Pacote versionado de conteúdo do VÉRTICE: texturas, blocos, biomas, itens, receitas e configuração de geração procedural.`

## Importante: conteúdo versus código

A engine deve continuar responsável por executar código nativo e renderizar. O repositório entrega **dados e imagens**, não código executável remoto. O motor pode baixar um manifesto e arquivos versionados, validar schema/hash e carregar conteúdo conhecido; nunca deve executar scripts arbitrários baixados da internet.

A base do motor alpha fornecida antes ainda não possui carregador dinâmico para este pacote. Por isso, estes arquivos organizam o repositório, mas não alteram automaticamente o APK até implementarmos o carregador e o mapeamento de texturas. `worldgen.json` documenta parâmetros da lógica atual; o gerador Java ainda precisa ser ligado a essa configuração.

## As imagens recebidas

Os arquivos originais têm dimensões variáveis (aproximadamente 78–81 × 83–87 px) e são preservados como **assets de origem/candidatos**. Eles não são tratados automaticamente como texturas tileáveis de cubo. A inspeção visual, recorte/normalização e mapeamento final a blocos devem ocorrer antes de trocar o atlas runtime.

## Validação local

Requer Python 3.10+ e Pillow para gerar a prévia. Para validar o pacote:

```bash
python scripts/validate_pack.py
```

Para regenerar a prévia do catálogo:

```bash
python scripts/build_catalog.py
```

## Publicar no GitHub

Crie um repositório com nome `vertice-content`, extraia este ZIP e envie o **conteúdo da pasta `vertice-content/` para a raiz do repositório**. Não envie o ZIP aninhado como único arquivo se o objetivo for que os manifestos e diretórios sejam navegáveis.

## Licenciamento

A estrutura JSON, os scripts de validação e a documentação são fornecidos para este projeto. As imagens foram fornecidas no arquivo `tiles.zip`; verifique direitos e autoria antes de escolher licença pública para os assets. Este pacote não presume que os PNGs podem ser redistribuídos sob uma licença aberta.
