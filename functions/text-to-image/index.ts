// Importing the 'serve' function from the Deno standard library for HTTP server
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'

// Importing the Hugging Face Inference library
import { HfInference } from 'https://esm.sh/@huggingface/inference@2.3.2'

// Creating a new instance of HfInference with the Hugging Face access token from the environment variables
const hf = new HfInference(Deno.env.get('HUGGING_FACE_ACCESS_TOKEN'))

// Listening for incoming HTTP requests
serve(async (req) => {
  // Parsing the JSON data from the incoming request
  const { prompt } = await req.json()

  // Converting the text input to an image using the Hugging Face Inference library
  const image = await hf.textToImage(
    {
      inputs: prompt, // Text prompt
      model: 'stabilityai/stable-diffusion-2', // Model for text to image conversion
    },
    {
      use_cache: false, // Disabling caching
    }
  )

  // Returning the converted image as the response
  return new Response(image)
})
