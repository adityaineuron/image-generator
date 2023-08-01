# image-generator

The Image Generator project introduces a cutting-edge application of the OpenAI API, leveraging the powerful image-alpha-001 model. With this innovative project, users can now unlock the potential of artificial intelligence to create stunning and unique images effortlessly.
Driven by the image-alpha-001 model, the Image Generator project pushes the boundaries of creativity by enabling users to generate high-quality images tailored to their preferences. The model's advanced capabilities allow for the synthesis of intricate visual elements, such as abstract shapes, textures, and patterns, ensuring that every generated image is truly one-of-a-kind.


## Adding openapi key to environment variables

Step 1. Search for 'Edit the system environment variables' in control panel.

Step 2. Click on 'Environment variables' 

Step 3. Click on new button for adding environment variable for openapi key

Step 4. Give variable name as 'OPENAI_API_KEY' and varaible value should be your openapi key

Step 5. click on ok


## How to run?

Step 1. Cloning the repository.

```bash
git clone https://github.com/adityaineuron/image-generator-using-openai.git
```

Step 2. Create a conda environment.

```bash
conda create -p env python=3.8 -y
```

Step 3. Activate the environment - 

```bash
conda activate env/
```

Step 4. Install necessary requirements

```bash
pip install -r requirements.txt
```

Step 5. Run the main.py file

```bash
python main.py
```