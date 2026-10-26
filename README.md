# API de LLM sin censura para LATAM — compatible con OpenAI

> API compatible con OpenAI para equipos de LATAM. Español neutro por defecto, prompt de sistema respetado, sin párrafo de advertencia al inicio de cada respuesta. Base: https://uncensored-llm.sbs/v1

**API:** https://uncensored-llm.sbs/v1
**Sitio:** https://uncensored-llm.sbs

Los equipos de LATAM suelen trabajar con modelos entrenados y afinados para otro mercado: responden en inglés aunque el prompt esté en español, y cuando el tema toca política, salud, dinero o seguridad devuelven un párrafo de advertencia en lugar de la respuesta. Para un producto en español eso es un defecto, no una función de seguridad. Esta página documenta una API compatible con OpenAI que responde al pedido tal como fue hecho.

## Por qué importa en LATAM

Un chatbot de atención al cliente en México o Colombia que responde con disclaimers quema la conversación en el segundo mensaje. Un generador de contenido que se niega a escribir sobre cripto o salud deja al redactor escribiendo solo. Y un equipo de seguridad que hace pentesting autorizado no puede pelearse con el modelo cada vez que pide una explicación técnica. El problema no es solo el idioma: es que el modelo decide por vos qué podés preguntar. Acá la decisión vuelve al equipo de producto, con la única excepción del contenido ilegal.

## Llamada de ejemplo

```bash
export UNLLM_KEY="sk-..."
curl https://uncensored-llm.sbs/v1/chat/completions \
  -H "Authorization: Bearer $UNLLM_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"uncensored-llm","messages":[{"role":"user","content":"Explica sin rodeos como se calcula el valor de mercado de una criptomoneda."}],"stream":true}'
```

```python
# pip install openai
from openai import OpenAI
client = OpenAI(base_url="https://uncensored-llm.sbs/v1", api_key="sk-...")
r = client.chat.completions.create(
    model="uncensored-llm",
    messages=[{"role": "user", "content": "Explica sin rodeos como se calcula el valor de mercado de una criptomoneda."}],
)
print(r.choices[0].message.content)
```

```javascript
import OpenAI from "openai";
const ai = new OpenAI({ baseURL: "https://uncensored-llm.sbs/v1", apiKey: process.env.UNLLM_KEY });
const r = await ai.chat.completions.create({ model: "uncensored-llm", messages: [{ role: "user", content: "Explica sin rodeos como se calcula el valor de mercado de una criptomoneda." }] });
console.log(r.choices[0].message.content);
```

## Casos de uso habituales

| Caso | Motivo |
|---|---|
| Atención al cliente | Un bot que resuelve y no se escuda en políticas internas. |
| Contenido en español | Textos, guiones y correos con registro local real. |
| Investigación de seguridad | Trabajo ofensivo con autorización escrita del cliente. |
| Ficción adulta (18+) | Escenas explícitas entre adultos, sin elipsis. |

## Latencia por país

La latencia la manda tu operador, no tu bandera. Medí desde tu máquina antes de culpar a la API:

```bash
curl -o /dev/null -s -w '%{time_total}s\n' https://uncensored-llm.sbs/v1/models
```

| Ciudad | País |
|---|---|
| Ciudad de México | México |
| Guadalajara | México |
| Monterrey | México |
| Bogotá | Colombia |
| Medellín | Colombia |
| Lima | Perú |
| Santiago | Chile |
| Buenos Aires | Argentina |
| Córdoba | Argentina |
| Quito | Ecuador |
| Caracas | Venezuela |
| Ciudad de Guatemala | Guatemala |

## Preguntas reales

### ¿Es realmente compatible con OpenAI?

Sí: /v1/chat/completions, /v1/models y streaming SSE con el mismo formato de eventos. El SDK oficial funciona cambiando base_url.

### ¿Hay plan gratuito o de prueba?

Las condiciones vigentes están publicadas en https://uncensored-llm.sbs. Cada cambio de precios se anuncia ahí, no en este repositorio.

### ¿Qué se bloquea?

Contenido ilegal, incluido cualquier material con menores. Si el pedido no cae ahí, la respuesta es sobre el pedido.

### ¿Puedo usarlo con LlamaIndex o LangChain?

Sí, como proveedor compatible con OpenAI. También sirve para Open WebUI, LibreChat y cualquier frontend que acepte una base URL propia.

### ¿Cómo protejo la clave?

Variable de entorno por entorno, rotación periódica y nunca en el frontend ni en un repositorio público.

## Esta documentación en otros idiomas

- [pt-BR] https://brown1023.github.io/llm-api-sem-censura-brasil/
- [id-ID] https://ryuuless.github.io/uncensored-llm-api-indonesia/
- [vi-VN] https://ryuuless.github.io/uncensored-llm-api-vietnam/
- [tr-TR] https://askcode24.github.io/sansursuz-llm-api-turkiye/
- [de-DE] https://askcode24.github.io/uncensored-llm-api-deutschland/
- [es-ES] https://palazuel0s2004.github.io/api-llm-sin-censura-espana/
- [it-IT] https://palazuel0s2004.github.io/llm-api-senza-censura-italia/
- [en-IN] https://nirav0712.github.io/uncensored-llm-api-india/
- [en-PH] https://nirav0712.github.io/uncensored-llm-api-philippines/
- [ar] https://mohamedabderrehman.github.io/uncensored-llm-api-arabia/
- [ar-EG] https://mohamedabderrehman.github.io/uncensored-llm-api-egypt/

---

uncensored-llm.sbs — API compatible con OpenAI. Se bloquea contenido ilegal, incluido cualquier material con menores. El resto es responsabilidad de quien llama.