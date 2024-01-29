from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa as lb
from fastapi import FastAPI, Form, UploadFile
from typing import Annotated
import uvicorn

app = FastAPI()

@app.post("/TryEngSub")
def audio_subtitle(audio: UploadFile):
    
    # load model and processor
    processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")
    model.config.forced_decoder_ids = None

    # receive audio files and save it in disk
    with open('temp/audio.mpeg','wb+') as file:
     file.write(audio.file.read())
    
    wave, sr = lb.load('temp/audio.mpeg', sr = 16000)
    input_features = processor(wave, sampling_rate=sr, return_tensors="pt").input_features 

    # generate token ids
    predicted_ids = model.generate(input_features)
    # decode token ids to text
    #transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)

    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    return transcription
    



if __name__=="__main__":
    uvicorn.run(app)