export async function streamText(text, onUpdate) {

    let current = "";

    const words = text.split(" ");

    for (const word of words) {

        current += word + " ";

        onUpdate(current);

        await new Promise(resolve => setTimeout(resolve, 25));

    }

}