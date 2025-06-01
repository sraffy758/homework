## (Ex 1) Do a benchmark of Inpainting solutions

The following inpainting methods were selected for evaluation based on their availability as open-source tools or their compatibility with integration pipelines such as ComfyUI:
• SDXL Inpainting (SDXL model finetuned for inpainting tasks)
• AlbedoXL + Foocus (patch-based adaptation for inpainting)
• AlbedoXL + BrushNet (dual-branch architecture tailored for inpainting)
• Flux-Fill Dev (Flux Dev variant finetuned for inpainting)
• Flux-Fill Pro (Flux Pro variant finetuned for inpainting)

To evaluate and compare these approaches, we used two consistent test cases:
• Generating a shiba inu on a carpet in a living room
• Adding a red throw blanket on a sofa
For both use cases, we paid close attention to object quality, image coherence (e.g., carpet pattern consistency, lighting, and shadows).
Each method was tested with two inpainting strategies:
• Global inpainting on the full image.
• Localized inpainting on a cropped, upscaled region surrounding the mask, giving the model more context to work with.
In our comparison, we considered the following criteria:
• Inference time (not deeply analyzed here, as all methods performed within ~30s on standard hardware)
• Integration capabilities (e.g., ease of use in ComfyUI)
• Adaptability (support for finetuning, LoRA training, compatibility with workflows)
• Pricing model
• And most importantly, image quality (evaluated in a separate section).
The comparison table below focuses on integration, adaptability, and cost. Visual quality assessments follow afterward.

| Nom                 | Intégration | Adaptabilité | Note   |
| ------------------- | ----------- | ------------ | ------ |
| SDXL inpainting     | Open-Source | Comfy        | Medium |
| AlbedoXL + Foocus   | Open-Source | Comfy        | Good   |
| AlbedoXL + Brushnet | Open-Source | Comfy        | Good   |
| Flux-fill dev       | Licence +   | Comfy        | Medium |
| Flux-fill pro       | API ++      | API          | Bad    |

Using these methods within ComfyUI provides greater flexibility and control over the generation process.
Both Foocus and BrushNet offer compatibility with any standard SDXL model, making them highly adaptable across different checkpoints.
In contrast, SDXL Inpainting and Flux-Fill Dev require dedicated inpainting models but can still be extended via LoRA finetuning.
Flux-Fill Pro, however, offers limited control, as it operates exclusively through API calls.
From a cost perspective:
• Flux-Fill Pro is the most expensive solution and requires external API access.
• Flux-Fill Dev requires a license.
• The other solutions are fully open-source and free to use.
While all these factors matter — integration, cost, and adaptability — the most critical criterion remains image quality, which is where Presti demonstrates its strongest advantage.

Use Case 1 – Shiba Inu on a Carpet
The Flux models offered the most convincing integration of the shiba inu, especially in terms of preserving the carpet’s pattern and texture.
With SDXL-based models, while the dog’s positioning and proportions were generally accurate, the asset quality was noticeably lower compared to the Flux outputs.
Regarding inpainting strategies, global inpainting provided better results in terms of scale consistency and lighting coherence across the image.

Use Case 2 – Red Plaid on a Sofa
SDXL Inpaint and BrushNet struggled to integrate the plaid naturally into the scene.
Foocus delivered better prompt adherence — successfully generating a casually draped plaid, as requested — but the asset quality varied significantly between runs.
Flux Fill Pro produced good image quality and respected the prompt relatively well.
However, Flux Fill Dev provided the most seamless integration and the highest asset quality, although its prompt adherence was weaker: the plaid appeared neatly folded in all generations, regardless of the instruction.

Overall, SDXL-based models show weaker integration with the environment. While their visual quality is generally good, it tends to be inconsistent across generations.
On the other hand, Flux models outperform SDXL models in terms of asset integration and offer superior asset quality. Flux Fill Pro appears to have the best prompt adherence among all models tested.

Based on these observations, I would recommend choosing a Flux-based solution.
Among the available options, Flux Fill Dev stands out as the most adaptable — it could be further improved through task-specific finetuning, making it a solid candidate for production.

Of course, this recommendation is based on a preliminary evaluation.
A more comprehensive benchmark could include A larger number of generations with the use of quantitative performance metrics such as:
• CLIP Score (prompt adherence)
• LPIPS (Learned Perceptual Image Patch Similarity)
• NIQE (Naturalness and perceptual quality)

Additionally, A/B testing could be used to support the selection process through direct human preference comparisons.

There are a few ways we could improve the results or explore alternatives:
• We could try using more advanced models like in-context inpainting or InstructPix2Pix, which allow better control by following text instructions or using more context from the image.
• To improve image quality, especially in terms of lighting and sharpness, we can apply relighting (adjusting the light in the image) and upscaling (to increase resolution and detail).
• If we want to keep the original background unchanged, one solution is to: 1. Isolate the generated object using a segmentation method, 2. Place it back on the original image, and 3. Apply relighting to match shadows and lighting for a more natural result.

This way, we can keep the environment consistent while improving how the object fits into the scene.
