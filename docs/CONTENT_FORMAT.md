# Contrato de conteúdo VÉRTICE

1. `id` numérico publicado nunca deve ser reutilizado.
2. IDs de blocos (`uint16`) são separados de IDs de itens (`uint32`).
3. Keys textuais (`namespace:key`) são estáveis e servem para inspeção/debug.
4. Caminhos de assets são relativos à raiz do pacote, sempre com `/`.
5. Cada atualização deve incrementar `version` em `manifest.json`; alterações incompatíveis incrementam `schema_version` ou `generator_version` conforme o caso.
6. A engine valida tamanho, tipo, hash e versão antes de aceitar conteúdo baixado.
7. Conteúdo declarativo pode ser consumido por implementações conhecidas; não execute scripts remotos arbitrários.
8. Mesma seed + mesma versão de algoritmo + mesmos parâmetros publicados devem preservar o mesmo resultado do mundo.
