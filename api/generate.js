import fetch from 'node-fetch';

export default async function handler(req, res) {
    if (req.method !== 'POST') {
        res.status(405).json({ error: 'Only POST requests are allowed' });
        return;
    }

    const API_TOKEN = process.env.HUGGING_FACE_API_TOKEN;
    const MODEL_NAME = 'OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5';
    const prompt = req.body.prompt;

    console.log('Received prompt:', prompt);  // Add logging to track the prompt

    try {
        const response = await fetch(`https://api-inference.huggingface.co/models/${MODEL_NAME}`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${API_TOKEN}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                inputs: prompt,
                parameters: { temperature: 0.7, max_new_tokens: 100 }
            })
        });

        const data = await response.json();
        res.status(200).json({ text: data[0]?.generated_text || 'No response generated' });
    } catch (error) {
        console.error('Error fetching AI Assistant response:', error);
        res.status(500).json({ error: 'Error occurred while fetching response' });
    }
}
